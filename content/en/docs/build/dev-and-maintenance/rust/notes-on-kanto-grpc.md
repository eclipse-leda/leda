---
title: "Communicating with Кanto-CM via gRPC"
date: 2023-01-03T17:24:56+05:30
weight: 1
---

Kanto container management binds to a unix socket (default: `/run/container-management/container-management.sock`) and exposes a gRPC interface which can be used to obtain all the functionality of the `kanto-cm` cli programatically. 

The easiest way to access this API through Rust is by creating a new Rust crate:

```shell
$ cargo new talk-to-kanto
```

## Dependencies 

The most feature-rich gRPC library for Rust right now is tonic. Add the following to your `Cargo.toml` to make tonic and the tokio async runtime available to your crate. Tower and hyper are needed to be able to bind to the unix socket.

```toml
[dependencies]
prost = "0.11"
tokio = { version = "1.0", features = [ "rt-multi-thread", "time", "fs", "macros", "net",] }
tokio-stream = { version = "0.1", features = ["net"] }
tonic = {version = "0.8.2" }
tower = { version = "0.4" }
http = "0.2"
hyper = { version = "0.14", features = ["full"] }
serde = { version = "1.0.147", features = ["derive"] }
serde_json = { version = "1.0.89", default-features = false, features = ["alloc"] }



[build-dependencies]
tonic-build =  "0.8.2"
```

## Compiling protobufs

The easiest way to obtain the kanto-cm `.proto` files is to add the container management repo in your project root as a git submodule:

```shell
$ git submodule init
$ git submodule add https://github.com/eclipse-kanto/container-management.git
$ git submodule update --init --recursive
```

You should now have the `container-management` repository available.

To build the `.proto` files during compile time, define a custom `build.rs` in the project root

```shell
$ touch build.rs
```

Add the following main function to the `build.rs`:

```Rust
fn main() -> Result<(), Box<dyn std::error::Error>> {
    tonic_build::configure()
        .build_server(false)
        .include_file("mod.rs")
        .type_attribute(".", "#[derive(serde::Serialize, serde::Deserialize)]")
        .compile(
            &["api/services/containers/containers.proto"],
            &["container-management/containerm/"],
        )?;
    Ok(())
}
```

Here it is important to know that tonic does not like deeply nested protobufs such as those for kanto-cm. That is why the line `.include_file("mod.rs")` re-exports everything in a seperate module which can later be included in the main.rs file.

`"#[derive(serde::Serialize, serde::Deserialize)]"` makes all structures (de-)serializable via serde.

## Importing generated Rust modules

Now in `src/main.rs` add the following to import the generated Rust modules:

```Rust
pub mod cm {
    tonic::include_proto!("mod");
}
use cm::github::com::eclipse_kanto::container_management::containerm::api::services::containers as cm_services;
use cm::github::com::eclipse_kanto::container_management::containerm::api::types::containers as cm_types;
```

Now all kanto-cm services as namespaced under `cm_services`.

## Obtaining a unix socket channel

To obtain a unix socket channel:

```Rust
use tokio::net::UnixStream;
use tonic::transport::{Endpoint, Uri};
use tower::service_fn;

let socket_path = "/run/container-management/container-management.sock";

let channel = Endpoint::try_from("http://[::]:50051")?
    .connect_with_connector(service_fn(move |_: Uri| UnixStream::connect(socket_path)))
    .await?;
```

This is a bit of a hack, because currently, tonic+tower don't support binding directly to an unix socket. Thus in this case we attemp to make an http connection to a non-existent service on port `5051`. When this fails, the fallback method `connect_with_connector()` is called where a tokio UnixStream is returned and the communication channel is generated from that.

## Making a simple gRPC call to kanto-cm

All that is left is to use the opened channel to issue a simple "list containers" request to kanto.

```Rust
// Generate a CM client, that handles containers-related requests (see protobufs)
let mut client = cm_services::containers_client::ContainersClient::new(channel);
let request = tonic::Request::new(cm_services::ListContainersRequest {});
let response = client.list(request).await?;
```

Since we made all tonic-generated structures (de-)serializable we can use `serde_json::to_string()` to print the response as a json string.

```Rust
println!("{}", serde_json::to_string(&response)?);
```
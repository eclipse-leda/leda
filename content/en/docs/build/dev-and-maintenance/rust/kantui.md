---
title: "Kantui"
date: 2023-01-03T17:24:56+05:30
weight: 3
---

The k8s ecosystem comes with a lot of utilies that allow for the easier management of containers (such as k9s). The [kantui util](https://github.com/eclipse-leda/leda-utils/tree/main/src/rust/kanto-tui) aims to be a "nice" text user interface that lets the user start/stop/remove/get logs of deployed containers in kanto-cm.

![kantui screenshot](https://github.com/eclipse-leda/leda-utils/blob/main/src/rust/kanto-tui/misc/kantocmcurses-ss.png?raw=true)

## Development notes

This tool is again based on the ideas in [Communicating with Кanto-CM via gRPC](../notes-on-kanto-grpc). 

It spins up two threads - an UI thread (drawing/updating UI) and an IO thread (communicating with kanto-cm via gRPC). The communication between these two threads happens over an [async-priority-channel](https://crates.io/crates/async-priority-channel) with `ListContainers` request having a lower priority than `Start/Stop/Remove/Get Logs` ("user interaction") requests.

This in an "eventually fair" mechanism of communication. That way even if kanto-cm is handling a slow request (such as stopping a container that does not respect SIGTERM) the UI thread is never blocked, allowing for a responsive-feeling UI. The size of the channel is 5 requests and the UI is running at 30 fps. Thus even if the UI gets out-of-sync with the actual state of container management it would be "only" for 5 out 30 frames.

## Cursive and ncurses-rs

The [cursive](https://crates.io/crates/cursive) crate is used as a high level "framework" as it allows very easy handling of UI events via callbacks, though this might be prone to callback hell.

The default backend for cursive is ncurses-rs which a very thin Rust wrapper over the standart ncurses library. This in theory would be the optimal backend for our case as ncurses is a very old and stable library that has buffering (other backends lead to flickering of the UI on updates) and is dynamically linked (smaller final binary size).

The ncurses-rs wrapper however is **not well-suited to cross-compilation** as it has a custom build.rs that generates a small C program, compiles it for the target and tries to run it on the host. The only reason for this C program to exist is to check the width of the _char_ type. Obviously, the char type on the host and the target might be of different width and this binary might not even run on the host machine if the host and target architectures are different.

After coming to the conclusion that the ncurses-rs backend was not suitable, kantui was migrated to the termion backend + the [cursive_buffered_backend](https://crates.io/crates/cursive_buffered_backend) crate which mitigates the flickering issue.

```toml
[dependencies]
...
cursive_buffered_backend = "0.5.0"

[dependencies.cursive]
default-features=false
version = "0.16.2"
features = ["termion-backend"]
```

This completely drops the need for ncurses-rs but results in a slightly bigger binary (all statically linked).

## Bitbake Recipe

The recipe was created following the guidelines in [Generating bitbake recipes with cargo-bitbake](../../#generating-bitbake-recipes-with-cargo-bitbake) and can be found in [meta-leda/meta-leda-components/recipes-sdv/eclipse-leda/](https://github.com/eclipse-leda/meta-leda/tree/main/meta-leda-components/recipes-sdv/eclipse-leda).


## Future improvement notes

- The gRPC channel can get blocked thus effectively "blocking" the IO-thread until it is freed-up again. Maybe open a new channel for each request (slow/resource heavy)?

- Reorganize the code a bit, move all generic functionally in the lib.rs.
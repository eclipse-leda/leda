---
title: "Developing and Maintaining Utils"
date: 2023-01-03T17:24:56+05:30
weight: 10
---

The Leda teams provides some custom utilities that allow for a more integrated end-user experience. They can be found in the main leda-utils repository on GitHub: [eclipse-leda/leda-utils](https://github.com/eclipse-leda/leda-utils).

The following pages are meant to serve as both internal documentation and general guidelines when developing for Leda.

## Bash

Leda uses the classic Bourne shell as its main shell, thus all scripts should be sh-compatible (use the `#!/bin/sh` shebang). As a Poky+OE-based distro we use BusyBox for core-utils. To check explicitly for *"bashisms"* in your scripts, the
`checkbashisms` tool might be useful.

[**Utility-Specific Pages**](shell/)

The bash-based leda-utils are all deployed with the same recipe under the sdv-base packagegroup: [meta-leda/meta-leda-components/recipes-sdv/sdv-base](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-components/recipes-sdv/sdv-base).

## Rust

The current _main_ branch for leda-distro (and meta-leda) is based on the Kirkstone Yocto/Poky release.

### Toolchain version

The version of the Rust toolchain available in OE (Kirkstone) is **1.59.0**. Make sure to target **1.59.0** (or earlier) when developing Rust-based utils for leda. To set **1.59.0** as your default Rust version on your development machine:

```shell
$ rustup install 1.59.0
$ rustup default 1.59.0
```

```shell
$ cargo --version
cargo 1.59.0 (49d8809dc 2022-02-10)
```

### Generating bitbake recipes with cargo-bitbake

After making sure your toolchain is on version **1.59.0** go trough a clean build of your Rust binary:

```shell
$ cd <rust_project_dir>
$ cargo clean
$ rm Cargo.lock
$ cargo build --release
```

This will make sure the Cargo.lock is re-generated with packages matching the Rust version. The `cargo.bbclass` on which Rust recipes are based, requires all Rust crates + their version (matching the Cargo.toml) to be specified as a "SRC_URI +=". This can become tedious and error-prone if done by hand. That's why meta-rust provides a tool called `cargo-bitbake` that generates a minimal recipe with all the crates it finds in the `Cargo.lock` files of the project.

```shell
$ cargo install --locked cargo-bitbake
$ cd <rust_project_dir>
$ cargo bitbake
```

This will generate a recipe in the project root which you can use as a starting point.

Example: [kantui_git.bb](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-components/recipes-sdv/eclipse-leda/kantui_git.bb)

Note this recipe will only build your Rust crate. To deploy/install your binary you have to define a `.inc` file with the same name as the recipe that would handle the installation.

Example: [kantui.inc](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-components/recipes-sdv/eclipse-leda/kantui.inc)

### Known bugs

The built-in `proc_macros` crate is not being imported properly by meta-rust (Kirkstone), thus breaking all library crates that define a proc_macro ([meta-rust issue 266](https://github.com/meta-rust/meta-rust/issues/266)). To fix this create a `libstd-rs_%.bbappend` file containing the single line:

```bash
S = "${RUSTSRC}/library/test"
```

meta-leda already provides this fix [here](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-components/recipes-sdv/eclipse-leda/libstd-rs_%25.bbappend), so it should not be necessary to implement it again.

### "Fat" Link time optimization

LTO is a nice feature of LLVM that can optimize even through language boundaries at link-time, but leads to longer overall build times. That is why Rust by default uses "thin" LTO which may result in larger/slower binaries. "Fat" LTO can be enabled when building release binaries by adding to the `Cargo.toml` file the following section:

```toml
[profile.release]
lto = true
```

For [kantui](rust/kantui) this leads to reduction of the final binary size from ~8 MiB to ~5 MiB.

More information on profile-optimizations can be found [here](https://doc.rust-lang.org/cargo/reference/profiles.html).

**Note**: Stripping the debug symbols completely results in further binary size reduction, but BitBake fails with a QA problem when deploying stripped binaries.

### Rust-based utilities

[**Utility-Specific Pages**](rust/)
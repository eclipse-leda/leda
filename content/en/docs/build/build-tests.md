---
title: "Building tests"
date: 2022-05-09T14:24:56+05:30
weight: 4
---

# Cross Compiling to X86_64 on Ubuntu 20.04

There is currently a step to cross-compile tests to X86_64. In order to successfully run the step, you need to make sure that the following artifacts are available on the runner:

- rustc + cargo: ``curl https://sh.rustup.rs -sSf | sh``
- docker: follow https://docs.docker.com/engine/install/ubuntu/ and afterwards https://docs.docker.com/engine/install/linux-postinstall/
- build-essential: ``sudo apt-get install build-essential``
- cross (0.1.16): ``cargo install cross --version 0.1.16``
- jq: ``sudo apt-get install jq -y``

You may restart your current shell so that all components are available as env vars.

---
title: "VSCode DevContainer"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

## Preparation

- Obtain the [Docker Engine](https://docs.docker.com/engine/install/) for your distribution and add your non-privileged user to the docker group (`sudo usermod -aG docker $USER` )
- Install [Visual Studio Code](https://code.visualstudio.com/download   )

## Visual Studio Code: Development Containers

- Open Visual Studio Code
- Open Command Palette (`F1`) and select `Clone repository in Container Volume`
- Select `eclipse-leda/meta-leda` and the main branch.
- Adapt proxy configurations if necessary (`.devcontainer/proxy.sh`)

*For a clean remote build machine, you may want to [set up a development environment on GitHub CodeSpaces](/leda/docs/build/devenv/github-codespaces/)*

## Building Leda in a VSCode DevContainer:

After successfully setting up your DevContainer you can build Leda either with kas or manually:

- To build with kas follow the instructions at: [Building with kas](/leda/docs/build/devenv/build-kas-manually/#building-with-kas)

- To build manually: [Building manually](/leda/docs/build/devenv/build-kas-manually/#building-manually)


## Authentication

The build process requires online connection and you must be authenticated to access private repositories.

1. Create a GitHub Personal Access Token (PAT) at https://github.com/settings/tokens and grant `read:packages` permission
2. Use `Configure SSO` and authorize your PAT for the organization
3. On the build host, authenticate to ghcr.io: `skopeo login ghcr.io --authfile ~/auth.json --username <username>` and enter the PAT as password
   - You may need to create the folder where skopeo is storing authentication information beforehand:
   ```bash
   sudo mkdir -p /run/containers/1000
   sudo chmod a+w /run/containers/1000
   ```
4. Start the bitbake build process


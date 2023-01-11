---
title: "Advanced topics"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

## Git Authentication

For private repositories, we need to separately authenticate against the submodule repositories, as
GitHub Codespaces will only inject a token with access rights to the current repository.

1. Change to the users home directory

    ```bash
    cd ~
    ```

2. Install https://github.com/GitCredentialManager/git-credential-manager

    ```bash
    curl -LO https://raw.githubusercontent.com/GitCredentialManager/git-credential-manager/main/src/linux/Packaging.Linux/install-from-source.sh &&
    sh ./install-from-source.sh &&
    git-credential-manager-core configure
    ```

3. Configure a credential store typ, e.g. `git config --global credential.credentialStore plaintext`
4. Verify with `git config --global -l`, it should show git-credential-manager-core as the credential helper.

## Update the submodules

Run `git submodule update --recursive`

See https://github.com/microsoft/vscode/issues/109050 for details.

## Setup skopeo

Skopeo is needed to download various files during the build:

```bash
sudo mkdir -p /run/containers/1000
sudo chmod a+w /run/containers/1000
skopeo login ghcr.io --authfile ~/auth.json --username <your GitHub User> 
```

Enter your token when asked for the password.

---
title: "Incubation Components"
date: 2022-05-09T14:24:56+05:30
weight: 10
---

# Building private components

Some components are not yet released to the public. 

To build them, or to integrate them to the image, these components need to be manually downloaded first.

## sdv-databroker-cli

- Install GitHub CLI
- Add to `local.conf` to include in image:

```
CORE_IMAGE_EXTRA_INSTALL += " sdv-databroker-cli"
```

- Manually login to GitHub CLI

```
    unset GITHUB_TOKEN
    gh auth login
```

    Output:
```
? What account do you want to log into? GitHub.com
? You're already logged into github.com. Do you want to re-authenticate? Yes
? What is your preferred protocol for Git operations? HTTPS
? How would you like to authenticate GitHub CLI? Login with a web browser

! First copy your one-time code: A123-C12B
Press Enter to open github.com in your browser... 
✓ Authentication complete.
- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as johndoe
```

- Manually download the release artifacts:
```
    $ gh release download v0.14.0 \
        --archive=zip \
        --repo eclipse-leda/incubator-vehicleapi \
        --dir downloads
    
    $ gh release download v0.14.0 \
        --pattern 'bin_release_databroker_*.tar.gz' \
        --repo eclipse-leda/incubator-vehicleapi \
        --dir downloads
```
- Build the recipe:
```
cd poky
source oe-init-build-env ../build-sdv-x86_64
bitbake sdv-databroker-cli
```
- Build the image:
```
bitbake sdv-image-minimal
```

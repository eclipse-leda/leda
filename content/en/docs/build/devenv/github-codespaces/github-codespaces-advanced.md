---
title: "Advanced topics"
date: 2022-05-09T14:24:56+05:30
weight: 1
---

# Setting up GitHub Codespaces

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

## Run the build
Now the actual build can be started:

```bash
cd /workspace/leda-distro/poky
source oe-init-build-env ../build-sdv-x86_64/
cd /workspace/leda-distro
./build-x86_64.sh
```

## Run qemu 
Start qemu with the new image:
```bash
runqemu qemux86-64 nographic slirp qemuparams="-m 2048"
```

## Start the k3s pods

Create the secret ConnectionString for the cloudconnector:
```bash
kubectl create secret generic cloudagent \
            --from-literal=PrimaryConnectionString='<<<ConnectionString>>>'
```

Create the secret needed to pull images from ghcr:
```bash
kubectl create secret docker-registry ghcr-io \
    --docker-server=ghcr.io \
    --docker-username=<your github username> \
    --docker-password=<your github personal access token>
```

check the pods, you should now have them running:
```bash
root@qemux86-64:~# kubectl get pods
NAME                                  READY   STATUS    RESTARTS   AGE
sdv-core-vehicle-update-manager-pod   1/1     Running   1          127m
mosquitto-76bcf4956f-bpncv            1/1     Running   1          127m
cloud-connector                       1/1     Running   18         37m
```

## Subscribe to a topic with the mosquitto in the pod:
```bash
kubectl exec --stdin --tty mosquitto -- /bin/sh
mosquitto_sub -v -t '#'
```





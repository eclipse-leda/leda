---
title: "Kanto Auto deployer"
date: 2023-01-03T17:24:56+05:30
weight: 2
---

**TLDR**: To deploy a container in the final Leda image, all you generally need to do is add the manifest in the [kanto-containers](https://github.com/eclipse-leda/meta-leda/tree/main/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers) directory and re-build.

Kanto-CM does not provide (currently) an out-of-the box feature that allows for the automatic deployment of containers through manifest files similar to k3s' automated deployment of k8s-manifests found in the `/var/lib/rancher/k3s/server/manifests` directory.

This can be worked around via a bash script for each container that runs on boot and makes sure it's deployed. Even though this approach is functional it is not very structured and would require a lot repeating code.

That is why the "[Kanto Auto deployer](https://github.com/eclipse-leda/leda-utils/tree/main/src/rust/kanto-auto-deployer)" tool was developed. It directly implements the ideas in [Communicating with Кanto-CM via gRPC](../notes-on-kanto-grpc).

The compiled binary takes a path to a directory containing the json manifests, parses them into Rust structures and sends gRPC requests to kanto container management to deploy these containers.
If the container is already deployed the manifest is ignored.

## Manifest structure

Kanto auto deployer uses the exact same structure for its manifests as the internal representation of container state in kanto container management. For example:

```json
{
    "id": "",
    "name": "databroker",
    "image": {
        "name": "ghcr.io/eclipse/kuksa.val/databroker:0.2.5",
        "decrypt_config": null
    },
    "host_name": "",
    "domain_name": "",
    "resolv_conf_path": "",
    "hosts_path": "",
    "hostname_path": "",
    "mounts": [],
    "hooks": [],
    "host_config": {
        "devices": [],
        "network_mode": "bridge",
        "privileged": false,
        "restart_policy": {
            "maximum_retry_count": 0,
            "retry_timeout": 0,
            "type": "unless-stopped"
        },
        "runtime": "io.containerd.runc.v2",
        "extra_hosts": [],
        "port_mappings": [],
        "log_config": {
            "driver_config": {
                "type": "json-file",
                "max_files": 2,
                "max_size": "100M",
                "root_dir": ""
            },
            "mode_config": {
                "mode": "blocking",
                "max_buffer_size": ""
            }
        },
        "resources": null
    },
    "io_config": {
        "attach_stderr": false,
        "attach_stdin": false,
        "attach_stdout": false,
        "open_stdin": false,
        "stdin_once": false,
        "tty": false
    },
    "config": null,
    "network_settings": null,
    "state": {
        "pid": -1,
        "started_at": "",
        "error": "",
        "exit_code": 0,
        "finished_at": "",
        "exited": false,
        "dead": false,
        "restarting": false,
        "paused": false,
        "running": false,
        "status": "",
        "oom_killed": false
    },
    "created": "",
    "manually_stopped": false,
    "restart_count": 0
}
```

The only difference to the actual internal state representation is that fields in the manifest can be left empty (`""`) if they are not important for the deployment. These values will be filled in with defaults by kanto-cm after deployment.

For example, you do not need to specify the container "id" in the manifest, as an unique uuid would be assigned automatically after deployment.

## Container deployment in Leda

Kanto-auto-deployer runs as a one-shot service on boot that goes through the manifest folder (default: `/var/containers/manifests`) and deploys required containers.

The Bitbake recipe for building and installing the auto deployer service can be found at [kanto-auto-deployer_git.bb](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-components/recipes-sdv/eclipse-leda/kanto-auto-deployer_git.bb). 

This recipe also takes all manifests in the [kanto-containers](https://github.com/eclipse-leda/meta-leda/tree/main/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers) directory and installs them in the directory specified by the `KANTO_MANIFESTS_DIR` BitBake variable (weak default: `/var/containers/manifests`).

**Important**: To deploy a container in the final Leda image, all you generally need to do is add the manifest in the [kanto-containers](https://github.com/eclipse-leda/meta-leda/tree/main/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers) directory and re-build.

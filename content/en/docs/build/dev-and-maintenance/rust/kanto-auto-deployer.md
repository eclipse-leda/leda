---
title: "Kanto Auto deployer (KAD)"
date: 2023-01-03T17:24:56+05:30
weight: 2
---

**TLDR**: To deploy a container in the final Leda image, all you generally need to do is add the manifest in the [kanto-containers](https://github.com/eclipse-leda/meta-leda/tree/main/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers) directory and re-build.

Kanto-CM does not provide (currently) a _stable_ feature that allows for the automatic deployment of containers through manifest files similar to k3s' automated deployment of k8s-manifests found in the `/var/lib/rancher/k3s/server/manifests` directory.

This can be worked around via a bash script for each container that runs on boot and makes sure it's deployed. Even though this approach is functional it is not very structured and would require a lot repeating code.

That is why the "[Kanto Auto deployer](https://github.com/eclipse-leda/leda-utils/tree/main/src/rust/kanto-auto-deployer)" tool was developed. It directly implements the ideas in [Communicating with Кanto-CM via gRPC](../notes-on-kanto-grpc).

The compiled binary takes a path to a directory containing the json manifests, parses them into Rust structures and sends gRPC requests to kanto container management to deploy these containers.



## Manifest structure

Because Kanto CM uses different JSON formats for the interal state representation of the container (from the gRPC API) and for the deployment via the Container Management-native `init_dir`-mechanism, KAD supports both through the "manifests_parser" module.
The conversion between formats is automatic (logged as a warning when it's attempted)
 so you **do not** need to provide extra options when using one or the other.

### Container Management Manifests Format

This is the CM-native format, described in the [Kanto-CM documentation](https://eclipse.dev/kanto/docs/references/containers/container-config/#template). 
It is the **recommended** format since KAD is supposed to be replaced by native CM deployment modules in the future and this manifest 
format will be compatible with that.

It also allows you to ommit options (defaults will be used). KAD will issue a log warning when the "manifests_parser" attempts to convert this manifest format
to the gRPC message format (internal state representation).

### Internal State Representation

The KAD "native" manifests format uses the exact same structure for its manifests as the internal representation of container state in kanto container management. 
This manifest format **does not** allow keys in the json to be ommited, so these manifests are generally larger/noisier.
For example:

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
        "port_mappings": [
            {
              "protocol": "tcp",
              "container_port": 55555,
              "host_ip": "localhost",
              "host_port": 30555,
              "host_port_end": 30555
            }
        ],
        "log_config": {
            "driver_config": {
                "type": "json-file",
                "max_files": 2,
                "max_size": "1M",
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
    "config": {
        "env": [
            "RUST_LOG=info",
            "vehicle_data_broker=debug"
        ],
        "cmd": []
    },
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

Kanto-auto-deployer can run as a one-shot util that goes through the manifest folder (default: `/data/var/containers/manifests`) and deploys required containers.

When you pass the `--daemon` flag it would enable the "filewatcher" module that would continuously monitor the provided path for changes/creation of manifests.

The Bitbake recipe for building and installing the auto deployer service can be found at [kanto-auto-deployer_git.bb](https://github.com/eclipse-leda/meta-leda/blob/main/meta-leda-components/recipes-sdv/eclipse-leda/kanto-auto-deployer_git.bb). 

This recipe also takes all manifests in the [kanto-containers](https://github.com/eclipse-leda/meta-leda/tree/main/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers) directory and installs them in the directory specified by the `KANTO_MANIFESTS_DIR` BitBake variable (weak default: `/var/containers/manifests`).

**Important**: To deploy a container in the final Leda image, all you generally need to do is add the manifest in the [kanto-containers](https://github.com/eclipse-leda/meta-leda/tree/main/meta-leda-components/recipes-sdv/eclipse-leda/kanto-containers) directory and re-build.

## Conditional compilation of the filewatcher module

To reduce binary bloat the `--daemon` option is namespaced under the `filewatcher` conditional compilation flag (enabled by default).
To compile KAD without the filewatcher module run: `cargo build --release --no-default-features`.
(Implemented in [Leda Utils PR#35](https://github.com/eclipse-leda/leda-utils/pull/35))


---
title: "Velocitas VApps"
date: 2022-05-09T14:24:56+05:30
---

For local deployment without a cloud backend, deployment specifications for [Eclipse Velocitas](https://projects.eclipse.org/projects/automotive.velocitas) Vehicle Apps may be put directly onto the device.

- Create a Kanto deployment specification for your vehicle app. You may copy one of the existing JSON files in `/data/containers/manifests` as a template
- Copy the specification file to the device, e.g. `scp -P 2222 myapp.json root@localhost:/data/containers/manifests/`
- Apply the specification: `systemctl restart kanto-auto-deployer`

To update an existing container when the configuration has changed, delete the container and restart kanto-auto-deployer:

    kanto-cm remove -n myapp-example
    # Edit /data/containers/manifests/myapp.json
    kanto-auto-deployer

## Example Deployment Specification

> Attention: The current implementation requires all fields to be present in the JSON, even if the values are not set or used. Do not remove any fields, as it may break the functionality.

```json
{
    "id": "",
    "name": "myapp-example",
    "image": {
        "name": "ghcr.io/my-org/my-repo/my-app:latest",
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
              "container_port": 50151,
              "host_ip": "localhost",
              "host_port": 50151,
              "host_port_end": 50151
            }
        ],
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
    "config": {
        "env": [
           "VEHICLEDATABROKER_DAPR_APP_ID=vehicledatabroker"
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

---
title: "sdv-health"
date: 2023-01-03T17:24:56+05:30
weight: 1
---

A general utility for monitoring the status of important sdv services/containers/devices.

## Checking the status of kanto-cm containers

Kanto CM containers are split into two groups - required and optional. Both groups are checked, but only a warning is issued when an optional container is missing/not working.

General code for checking the status is:

```bash
if [ -n "$KANTO_CM_CONTAINERS_OPT" ]; then
	printf -- "$SEPARATOR\n"

	printf -- "${COL_WHITE}[Kanto CM Containers (OPTIONAL)]${COL_NC}\n"
	if [[ ${CM_STATUS} != *"inactive"*  ]]; then
		
		# "Optional containers"
		KANTO_CM_LIST=$(${KANTO_CMD} list)
		# removes tabs, splits on pipe and takes the container name column ($2)
		FOUND_CONTAINERS=($(echo "$KANTO_CM_LIST" | awk -F'|' '{gsub(/\t/, ""); print $2}')) # array with all kanto container names
		# removes tabs, splits on pipe and takes the container status colum ($4)
		FOUND_CONTAINERS_STATES=($(echo "$KANTO_CM_LIST" | awk -F'|' '{gsub(/\t/, ""); print $4}')) # array with all kanto container states
		KANTO_CM_CONTAINERS_ARR=( $KANTO_CM_CONTAINERS_OPT )

		for expectedCtr in ${KANTO_CM_CONTAINERS_ARR[@]}; do
			CTR_IDX=$(get_array_element_index ${expectedCtr} ${FOUND_CONTAINERS[@]})
			if [ ! -z $CTR_IDX ]; then
				status=${FOUND_CONTAINERS_STATES[$CTR_IDX]}
				if [ "$status" = "Running" ]; then
					printf "  * %-40s : $TEXT_OK\n" "${expectedCtr}"
				else
					printf "  * %-40s : $TEXT_WARN (%s)\n" "${expectedCtr}" "$status"
				fi
			else
				printf "  * %-40s : $TEXT_WARN (%s)\n" "${expectedCtr}" "NOT FOUND"
			fi
		done

	else
		printf "  * %-40s : $TEXT_FAIL (%s)\n" "Kanto Container Management" "Unavailable"
	fi

fi
```

Here it is important to know that `kanto-cm list` outputs the list of containers in a different order every time it's called. That is why, `kanto-cm list` is invoked once and its output is stored in a variable:

```bash
	KANTO_CM_LIST=$(${KANTO_CMD} list)
```

Output:

```shell

ID                                   	|Name                                 	|Image                                                       	|Status    	|Finished At                     |Exit Code 	|
-------------------------------------	|-------------------------------------	|------------------------------------------------------------	|----------	|------------------------------  |----------	|
d0cf1367-996d-4c83-bcc5-37d6acba9966 	|feedercan                            	|ghcr.io/eclipse/kuksa.val/databroker:0.2.5                  	|Running   	|2022-12-30T23:04:28.340430098Z  |0         	|
f58425b0-9260-4a15-a6fc-5c59f8840839 	|vehicledatabroker13                  	|ghcr.io/eclipse/kuksa.val/databroker:0.2.5                  	|Created   	|                                |0         	|
f8a716f7-d2c5-4165-a081-407a7acb7643 	|vehicledatabroker13                  	|ghcr.io/eclipse/kuksa.val/databroker:0.2.5                  	|Stopped   	|2022-12-05T11:38:02.0213865Z    |137       	|
627f068a-b9eb-400b-826b-868f6b79e9d8 	|vehicledatabroker13                  	|ghcr.io/eclipse/kuksa.val/databroker:0.2.5                  	|Running   	|2022-12-30T23:03:58.144873827Z  |0         	|
62ba3e6f-af01-4518-8393-00a5ba553062 	|databroker                           	|ghcr.io/eclipse/kuksa.val/databroker:0.2.5                  	|Stopped   	|2022-12-07T11:38:28.418199429Z  |137       	|
753a0b10-d72a-4065-8c27-758ed9a77c2d 	|vehicledatabroker13                  	|ghcr.io/eclipse/kuksa.val/databroker:0.2.5                  	|Created   	|                                |0         	|

```

So we use awk to split on pipe (column), strip unecessary tabs. `print $2` then gives us the container name and `print $4` - its status.

sdv-health then proceeds to check if every container specified in the list is available and if its status is `Running`.

Note: `Exited` is considered a fail-state.


## Checking kanto-cm socket

This is a simple `test -s` check for the default socket path.

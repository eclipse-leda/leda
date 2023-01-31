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


ID                                      |Name                                   |Image                                                                                                                          |Status         |Finished At                     |Exit Code   |
-------------------------------------   |-------------------------------------  |------------------------------------------------------------                                                                   |----------     |------------------------------  |----------  |
d82a406e-80d7-4d2c-8044-3799544fc39a    |vum                                    |ghcr.io/eclipse-leda/leda-contrib-vehicle-update-manager/vehicleupdatemanager:main-1d8dca55a755c4b3c7bc06eabfa06ad49e068a48    |Running        |                                |0           |
0f079856-767c-4e8d-b4df-a2323392849f    |cloudconnector                         |ghcr.io/eclipse-leda/leda-contrib-cloud-connector/cloudconnector:main-47c01227a620a3dbd85b66e177205c06c0f7a52e                 |Exited         |2023-01-31T11:58:01.564126452Z  |1           |
e4cf317e-c2d3-42c7-8f12-8ecf6f9d5d7a    |databroker                             |ghcr.io/eclipse/kuksa.val/databroker:0.2.5                                                                                     |Running        |                                |0           |
6440a9b6-4fb8-4735-b3de-484286ac705b    |feedercan                              |ghcr.io/eclipse/kuksa.val.feeders/dbc2val:v0.1.1                                                                               |Running        |                                |0           |
efbd572b-3331-4f19-9b17-7c69511ec5ca    |hvacservice-example                    |ghcr.io/eclipse/kuksa.val.services/hvac_service:v0.1.0                                                                         |Running        |                                |0           |
6d9a6f07-1659-4b51-9ddb-6e9ade64f2fd    |seatservice-example                    |ghcr.io/eclipse/kuksa.val.services/seat_service:v0.1.0                                                                         |Running        |                                |0           |
06b0ddf2-7c91-41e4-9a00-4213ee361cdf    |sua                                    |ghcr.io/eclipse-leda/leda-contrib-self-update-agent/self-update-agent:build-12                                                 |Running        |                                |0           |

```

So we use awk to split on pipe (column), strip unecessary tabs. `print $2` then gives us the container name and `print $4` - its status.

sdv-health then proceeds to check if every container specified in the list is available and if its status is `Running`.

Note: `Exited` is considered a fail-state.


## Checking kanto-cm socket

This is a simple `test -s` check for the default socket path.

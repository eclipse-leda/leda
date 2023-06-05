#!/bin/bash
# /********************************************************************************
# * Copyright (c) 2023 Contributors to the Eclipse Foundation
# *
# * See the NOTICE file(s) distributed with this work for additional
# * information regarding copyright ownership.
# *
# * This program and the accompanying materials are made available under the
# * terms of the Apache License 2.0 which is available at
# * https://www.apache.org/licenses/LICENSE-2.0
# *
# * SPDX-License-Identifier: Apache-2.0
# ********************************************************************************/
#
# Setup:
# sudo apt-get install python3.10
# sudo apt-get update
# sudo apt-get install pip
# pip install vss-tools
# git clone https://github.com/COVESA/vss-tools.git

# git clone --recurse-submodules https://github.com/COVESA/vehicle_signal_specification
# pushd vehicle_signal_specification
# git checkout --detach
# git for-each-ref refs/remotes/origin --format='../%(refname:lstrip=3) %(refname:lstrip=3)'|grep -v ' HEAD$' |xargs -n 2 git worktree add
# popd

./vspecjson2markdown.py -I release/3.1/spec -i VehicleSignalSpecification.vspec -u release/3.1/spec/units.yaml -o output


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
# sudo apt-get install python3
# sudo apt-get update
# sudo apt-get install pip
# pip install vss-tools mako anytree

# Auto-detect the latest COVESA VSS release from GitHub
GITHUB_API_URL="https://api.github.com/repos/COVESA/vehicle_signal_specification/releases/latest"
DEFAULT_VSS_VERSION="6.0"

echo "Detecting latest VSS release..."
LATEST_TAG=$(curl -s "${GITHUB_API_URL}" | python3 -c "import sys, json; print(json.load(sys.stdin)['tag_name'])" 2>/dev/null || echo "")

if [ -z "${LATEST_TAG}" ]; then
    echo "Could not auto-detect latest version, using default: v${DEFAULT_VSS_VERSION}"
    LATEST_TAG="v${DEFAULT_VSS_VERSION}"
fi

VSS_VERSION="${LATEST_TAG#v}"
echo "Using VSS version: ${VSS_VERSION} (tag: ${LATEST_TAG})"

# Download and extract the VSS specification if not already present
VSS_DIR="/tmp/vehicle_signal_specification-${VSS_VERSION}"
if [ ! -d "${VSS_DIR}" ]; then
    echo "Downloading VSS ${VSS_VERSION}..."
    DOWNLOAD_URL="https://github.com/COVESA/vehicle_signal_specification/archive/refs/tags/${LATEST_TAG}.zip"
    curl -L "${DOWNLOAD_URL}" -o "/tmp/vss_${VSS_VERSION}.zip"
    unzip -q "/tmp/vss_${VSS_VERSION}.zip" -d /tmp/
fi

SPEC_DIR="${VSS_DIR}/spec"
echo "Using spec directory: ${SPEC_DIR}"

# Clean up old output before regenerating
echo "Cleaning output directory..."
rm -rf output

./vspecjson2markdown.py \
    -I "${SPEC_DIR}" \
    -i "${SPEC_DIR}/VehicleSignalSpecification.vspec" \
    -u "${SPEC_DIR}/units.yaml" \
    -q "${SPEC_DIR}/quantities.yaml" \
    -o output


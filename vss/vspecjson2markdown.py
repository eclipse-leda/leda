#!/usr/bin/env python3
# /********************************************************************************
# * Copyright (c) 2023-2026 Contributors to the Eclipse Foundation
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
# Requires: pip install vss-tools mako

import argparse
import os
from pathlib import Path

from vss_tools.datatypes import dynamic_quantities, dynamic_units
from vss_tools.main import validate_tree
from vss_tools.tree import VSSNode, build_tree
from vss_tools.units_quantities import load_quantities, load_units
from vss_tools.vspec import load_vspec

from io import StringIO
from mako.template import Template
from mako.runtime import Context


class MarkdownNode:
    """Expose the template's node properties over vss-tools' data model."""

    def __init__(self, node: VSSNode):
        self._node = node

    @property
    def children(self):
        return [MarkdownNode(child) for child in self._node.children]

    @property
    def name(self):
        return self._node.name

    @property
    def description(self):
        return self._value("description")

    @property
    def comment(self):
        return self._value("comment")

    @property
    def deprecation(self):
        return self._value("deprecation")

    @property
    def default(self):
        return self._value("default")

    @property
    def min(self):
        return self._value("min")

    @property
    def max(self):
        return self._value("max")

    @property
    def allowed(self):
        return self._value("allowed")

    @property
    def uuid(self):
        return self._value("constUID")

    @property
    def data_type_str(self):
        datatype = self._value("datatype")
        if datatype and getattr(self._node.data, "arraysize", None) is not None:
            return f"{datatype}[]"
        return datatype

    def qualified_name(self):
        return self._node.get_fqn()

    def has_unit(self):
        return bool(self._value("unit"))

    def get_unit(self):
        return self._value("unit")

    def _value(self, field):
        value = getattr(self._node.data, field, None)
        return "" if value is None else value

    def _is_type(self, node_type):
        return self._node.data.type.value == node_type

    def is_actuator(self):
        return self._is_type("actuator")

    def is_property(self):
        return self._is_type("property")

    def is_attribute(self):
        return self._is_type("attribute")

    def is_branch(self):
        return self._is_type("branch")

    def is_sensor(self):
        return self._is_type("sensor")

    def is_signal(self):
        return self._node.data.type.value in {"sensor", "actuator", "attribute", "property"}

    def is_struct(self):
        return self._is_type("struct")

    def is_orphan(self):
        return False

parser = argparse.ArgumentParser(
                    prog='vspecjson2markdown.py',
                    description='Convert VSS VSpec-JSON to Markdown pages',
                    epilog='This utility is part of the Eclipse Leda project')

parser.add_argument('-I', '--include',
                    action='append',
                    type=str,
                    default=[],
                    required=True,
                    help='The Vehicle Signal Specification include directory search list')

parser.add_argument('-i', '--input',
                    required=True,
                    help='The Vehicle Signal Specification .vspec file')

parser.add_argument('-u', '--units',
                    action='append',
                    metavar='unit_file',
                    type=str,
                    default=[],
                    required=False,
                    help='The Vehicle Signal Specification units.yaml file')

parser.add_argument('-q', '--quantities',
                    action='append',
                    metavar='quantities_file',
                    type=str,
                    default=[],
                    required=False,
                    help='The Vehicle Signal Specification quantities.yaml file')

parser.add_argument('-o', '--output',
                    required=True,
                    help='The output directory where to store the generated Markdown files')

parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag

args = parser.parse_args()

print("Arguments:")
print("Verbose: %s" % args.verbose)
print("VSpec Include Directory: %s" % args.include)
print("VSpec Input file: %s" % args.input)
print("VSpec Units file: %s" % args.units)
print("VSpec Quantities file: %s" % args.quantities)
print("Output directory: %s" % args.output)

input_path = Path(args.input).resolve()
vspec_dir = input_path.parent
print("VSpec Directory: %s" % vspec_dir)

unit_files = [Path(path).resolve() for path in args.units]
quantity_files = [Path(path).resolve() for path in args.quantities]
if not unit_files and (vspec_dir / "units.yaml").exists():
    unit_files = [vspec_dir / "units.yaml"]
if not quantity_files and (vspec_dir / "quantities.yaml").exists():
    quantity_files = [vspec_dir / "quantities.yaml"]

quantity_data = load_quantities(quantity_files)
dynamic_quantities.extend(quantity_data)
unit_data = load_units(unit_files)
for key, unit_definition in unit_data.items():
    if unit_definition.unit is not None:
        dynamic_units[unit_definition.unit] = unit_definition
    dynamic_units[key] = unit_definition

include_dirs = [Path(path).resolve() for path in args.include]
vspec_data = load_vspec(include_dirs, [input_path])
tree, _ = build_tree(vspec_data.data, connect_orphans=True)
tree.expand_instances()
tree.resolve()
validate_tree(tree)

outputdir=os.path.realpath(args.output)
print("Absolute output directory: %s" % outputdir)
os.makedirs(args.output, mode=0o777, exist_ok=True)

def export_node(node : VSSNode):
    markdown_node = MarkdownNode(node)
    print("Exporting: %s" % markdown_node.qualified_name())
   
    outfilename=markdown_node.qualified_name().replace(".",os.path.sep) + os.path.sep + "_index.md"
    outfilepath=os.path.join(outputdir, outfilename)
    os.makedirs(os.path.dirname(outfilepath), mode=0o777, exist_ok=True)
    
    mytemplate = Template(filename='vss.mako.md')
    buf = StringIO()
    
    unit = dynamic_units.get(markdown_node.get_unit(), "") if markdown_node.has_unit() else ""
    ctx = Context(buf, node=markdown_node, unit=unit)
    
    mytemplate.render_context(ctx)
    with open(outfilepath, "w") as outfile:
        outfile.write(buf.getvalue())

    for child in node.children:
        export_node(child)

export_node(tree)

print("Done")
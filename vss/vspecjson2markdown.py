#!/usr/bin/env python3
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
# https://pypi.org/project/json-stream/
# Requires: pip install json-stream

import argparse
import json
import os
import json_stream
from enum import Enum
from vspec.model.vsstree import VSSNode, Unit
from vspec.model.constants import VSSTreeType
from vspec.loggingconfig import initLogging
from anytree import Node, RenderTree, AsciiStyle
import logging
import sys
import vspec

from io import StringIO
from mako.template import Template
from mako.runtime import Context
from mako.lookup import TemplateLookup

initLogging()

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
print("Output directory: %s" % args.output)

vspec_dir = os.path.dirname(os.path.realpath(args.input))
print("VSpec Directory: %s" % vspec_dir)

vspec.load_units(args.input,args.units)

data_type_tree = None
tree = vspec.load_tree(args.input, args.include, VSSTreeType.SIGNAL_TREE)
vspec.check_type_usage(tree, VSSTreeType.SIGNAL_TREE, data_type_tree)
vspec.expand_tree_instances(tree)
vspec.clean_metadata(tree)
vspec.verify_mandatory_attributes(tree, abort_on_unknown_attribute=True)

outputdir=os.path.realpath(args.output)
print("Absolute output directory: %s" % outputdir)
os.makedirs(args.output, mode=0o777, exist_ok=True)

def export_node(node : VSSNode):
    print("Exporting: %s" % node.qualified_name())
   
    outfilename=node.qualified_name().replace(".",os.path.sep) + os.path.sep + "_index.md"
    outfilepath=os.path.join(outputdir, outfilename)
    os.makedirs(os.path.dirname(outfilepath), mode=0o777, exist_ok=True)
    
    mytemplate = Template(filename='vss.mako.md')
    buf = StringIO()
    
    unit=""
    if node.has_unit():
        unit = Unit.from_str(node.get_unit())
    ctx = Context(buf, node=node, unit=unit)
    
    mytemplate.render_context(ctx)
    outfile = open(outfilepath, "w")
    outfile.write(buf.getvalue())

    for child in node.children:
            export_node(child)

export_node(tree)

print("Done")
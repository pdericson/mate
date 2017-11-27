"""Mate

Aye Aye, Captain!

Usage:
  mate FILE...

"""

from __future__ import print_function

import json
import logging
import os
import re
import sys

import docopt
import jsonschema
import yaml

import mate


def main():
    args = docopt.docopt(__doc__, version=mate.__version__)

    logging.basicConfig(format="%(message)s")

    for path in args['FILE']:
        with open(path) as f:
            if re.search(r'\.ya?ml$', path, re.I):
                resource = yaml.load(f.read())
            else:
                resource = json.load(f)

        if resource is None or 'kind' not in resource:
            logging.error("Unknown resource.")
            sys.exit(1)

        schema_path = os.path.join(os.path.dirname(__file__), 'data/kubernetes-json-schema/v1.8.1-local')

        with open(os.path.join(schema_path, resource['kind'].lower() + 'spec.json')) as f:
            schema = json.load(f)

        resolver = jsonschema.RefResolver('file://' + schema_path + '/', None)
        try:
            jsonschema.validate(resource, schema, resolver=resolver)
        except jsonschema.ValidationError as exc:
            logging.error("{}: {}".format(path, exc))
            sys.exit(1)


if __name__ == '__main__':
    main()

#!/bin/bash

set -xeuE

./example.py --template "example.jinja2" --number "first" --iterable passing list of arguments "arg with spaces"
./example.py --template "example.jinja2" --number "second" --boolean

exit 0

#!/bin/bash

set -e
echo '---------------------------Running PEP8---------------------------'
for f in $(find requestOn -name '*.py' -or -name '*.doc'); do pep8 $f; done
echo '------------------------------------------------------------------'

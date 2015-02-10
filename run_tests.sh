#!/bin/bash

echo '---------------------------Running PEP8---------------------------'
for f in $(find ../checkit -name '*.py' -or -name '*.doc'); do pep8 $f; done
echo '------------------------------------------------------------------'
echo '---------------------------Running Tests--------------------------'
python3 tests/test.py

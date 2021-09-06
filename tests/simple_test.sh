#!/bin/bash

cat basic_test/text.txt | basic_test/slowprint.sh | ../src/tellme.py

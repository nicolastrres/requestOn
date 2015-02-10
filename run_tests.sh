#!/bin/bash
FILES=/path/to/*
for f in $FILES
do

  echo "Processing $f file..."
  # take action on each file. $f store current file name
  cat $f
done
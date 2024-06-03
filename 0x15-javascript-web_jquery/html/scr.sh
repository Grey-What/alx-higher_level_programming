#!/bin/bash

# Loop through numbers 0 to 12
for i in {0..12}; do
  # Create a file with the current number in the filename
  touch "${i}-main.html"
done

echo "Created 13 files from 0-main.htm to 12-main.htm"

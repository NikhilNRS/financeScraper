#!/bin/bash

# Navigate to the root directory of your raw collected data
cd "$(dirname "$0")"

# Find and print the absolute path of all CSV files in the current and subdirectories
find "$(pwd)" -type f -name "*.csv"

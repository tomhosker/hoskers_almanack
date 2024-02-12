#!/bin/sh

### This code extracts a given range of pages from the full Almanack into its
### own PDF file.

# Local constants.
PATH_TO_INPUT="$(dirname $0)/../almanack.pdf"

# Check arguments.
if [ $# -ne 2 ]; then
    echo "Usage: sh $0 START STOP" 1>&2
    exit 1
fi

# Set variables.
path_to_output="$HOME/split_almanack_$1_$2.pdf"

# Let's get cracking...
pdftk $PATH_TO_INPUT cat $1-$2 output $path_to_output
echo "Wrote split PDF to path: $path_to_output"

#!/bin/sh

### This code install the necessary third-party software for this project.

# Crash on the first non-zero exit code.
set -e

# Local constants.
APT_PACKAGES="pdftk sqlitebrowser texlive-full"
PATH_TO_THIS_FOLDER="$(dirname "$0")"
PATH_TO_REQUIREMENTS="$PATH_TO_THIS_FOLDER/pip_requirements.txt"

# Let's get cracking...
sudo apt install --yes $APT_PACKAGES
pip install -r $PATH_TO_REQUIREMENTS

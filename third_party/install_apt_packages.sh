#!/bin/sh

### This script installs the necessary APT packages for working with this
### project. Note that the these packages will be installed centrally, and not
### in the local virtual environment.

# Crash on the first non-zero exit code.
set -e

# Local constants.
APT_PACKAGES="pdftk sqlitebrowser texlive-full"

# Let's get cracking...
sudo apt install --yes $APT_PACKAGES

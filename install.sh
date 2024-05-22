#!/bin/sh

### This code defines a script which makes the necessary installations for
### working with and on this project on this device.

# Crash on the first non-zero exit code.
set -e

# Local constants.
PATH_TO_THIS_DIR=$(dirname $(realpath $0))
PATH_TO_THIRD_PARTY_DIR="$PATH_TO_THIS_DIR/third_party"
PATH_TO_INSTALL_APT_PACKAGES="$PATH_TO_THIRD_PARTY_DIR/install_apt_packages.sh"
PATH_TO_BUILD_VENV="$PATH_TO_THIRD_PARTY_DIR/build_venv.sh"

# Let's get cracking...
sh $PATH_TO_INSTALL_APT_PACKAGES
sh $PATH_TO_BUILD_VENV
echo "You can now activate the virtual environment with: . venv/bin/activate"

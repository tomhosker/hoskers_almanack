"""
This code defines the install script.
"""

# Standard imports.
import shutil
import warnings
from pathlib import Path

# Bespoke imports.
from hosker_utils import install_apt_packages

# Local constants.
PATH_TO_GTKSOURCEVIEW = "/usr/share/gtksourceview-4"
SOURCE_PATH_FOR_HPML_LANG = "hpml/hpml.lang"
TARGET_PATH_FOR_HPML_LANG = \
    str(Path(PATH_TO_GTKSOURCEVIEW)/"language-specs"/"hpml.lang")
APT_PACKAGES = ("sqlitebrowser", "texlive-full")

#############
# FUNCTIONS #
#############

def install_hpml_lang():
    """ Install the HPML language features in Gedit. """
    if not Path(TARGET_PATH_FOR_HPML_LANG).exists():
        if Path(PATH_TO_GTKSOURCEVIEW).exists():
            shutil.copy(SOURCE_PATH_FOR_HPML_LANG, TARGET_PATH_FOR_HPML_LANG)
        else:
            message = (
                "The folder "+PATH_TO_GTKSOURCEVIEW+" does not exist on this "+
                "machine. Therefore, it has not been possible to install the "+
                "HPML language features into Gedit."
            )
            warnings.warn(message)

def install():
    """ The main function. """
    install_apt_packages(APT_PACKAGES)
    install_hpml_lang()

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    install()

if __name__ == "__main__":
    run()

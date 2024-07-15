"""
This script compiles the almanack PDF.
"""

# Standard imports.
import argparse

# Local imports.
from source import build_pdf

###################
# RUN AND WRAP UP #
###################

def make_parser():
    """ Return a parser argument. """
    result = \
        argparse.ArgumentParser(
            description="Compile the Almanack"
        )
    result.add_argument(
        "--preserve-tex-files",
        action="store_true",
        default=False,
        dest="preserve_tex_files",
        help="Preserve the .tex files used to build the PDFs"
    )
    return result

def run():
    """ Run this file. """
    parser = make_parser()
    arguments = parser.parse_args()
    build_pdf(clean=(not arguments.preserve_tex_files))

if __name__ == "__main__":
    run()

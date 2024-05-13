"""
This code defines a script which checks the correctness of the HPML code in the
database.
"""

# Standard imports.
import argparse

# Local imports.
from source.validate_hpml import validate_hpml_in_article, validate_all_hpml

####################
# HELPER FUNCTIONS #
####################

def make_parser():
    """ Return an argument parser. """
    result = \
        argparse.ArgumentParser(
            description="Validate HPML"
        )
    result.add_argument(
        "--article-id",
        help="If validating a specific article only, give its ID",
        dest="article_id"
    )
    return result

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    parser = make_parser()
    arguments = parser.parse_args()
    if arguments.article_id:
        validate_hpml_in_article(arguments.article_id)
    else:
        validate_all_hpml()

if __name__ == "__main__":
    run()

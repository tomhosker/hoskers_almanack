"""
This code runs all the integration tests in this directory.
"""

# Local imports.
from integration_tests.test_hpml import test_hpml

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    test_hpml()

if __name__ == "__main__":
    run()

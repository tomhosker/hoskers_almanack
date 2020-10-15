"""
This code uploads all the files in /uploads to the database.
"""

# Standard imports.
import os
import sys

# Local imports.
import constants
from uploader import Uploader

#############
# FUNCTIONS #
#############

def batch_upload(folder="uploads/"):
    """ This is where the magic happens. """
    files = os.listdir(folder)
    for fn in files:
        if ((fn == "TEMPLATE.hpml") or ("TEST" in fn) or
            not fn.endswith(".hpml")):
            continue
        uploader = Uploader("uploads/"+fn)
        if uploader.upload():
            os.system("rm uploads/"+fn)
        else:
            print("Could not upload "+fn+".")

###########
# TESTING #
###########

def test():
    """ Run unit tests. """
    os.system("cp uploads/TEST1.hpml uploads/t1.hpml")
    os.system("cp uploads/TEST2.hpml uploads/t2.hpml")
    batch_upload()
    # Remember to clean up the database!

###################
# RUN AND WRAP UP #
###################

def run():
    if "--test" not in sys.argv:
        batch_upload()

if __name__ == "__main__":
    run()

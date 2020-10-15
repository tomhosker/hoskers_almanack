"""
This code runs all of the unit tests in this directory.
"""

# Standard imports.
import os

# Local constants.
THIS_FILENAME = "run_all_unit_tests.py"

#############
# FUNCTIONS #
#############

def test_file(filename):
    """ Ronseal. """
    if (not filename.endswith(".py")) or (filename == THIS_FILENAME):
        return
    print("Testing "+filename+"...")
    if os.system("python3 "+filename+" --test") != 0:
        raise Exception("At least one unit test in "+filename+" failed.")

def test_folder(foldername, first, completed):
    """ Ronseal. """
    os.chdir(foldername)
    for item in os.listdir():
        if os.path.isdir(item):
            if item in completed:
                continue
            test_folder(item, first, completed)
        else:
            test_file(item)
    completed.append(os.getcwd())
    os.chdir("..")
    if os.getcwd() == first:
        return

###################
# RUN AND WRAP UP #
###################

def run():
    test_folder(".", os.getcwd(), [])

if __name__ == "__main__":
    run()

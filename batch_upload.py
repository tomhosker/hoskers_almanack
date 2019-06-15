### This code uploads all the files in "/uploads".

# Imports.
import os, sys

# Local imports.
import constants
from uploader import Uploader

# The function in question.
def batch_upload():
  files = os.listdir("uploads/")
  for fn in files:
    if ((fn == "TEMPLATE.hpml") or ("TEST" in fn) or
        (fn.endswith(".hpml") == False)):
      continue
    else:
      u = Uploader("uploads/"+fn)
      if u.upload():
        os.system("rm uploads/"+fn)
      else:
        print("Could not upload "+fn+".")

# Run unit tests.
def test():
  os.system("cp uploads/TEST1.hpml uploads/t1.hpml")
  os.system("cp uploads/TEST2.hpml uploads/t2.hpml")
  batch_upload()
  # Remember to clean up the database!

# Wrap up.
#test()
batch_upload()

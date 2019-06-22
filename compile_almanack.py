### This code compiles the entire Almanack.

# Imports.
import sys

# Local imports.
from pdf_builder import PDF_builder

# This is where the magic happens.
def compile_almanack(args):
  if len(args) == 1:
    fullness = "full"
  else:
    fullness = args[1]
  mods = []
  for arg in args:
    if args.index(arg) > 1:
      mods.append(arg)
  PDF_builder(fullness, mods)
  print(args)

# Run and wrap up.
def run():
  compile_almanack(sys.argv)
run()

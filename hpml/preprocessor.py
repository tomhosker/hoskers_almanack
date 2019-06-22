### This code holds a class which performs a series of replacement on a
### a snippet of HPML.

# Local imports.
from hpml.constants import fractions

# Helper functions.
def suppress_person_font(hpml):
  while "#PERSON" in hpml:
    hpml = hpml.replace("#PERSON", "")
  return hpml
def suppress_place_font(hpml):
  while "#PLACE" in hpml:
    hpml = hpml.replace("#PLACE", "")
  return hpml
def suppress_publication_font(hpml):
  while "#PUBLICATION" in hpml:
    hpml = hpml.replace("#PUBLICATION", "#ITAL")
  return hpml
def suppress_foreign_font(hpml):
  while "#FOREIGN" in hpml:
    hpml = hpml.replace("#FOREIGN", "#ITAL")
  return hpml
def suppress_ship_font(hpml):
  while "#SHIP" in hpml:
    hpml = hpml.replace("#SHIP", "#ITAL")
  return hpml
def suppress_ampersands(hpml):
  while "#ADD" in hpml:
    hpml = hpml.replace("#ADD", "and")
  return hpml
def em_dashes(hpml):
  while " -- " in hpml:
    hpml = hpml.replace(" -- ", " --- ")
  return hpml
def contains_numeric_fractions(hpml):
  for fraction in fractions.keys():
    if fraction in hpml:
      return True
  return False
def suppress_fractions(hpml):
  while contains_numeric_fractions(hpml):
    for fraction in fractions.keys():
      words = fractions[fraction]["words"]
      hpml = hpml.replace(fraction, words)
  return hpml

# This defines a dictionary which maps strings to functions.
mod_lookup = dict()
mod_lookup["suppress-person-font"] = suppress_person_font
mod_lookup["suppress-place-font"] = suppress_place_font
mod_lookup["suppress-publication-font"] = suppress_publication_font
mod_lookup["suppress-foreign-font"] = suppress_foreign_font
mod_lookup["suppress-ship-font"] = suppress_ship_font
mod_lookup["suppress-fractions"] = suppress_fractions
mod_lookup["suppress-ampersands"] = suppress_ampersands
mod_lookup["em-dashes"] = em_dashes

# The class in question.
class Preprocessor:
  def __init__(self, hpml, mods):
    self.hpml = hpml
    self.mods = mods
    self.pre_preprocess()
    self.perform_mods()

  # Handles any mods which are actually an instruction to carry out several
  # sub-mods.
  def pre_preprocess(self):
    if "suppress-non-standard" in self.mods:
      submods = ["suppress-person-font", "suppress-place-font",
                 "suppress-publication-font", "suppress-foreign-font",
                 "suppress-ship-font", "suppress-fractions",
                 "suppress-ampersands"]
      for submod in submods:
        if submod not in self.mods:
          self.mods.append(submod)

  # Performs each mod in "mods" on the code in "hpml".
  def perform_mods(self):
    if self.mods == None:
      return
    for mod in self.mods:
      if mod in mod_lookup.keys():
        function = mod_lookup[mod]
        self.hpml = function(self.hpml)

  # Ronseal.
  def digest(self):
    return self.hpml

# Run unit tests.
def test():
  before = "This #PERSON{Person} is a douchebag."
  after = Preprocessor(before, []).digest()
  assert("#PERSON" in after)
  after = Preprocessor(before, ["suppress-person-font"]).digest()
  assert("#PERSON" not in after)
  before = "This #PLACE{Place} feels #FOREIGN{foreign}."
  after = Preprocessor(before, ["suppress-place-font",
                                "suppress-foreign-font"]).digest()
  assert(("#PLACE" not in after) and ("#FOREIGN" not in after))
  before = "What's a #HALF plus a #THIRD plus a #QUARTER?"
  after = Preprocessor(before, ["suppress-fractions"]).digest()
  assert(("#HALF" not in after) and ("#THIRD" not in after) and
         ("#QUARTER" not in after))
  before = "Fear God -- #ADD take your own part."
  after = Preprocessor(before, ["suppress-ampersands",
                                "em-dashes"]).digest()
  assert(("#ADD" not in after) and (" -- " not in after))
  print("Tests passed!")

# Run and wrap up.
def run():
  test()
#run()

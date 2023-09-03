"""
This code defines a class which performs a series of replacement on a snippet of
HPML.
"""

# Local imports.
from .lexicon import fractions

##############
# MAIN CLASS #
##############

class Preprocessor:
    """ The class in question. """
    def __init__(self, hpml, mods):
        self.mod_lookup = make_mod_lookup()
        self.hpml = hpml
        self.mods = mods
        self.pre_preprocess()
        self.perform_mods()

    def pre_preprocess(self):
        """ Handles any mods which are actually an instruction to carry out
        several sub-mods. """
        if "suppress-non-standard" in self.mods:
            submods = ["suppress-person-font", "suppress-place-font",
                       "suppress-publication-font", "suppress-foreign-font",
                       "suppress-ship-font", "suppress-fractions",
                       "suppress-ampersands"]
            for submod in submods:
                if submod not in self.mods:
                    self.mods.append(submod)

    def perform_mods(self):
        """ Performs each mod in "mods" on the code in "hpml". """
        if not self.mods:
            return
        for mod in self.mods:
            if mod in self.mod_lookup.keys():
                function = self.mod_lookup[mod]
                self.hpml = function(self.hpml)

    def digest(self):
        """ Deprecated. """
        return self.hpml

####################
# HELPER FUNCTIONS #
####################

def suppress_person_font(hpml):
    """ Implement a mod. """
    while "#PERSON" in hpml:
        hpml = hpml.replace("#PERSON", "")
    return hpml

def suppress_place_font(hpml):
    """ Implement a mod. """
    while "#PLACE" in hpml:
        hpml = hpml.replace("#PLACE", "")
    return hpml

def suppress_publication_font(hpml):
    """ Implement a mod. """
    while "#PUBLICATION" in hpml:
        hpml = hpml.replace("#PUBLICATION", "#ITAL")
    return hpml

def suppress_foreign_font(hpml):
    """ Implement a mod. """
    while "#FOREIGN" in hpml:
        hpml = hpml.replace("#FOREIGN", "#ITAL")
    return hpml

def suppress_ship_font(hpml):
    """ Implement a mod. """
    while "#SHIP" in hpml:
        hpml = hpml.replace("#SHIP", "#ITAL")
    return hpml

def suppress_ampersands(hpml):
    """ Implement a mod. """
    while "#ADD" in hpml:
        hpml = hpml.replace("#ADD", "and")
    return hpml

def em_dashes(hpml):
    """ Implement a mod. """
    while " -- " in hpml:
        hpml = hpml.replace(" -- ", " --- ")
    return hpml

def contains_numeric_fractions(hpml):
    """ Implement a mod. """
    for fraction in fractions.keys():
        if fraction in hpml:
            return True
    return False

def suppress_fractions(hpml):
    """ Implement a mod. """
    while contains_numeric_fractions(hpml):
        for fraction in fractions.keys():
            words = fractions[fraction]["words"]
            hpml = hpml.replace(fraction, words)
    return hpml

def make_mod_lookup():
    """ This defines a dictionary which maps strings to functions. """
    result = dict()
    result["suppress-person-font"] = suppress_person_font
    result["suppress-place-font"] = suppress_place_font
    result["suppress-publication-font"] = suppress_publication_font
    result["suppress-foreign-font"] = suppress_foreign_font
    result["suppress-ship-font"] = suppress_ship_font
    result["suppress-fractions"] = suppress_fractions
    result["suppress-ampersands"] = suppress_ampersands
    result["em-dashes"] = em_dashes
    return result

###########
# TESTING #
###########

def test():
    """ Run unit tests. """
    before = "This #PERSON{Person} is a douchebag."
    after = Preprocessor(before, []).digest()
    assert "#PERSON" in after
    after = Preprocessor(before, ["suppress-person-font"]).digest()
    assert "#PERSON" not in after
    before = "This #PLACE{Place} feels #FOREIGN{foreign}."
    after = Preprocessor(before, ["suppress-place-font",
                                  "suppress-foreign-font"]).digest()
    assert ("#PLACE" not in after) and ("#FOREIGN" not in after)
    before = "What's a #HALF plus a #THIRD plus a #QUARTER?"
    after = Preprocessor(before, ["suppress-fractions"]).digest()
    assert "#HALF" not in after
    assert "#THIRD" not in after
    assert "#QUARTER" not in after
    before = "Fear God -- #ADD take your own part."
    after = Preprocessor(before, ["suppress-ampersands",
                                  "em-dashes"]).digest()
    assert "#ADD" not in after
    assert " -- " not in after
    print("Tests passed!")

###################
# RUN AND WRAP UP #
###################

def run():
    test()

if __name__ == "__main__":
    run()

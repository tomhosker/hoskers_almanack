"""
This code defines a class which builds the contents of a given month.
"""

# Standard imports.
import sqlite3

# Local imports.
from .almanack_utils import fetch_to_dict
from .article import Article
from .configs import FULL, ID_KEY, SONGS_KEY, SONNETS_KEY, PROVERBS_KEY
from .monthly_selects import SELECTS

##############
# MAIN CLASS #
##############

class MonthBuilder:
    """ The class in question. """
    # Class attributes.
    SECTION_SEPARATOR = "\n\n"

    def __init__(self, name, fullness=FULL, mods=None):
        self.name = name
        self.fullness = fullness
        self.mods = mods
        self.songs = fetch_to_dict(SELECTS[self.name][SONGS_KEY])
        self.sonnets = fetch_to_dict(SELECTS[self.name][SONNETS_KEY])
        self.proverbs = fetch_to_dict(SELECTS[self.name][PROVERBS_KEY])

    def digest(self):
        """ Condense the month into a single string. """
        min_count = \
            min([len(self.songs), len(self.sonnets), len(self.proverbs)])
        components = ["\\chapter{"+self.name+"}"]
        for index in range(min_count):
            song_obj = \
                Article(
                    self.songs[index][ID_KEY],
                    fullness=self.fullness,
                    mods=self.mods
                )
            sonnet_obj = \
                Article(
                    self.sonnets[index][ID_KEY],
                    fullness=self.fullness,
                    mods=self.mods
                )
            proverb_obj = \
                Article(
                    self.proverbs[index][ID_KEY],
                    fullness=self.fullness,
                    mods=self.mods
                )
            components.append("\\section{}")
            components.append("\\subsection{}")
            components.append(song_obj.digest())
            components.append("\\subsection{}")
            components.append(sonnet_obj.digest())
            components.append("\\subsection{}")
            components.append(proverb_obj.digest())
        result = self.SECTION_SEPARATOR.join(components)
        return result

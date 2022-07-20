"""
This code defines a class which builds the contents of a given month.
"""

# Standard imports.
import sqlite3

# Local imports.
import configs
from article import Article
from monthly_selects import DEFAULT_SELECTS

# Local constants.
DEFAULT_PATH_TO_DEMO_OUTPUT = "month_builder_demo_output.tex"

##############
# MAIN CLASS #
##############

class MonthBuilder:
    """ The class in question. """
    def __init__(
            self, name, selects=DEFAULT_SELECTS, fullness="full", mods=None
        ):
        self.name = name
        self.selects = selects
        self.fullness = fullness
        self.mods = mods
        self.songs = fetch_articles(selects[self.name]["songs"])
        self.sonnets = fetch_articles(selects[self.name]["sonnets"])
        self.proverbs = fetch_articles(selects[self.name]["proverbs"])

    def digest(self):
        """ Condense the month into a single string. """
        min_count = \
            min([len(self.songs), len(self.sonnets), len(self.proverbs)])
        result = "\\chapter{"+self.name+"}\n\n"
        for index in range(min_count):
            song_obj = \
                Article(
                    self.songs[index],
                    fullness=self.fullness,
                    mods=self.mods
                )
            sonnet_obj = \
                Article(
                    self.sonnets[index],
                    fullness=self.fullness,
                    mods=self.mods
                )
            proverb_obj = \
                Article(
                    self.proverbs[index],
                    fullness=self.fullness,
                    mods=self.mods
                )
            song = song_obj.digest()
            sonnet = sonnet_obj.digest()
            proverb = proverb_obj.digest()
            result = (
                result+
                "\\bigskip\n\\bigskip\n\\section{}\n\n"+
                "\\subsection{}\n\n"+song+"\n\n"+
                "\\subsection{}\n\n"+sonnet+"\n\n"+
                "\\subsection{}\n\n"+proverb+"\n\n"
            )
        return result

####################
# HELPER FUNCTIONS #
####################

def fetch_articles(select, path_to_db=configs.PATH_TO_DB):
    """ Extract a list of article IDs from a select statement. """
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute(select)
    extract = cursor.fetchall()
    connection.close()
    result = []
    for item in extract:
        result.append(item[0])
    return result

###########
# TESTING #
###########

def demo(path_to_demo_output=DEFAULT_PATH_TO_DEMO_OUTPUT,
         month_to_demo="Primilis"):
    """ Run a demonstration. """
    month_builder = MonthBuilder(month_to_demo)
    digest = month_builder.digest()
    with open(path_to_demo_output, "w") as output_file:
        output_file.write(digest)
    print("Demo output saved to "+path_to_demo_output)

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    demo()

if __name__ == "__main__":
    run()

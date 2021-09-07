"""
This code defines a class which builds the LaTeX code for the Almanack's
various months.
"""

# Local imports.
import constants
from month_builder import MonthBuilder

# Local constants.
DEFAULT_PATH_TO_DEMO_OUTPUT = "year_builder_demo_output.tex"

##############
# MAIN CLASS #
##############

# The class in question.
class YearBuilder:
    """ The class in question. """
    def __init__(self, fullness="full", mods=None):
        self.fullness = fullness
        self.mods = mods
        self.months = self.get_months()

    def buid_months(self):
        """ Fill the month fields. """
        result = dict()
        connection = sqlite3.connect(constants.db)
        cursor = connection.cursor()
        for month_name in constants.MONTH_NAMES:
            month_builder = MonthBuilder(
                                month_name, fullness=self.fullness,
                                mods=self.mods)
            result[month_name] = month_builder.digest()
        connection.close()

    def digest(self):
        """ Wrap all months into one string. """
        result = ""
        for month_name in constants.MONTH_NAMES:
            result = result+self.months[month_name]
        return result

###########
# TESTING #
###########

def demo(path_to_demo_output=DEFAULT_PATH_TO_DEMO_OUTPUT):
    """ Run a demonstration. """
    year_builder = YearBuilder()
    digest = year_builder.digest()
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

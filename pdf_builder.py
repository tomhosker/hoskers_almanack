"""
This code defines a class which builds almanack.pdf.
"""

# Standard imports.
import os
import sqlite3

# Local imports.
import constants, almanack_utils
from month_builder import MonthBuilder
from bib_builder import build_bib

##############
# MAIN CLASS #
##############

class PDFBuilder:
    """ The class in question. """
    def __init__(self, fullness="full", mods=None, quiet=False):
        # Fullness determines how much front- and backmatter, etc is put in.
        self.fullness = fullness
        self.mods = mods
        self.quiet = quiet
        self.loadout = self.fetch_loadout()
        self.tween_syntax = self.fetch_tween_syntax()
        if(self.fullness == "full"):
            self.frontmatter = self.build_frontmatter()
        else:
            self.frontmatter = ""
        self.mainmatter = self.build_mainmatter()
        if(self.fullness in ["full", "slender"]):
            self.backmatter = self.build_backmatter()
        else:
            self.backmatter = ""

    def fetch_loadout(self):
        """ Fetch packages used from the database. """
        select = "SELECT latex FROM package_loadout WHERE name = \"main\";"
        rows = almanack_utils.fetch_to_dict(constants.db, select, tuple())
        result = rows[0]["latex"]
        return result

    def fetch_tween_syntax(self):
        """ Fetches the bits of LaTeX syntax which go between the lumps of
        content. """
        conn = sqlite3.connect(constants.db)
        cursor = conn.cursor()
        select = "SELECT * FROM tween_syntax;"
        cursor.execute(select)
        rows = cursor.fetchall()
        result = dict()
        for row in rows:
            result[row[0]] = row[1]
        return result

    def build_frontmatter(self):
        """ Build the frontmatter from the database. """
        select = "SELECT * FROM frontmatter_chapters ORDER BY no;"
        rows = almanack_utils.fetch_to_dict(constants.db, select, tuple())
        result = ("\\listoffigures\n\n"+
                  "\\part{Introductory Material}\n\n")
        for row in rows:
            title = "\\chapter{"+row["name"]+"}"
            content = row["content"]
            result = result+title+"\n\n"+content
            if rows.index(row) != len(rows)-1:
                result = result+"\n\n"
        return result

    def build_mainmatter(self):
        """ Build the mainmatter from the "MonthBuilder" class. """
        month_builder = MonthBuilder(fullness=self.fullness, mods=self.mods)
        result = ("\\part{The \\textit{Almanack} Proper}\n\n"+
                  self.tween_syntax["pre_mainmatter"]+"\n\n")
        result = result+month_builder.digest()
        return result

    def build_backmatter(self):
        """ Build the backmatter from the database. """
        select = "SELECT * FROM backmatter_chapters ORDER BY no;"
        rows = almanack_utils.fetch_to_dict(constants.db, select, tuple())
        result = (self.tween_syntax["pre_backmatter"]+"\n\n"+
                  "\\part{Other Material}\n\n")
        for row in rows:
            title = "\\chapter{"+row["name"]+"}"
            content = row["content"]
            result = result+title+"\n\n"+content+"\n\n"
        result = (result+"\\printbibliography[title={Sources}]\n"+
                         "\\bigskip\n"+
                         "{\\footnotesize "+
                         self.tween_syntax["bibliography_note"]+"}\n\n")
        return result

    def build_tex(self):
        """ This is where the magic happens. """
        tex =  ("\\documentclass{amsbook}\n"+
                "\\title{Hosker's Almanack ("+constants.version+")}\n\n"+
                self.loadout+"\n\n"+
                self.tween_syntax["in_preamble"]+"\n\n"+
                "\\begin{document}\n\n"+
                "\\frontmatter\n\n"+
                "\\maketitle\n"+
                "\\tableofcontents\n"+
                self.frontmatter+"\n\n"+
                "\\mainmatter\n\n"+
                self.mainmatter+"\n\n"+
                #"\\backmatter\n\n"+
                self.backmatter+"\n\n"+
                "\\end{document}")
        with open("main.tex", "w") as fileobj:
            fileobj.write(tex)

    def build_pdf(self):
        """ Runs XeLaTeX on "main.tex" and BibTex on "main.aux" in order to
        build our PDF, "main.pdf". """
        commands = ("xelatex main.tex",
                    "bibtex main.aux",
                    "xelatex main.tex",
                    "mv main.pdf almanack.pdf")
        try:
            for command in commands:
                if self.quiet:
                    os.system(command+" >/dev/null")
                else:
                    os.system(command)
        except:
            print("Run build_tex() first!")
        os.system("rm -rf main*")
        os.system("rm sources.bib")

    def build(self):
        """ Build everything. """
        print("Building bibliography...")
        build_bib()
        print("Building .tex file...")
        self.build_tex()
        print("Building PDF...")
        self.build_pdf()
        print("PDF built!")

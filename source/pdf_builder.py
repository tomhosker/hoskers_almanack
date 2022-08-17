"""
This code defines a class which builds almanack.pdf.
"""

# Standard imports.
import os
import subprocess
from pathlib import Path

# Local imports.
if __package__:
    from . import configs
else:
    import configs
from .almanack_utils import fetch_to_dict
from .encapsulator import get_loadout
from .month_builder import MonthBuilder
from .bib_builder import build_bib

##############
# MAIN CLASS #
##############

class PDFBuilder:
    """ The class in question. """
    def __init__(
            self,
            path_to_output="almanack.pdf",
            fullness="full",
            mods=None,
            version="MAIN",
            quiet=False
        ):
        self.path_to_output = path_to_output
        # Fullness determines how much front- and backmatter, etc is put in.
        self.fullness = fullness
        self.mods = mods
        self.version = version
        self.quiet = quiet
        self.loadout = get_loadout("main")
        if self.fullness == "full":
            self.frontmatter = self.build_frontmatter()
        else:
            self.frontmatter = ""
        self.mainmatter = self.build_mainmatter()
        if self.fullness in ["full", "slender"]:
            self.backmatter = self.build_backmatter()
        else:
            self.backmatter = ""

    def build_frontmatter(self):
        """ Build the frontmatter from the database. """
        result = ""
        select = "SELECT * FROM frontmatter_chapters ORDER BY no;"
        rows = fetch_to_dict(select, tuple())
        for row in rows:
            title = "\\chapter{"+row["name"]+"}"
            content = row["content"]
            result = result+title+"\n\n"+content
            if rows.index(row) != len(rows)-1:
                result = result+"\n\n"
        return result

    def build_mainmatter(self):
        """ Build the mainmatter from the "MonthBuilder" class. """
        result = ""
        for month_name in configs.MONTH_NAMES:
            month_builder = \
                MonthBuilder(month_name, fullness=self.fullness, mods=self.mods)
            result = result+month_builder.digest()
        return result

    def build_backmatter(self):
        """ Build the backmatter from the database. """
        result = ""
        select = "SELECT * FROM backmatter_chapters ORDER BY no;"
        rows = fetch_to_dict(select, tuple())
        for row in rows:
            title = "\\chapter{"+row["name"]+"}"
            content = row["content"]
            result = result+title+"\n\n"+content+"\n\n"
        return result

    def build_tex(self):
        """ This is where the magic happens. """
        path_to_base = str(Path(__file__).parent/"base.tex")
        with open(path_to_base, "r") as base_file:
            tex = base_file.read()
        tex = tex.replace("#VERSION_STRING", self.version)
        tex = tex.replace("#PACKAGE_LOADOUT", self.loadout)
        tex = tex.replace("#FRONTMATTER", self.frontmatter)
        tex = tex.replace("#MAINMATTER", self.mainmatter)
        tex = tex.replace("#BACKMATTER", self.backmatter)
        with open("main.tex", "w") as fileobj:
            fileobj.write(tex)

    def build_pdf(self):
        """ Runs XeLaTeX on "main.tex" and BibTex on "main.aux" in order to
        build our PDF, "main.pdf". """
        commands = (
            ["xelatex", "main.tex"],
            ["bibtex", "main.aux"],
            ["xelatex", "main.tex"],
        )
        for command in commands:
            if self.quiet:
                subprocess.run(command, stdout=subprocess.DEVNULL, check=True)
            else:
                subprocess.run(command, check=True)
        os.rename("main.pdf", self.path_to_output)

    def build(self):
        """ Build everything. """
        purge_main()
        print("Building bibliography...")
        build_bib()
        print("Building .tex file...")
        self.build_tex()
        print("Building PDF...")
        self.build_pdf()
        purge_main()
        os.remove(configs.PATH_TO_BIB)
        print("PDF built!")

####################
# HELPER FUNCTIONS #
####################

def purge_main():
    """ Purge all the "main" files. """
    purge_stem("main")
    try:
        os.remove("main-blx.bib")
    except FileNotFoundError:
        pass

def purge_stem(stem):
    """ Remove all the files beginning with a given stem. """
    for path_obj in Path.cwd().glob(stem+".*"):
        os.remove(str(path_obj))

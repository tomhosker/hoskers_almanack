"""
This code defines a class which builds almanack.pdf.
"""

# Standard imports.
import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar

# Local imports.
from .almanack_utils import fetch_to_dict
from .configs import (
    OUTPUT_FN,
    FULLNESS,
    FULL,
    SLENDER,
    MODS,
    VERSION,
    LOADOUT_ID,
    NAME_KEY,
    CONTENT_KEY,
    MONTH_NAMES,
    PATH_OBJ_TO_TEX,
    PATH_TO_BIB,
    BASE_TEX,
    MAIN_STEM,
    MAIN_BLX,
    MAIN_TEX,
    MAIN_AUX,
    MAIN_PDF
)
from .encapsulator import get_loadout
from .month_builder import MonthBuilder
from .bib_builder import build_bib

##############
# MAIN CLASS #
##############

@dataclass
class PDFBuilder:
    """ The class in question. """
    # Class attributes.
    CHAPTER_SEPARATOR: ClassVar[str] = "\n\n"
    VERSION_MARKER: ClassVar[str] = "#VERSION_STRING"
    LOADOUT_MARKER: ClassVar[str] = "#PACKAGE_LOADOUT"
    FRONTMATTER_MARKER: ClassVar[str] = "#FRONTMATTER"
    MAINMATTER_MARKER: ClassVar[str] = "#MAINMATTER"
    BACKMATTER_MARKER: ClassVar[str] = "#BACKMATTER"
    LATEX_COMMAND: ClassVar[str] = "xelatex"
    BIBTEX_COMMAND: ClassVar[str] = "bibtex"

    # Instance attributes.
    path_to_output: str = OUTPUT_FN
    fullness: str = FULLNESS # Determines volume of notes, backmatter, etc.
    mods: tuple = MODS
    version: str = VERSION
    quiet: bool = False
    loadout_id: str = LOADOUT_ID
    loadout: str = None
    frontmatter: str = None
    mainmatter: str = None
    backmatter: str = None

    def __post_init__(self):
        self.loadout = get_loadout(self.loadout_id)
        if self.fullness == FULL:
            self.frontmatter = self.build_frontmatter()
        self.mainmatter = self.build_mainmatter()
        if self.fullness in (FULL, SLENDER):
            self.backmatter = self.build_backmatter()

    def build_frontmatter(self):
        """ Build the frontmatter from the database. """
        chapters = []
        select = "SELECT * FROM frontmatter_chapters ORDER BY no;"
        rows = fetch_to_dict(select, tuple())
        for row in rows:
            title = "\\chapter{"+row[NAME_KEY]+"}"
            content = row[CONTENT_KEY]
            chapter = title+"\n\n"+content
            chapters.append(chapter)
        result = self.CHAPTER_SEPARATOR.join(chapters)
        return result

    def build_mainmatter(self):
        """ Build the mainmatter from the "MonthBuilder" class. """
        chapters = []
        for month_name in MONTH_NAMES:
            month_builder = \
                MonthBuilder(month_name, fullness=self.fullness, mods=self.mods)
            chapters.append(month_builder.digest())
        result = self.CHAPTER_SEPARATOR.join(chapters)
        return result

    def build_backmatter(self):
        """ Build the backmatter from the database. """
        chapters = []
        select = "SELECT * FROM backmatter_chapters ORDER BY no;"
        rows = fetch_to_dict(select, tuple())
        for row in rows:
            title = "\\chapter{"+row[NAME_KEY]+"}"
            content = row[CONTENT_KEY]
            chapter = title+"\n\n"+content
            chapters.append(chapter)
        result = self.CHAPTER_SEPARATOR.join(chapters)
        return result

    def build_tex(self):
        """ This is where the magic happens. """
        path_to_base = str(PATH_OBJ_TO_TEX/BASE_TEX)
        with open(path_to_base, "r") as base_file:
            tex = base_file.read()
        tex = tex.replace(self.VERSION_MARKER, self.version)
        tex = tex.replace(self.LOADOUT_MARKER, self.loadout)
        tex = tex.replace(self.FRONTMATTER_MARKER, self.frontmatter)
        tex = tex.replace(self.MAINMATTER_MARKER, self.mainmatter)
        tex = tex.replace(self.BACKMATTER_MARKER, self.backmatter)
        with open(MAIN_TEX, "w") as fileobj:
            fileobj.write(tex)

    def build_pdf(self):
        """ Run XeLaTeX on "main.tex" and BibTex on "main.aux" in order to
        build our PDF, "main.pdf". """
        commands = (
            (self.LATEX_COMMAND, MAIN_TEX),
            (self.BIBTEX_COMMAND, MAIN_AUX),
            (self.LATEX_COMMAND, MAIN_TEX)
        )
        for command in commands:
            if self.quiet:
                subprocess.run(command, stdout=subprocess.DEVNULL, check=True)
            else:
                subprocess.run(command, check=True)
        Path(MAIN_PDF).rename(self.path_to_output)

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
        purge_generated(PATH_TO_BIB)
        print("PDF built!")

####################
# HELPER FUNCTIONS #
####################

def purge_main():
    """ Purge all the "main" files. """
    purge_stem(MAIN_STEM)
    purge_generated(MAIN_BLX)

def purge_generated(path_to):
    """ Remove a given generated file, if it exists. """
    path_obj = Path(path_to)
    path_obj.unlink(missing_ok=True)

def purge_stem(stem):
    """ Remove all the files beginning with a given stem. """
    for path_obj in Path.cwd().glob(stem+".*"):
        path_obj.unlink(missing_ok=True)

def build_pdf(**kwargs):
    """ An entry point function. """
    pdf_builder = PDFBuilder(**kwargs)
    pdf_builder.build()

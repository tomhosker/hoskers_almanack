"""
This code defines a class which builds almanack.pdf.
"""

# Standard imports.
from dataclasses import dataclass
from pathlib import Path

# Local imports.
from .almanack_utils import (
    fetch_to_dict,
    get_loadout,
    compile_latex,
    run_bibtex,
)
from .configs import (
    MODS,
    VERSION,
    LOADOUT_ID,
    FULLNESS,
    CHAPTER_SEPARATOR,
    MONTH_NAMES
)
from .constants import (
    Filenames,
    Fullnesses,
    ColumnNames,
    Paths,
    Markers,
    MAIN_STEM
)
from .month_builder import MonthBuilder
from .bib_builder import build_bib

##############
# MAIN CLASS #
##############

@dataclass
class PDFBuilder:
    """ The class in question. """
    path_to_output: str = Filenames.OUTPUT_FN.value
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
        if self.fullness == Fullnesses.FULL:
            self.frontmatter = self.build_frontmatter()
        if self.fullness in (Fullnesses.FULL, Fullnesses.SLENDER):
            self.backmatter = self.build_backmatter()
        self.mainmatter = self.build_mainmatter() # This should be last.

    def build_frontmatter(self):
        """ Build the frontmatter from the database. """
        chapters = ["\\part{Introductory Material}"]
        select = "SELECT * FROM FrontmatterChapter ORDER BY num;"
        rows = fetch_to_dict(select, tuple())
        for row in rows:
            title = "\\chapter{"+row["name"]+"}"
            content = row[ColumnNames.CONTENT.value]
            chapter = title+"\n\n"+content
            chapters.append(chapter)
        result = CHAPTER_SEPARATOR.join(chapters)
        return result

    def build_mainmatter(self):
        """ Build the mainmatter from the "MonthBuilder" class. """
        chapters = []
        if self.frontmatter or self.backmatter:
            chapters.append("\\part{The \\textit{Almanack} Proper}")
        for month_name in MONTH_NAMES:
            month_builder = \
                MonthBuilder(month_name, fullness=self.fullness, mods=self.mods)
            chapters.append(month_builder.digest())
        result = CHAPTER_SEPARATOR.join(chapters)
        return result

    def build_backmatter(self):
        """ Build the backmatter from the database. """
        chapters = ["\\part{Supplementary Material}"]
        select = "SELECT * FROM BackmatterChapter ORDER BY num;"
        rows = fetch_to_dict(select)
        for row in rows:
            title = "\\chapter{"+row["name"]+"}"
            content = row[ColumnNames.CONTENT.value]
            chapter = title+"\n\n"+content
            chapters.append(chapter)
        result = CHAPTER_SEPARATOR.join(chapters)
        return result

    def build_tex(self):
        """ This is where the magic happens. """
        with open(Paths.PATH_TO_BASE.value, "r") as base_file:
            tex = base_file.read()
        tex = tex.replace(Markers.VERSION.value, self.version)
        tex = tex.replace(Markers.LOADOUT.value, self.loadout)
        tex = tex.replace(Markers.FRONTMATTER.value, self.frontmatter)
        tex = tex.replace(Markers.MAINMATTER.value, self.mainmatter)
        tex = tex.replace(Markers.BACKMATTER.value, self.backmatter)
        with open(Filenames.MAIN_TEX.value, "w") as fileobj:
            fileobj.write(tex)

    def build_pdf(self):
        """ Run XeLaTeX on "main.tex" and BibTex on "main.aux" in order to
        build our PDF, "main.pdf". """
        if (
            (not compile_latex(Filenames.MAIN_TEX.value, quiet=self.quiet)) or
            (not run_bibtex(Filenames.MAIN_AUX.value, quiet=self.quiet)) or
            (not compile_latex(Filenames.MAIN_TEX.value, quiet=self.quiet))
        ):
            return False
        Path(Filenames.MAIN_PDF.value).rename(self.path_to_output)
        return True

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
        purge_generated(Paths.PATH_TO_BIB.value)
        print("PDF built!")

####################
# HELPER FUNCTIONS #
####################

def purge_main():
    """ Purge all the "main" files. """
    purge_stem(MAIN_STEM)
    purge_generated(Filenames.MAIN_BLX.value)

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

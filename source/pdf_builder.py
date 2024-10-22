"""
This code defines a class which builds almanack.pdf.
"""

# Standard imports.
from dataclasses import dataclass, field
from pathlib import Path

# Local imports.
from .utils import (
    get_loadout,
    compile_latex,
    run_bibtex,
    PATH_OBJ_TO_BACKMATTER,
    PATH_OBJ_TO_FRONTMATTER
)
from .configs import (
    MODS,
    VERSION,
    LOADOUT_ID,
    FULLNESS,
    CHAPTER_SEPARATOR,
    PUBLIC_MONTH_NAMES
)
from .constants import (
    Filenames,
    Fullnesses,
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
    clean: bool = True
    title_page: str = field(init=False, default=None)
    frontmatter: str = field(init=False, default=None)
    mainmatter: str = field(init=False, default=None)
    backmatter: str = field(init=False, default=None)

    def __post_init__(self):
        self.loadout = get_loadout(self.loadout_id)
        if self.fullness == Fullnesses.FULL:
            self.title_page = self.get_title_page()
            self.frontmatter = self.build_frontmatter()
        else:
            self.title_page = ""
            self.frontmatter = ""
        if self.fullness in (Fullnesses.FULL, Fullnesses.SLENDER):
            self.backmatter = self.build_backmatter()
        else:
            self.backmatter = ""
        self.mainmatter = self.build_mainmatter() # This should be last.

    def get_title_page(self) -> str:
        """ Ronseal. """
        items = [
            "\\frontmatter",
            fetch_frontmatter_chapter("title_page")
        ]
        result = CHAPTER_SEPARATOR.join(items)
        return result

    def build_frontmatter(self) -> str:
        """ Build the frontmatter from the files. """
        return ""

    def build_mainmatter(self) -> str:
        """ Build the mainmatter from the "MonthBuilder" class. """
        chapters = []
        if self.frontmatter or self.backmatter:
            chapters.append("\\part{The \\textit{Almanack} Proper}")
        for index, month_name in enumerate(PUBLIC_MONTH_NAMES):
            month_builder = \
                MonthBuilder(
                    index+1,
                    month_name,
                    fullness=self.fullness,
                    mods=self.mods
                )
            chapters.append(month_builder.digest())
        result = CHAPTER_SEPARATOR.join(chapters)
        return result

    def build_backmatter(self) -> str:
        """ Build the backmatter from the database. """
        chapters = [
            "\\part{Supplementary Material}",
            fetch_backmatter_chapter("ecclesiastes"),
            fetch_backmatter_chapter("song_of_solomon"),
            fetch_backmatter_chapter("principles")
        ]
        result = CHAPTER_SEPARATOR.join(chapters)
        return result

    def build_tex(self):
        """ This is where the magic happens. """
        with open(Paths.PATH_TO_BASE.value, "r") as base_file:
            tex = base_file.read()
        pairs = (
            (Markers.LOADOUT.value, self.loadout),
            (Markers.TITLE_PAGE.value, self.title_page),
            (Markers.FRONTMATTER.value, self.frontmatter),
            (Markers.MAINMATTER.value, self.mainmatter),
            (Markers.BACKMATTER.value, self.backmatter),
            (Markers.VERSION.value, self.version)
        )
        for pair in pairs:
            tex = tex.replace(*pair)
        with open(Filenames.MAIN_TEX.value, "w") as fileobj:
            fileobj.write(tex)

    def build_pdf(self) -> bool:
        """ Run XeLaTeX on "main.tex" and BibTex on "main.aux" in order to
        build our PDF, "main.pdf". """
        if (
            (not compile_latex(Filenames.MAIN_TEX.value, quiet=self.quiet)) or
            (not run_bibtex(Filenames.MAIN_AUX.value, quiet=self.quiet)) or
            (not compile_latex(Filenames.MAIN_TEX.value, quiet=self.quiet))
        ):
            return False
        path_obj_to_pdf = Path(Filenames.MAIN_PDF.value)
        if path_obj_to_pdf.exists(): # The if-statement is for testing purposes.
            path_obj_to_pdf.rename(self.path_to_output)
        return True

    def clean_up(self):
        """ Ronseal. """
        purge_main()
        purge_generated(Paths.PATH_TO_BIB.value)

    def build(self):
        """ Build everything. """
        purge_main()
        print("Building bibliography...")
        build_bib()
        print("Building .tex file...")
        self.build_tex()
        print("Building PDF...")
        self.build_pdf()
        if self.clean:
            print("Tidying up...")
            self.clean_up()
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

def purge_stem(stem: str):
    """ Remove all the files beginning with a given stem. """
    for path_obj in Path.cwd().glob(f"{stem}.*"):
        path_obj.unlink(missing_ok=True)

def build_pdf(**kwargs):
    """ An entry point function. """
    pdf_builder = PDFBuilder(**kwargs)
    pdf_builder.build()

def fetch_backmatter_chapter(code: str) -> str:
    """ Return the contents of the file as a string. """
    filename = f"{code}.tex"
    path_to_file = str(PATH_OBJ_TO_BACKMATTER/filename)
    with open(path_to_file, "r") as chapter_file:
        result = chapter_file.read()
    return result

def fetch_frontmatter_chapter(code: str) -> str:
    """ Return the contents of the file as a string. """
    filename = f"{code}.tex"
    path_to_file = str(PATH_OBJ_TO_FRONTMATTER/filename)
    with open(path_to_file, "r") as chapter_file:
        result = chapter_file.read()
    return result

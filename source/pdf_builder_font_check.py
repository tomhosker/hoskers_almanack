"""
This code defines a class which builds the font check PDF.
"""

# Standard imports.
from dataclasses import dataclass, field
from pathlib import Path

# Local imports.
from .article import Article
from .utils import (compile_latex, run_bibtex)
from .configs import (
    MODS,
    LOADOUT_ID,
    DEFAULT_FONT,
    PRINT_FONT
)
from .constants import (
    Filenames,
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
class PDFBuilderFontCheck:
    """ The class in question. """
    path_to_output: str = "font_check.pdf"
    mods: tuple = MODS
    quiet: bool = False
    loadout_id: str = LOADOUT_ID
    loadout: str = None
    clean: bool = True
    print_run: bool = False
    title: str = field(default=None, init=False)

    def __post_init__(self):
        self.loadout = self.get_loadout()
        self.title = self.build_title()

    def get_loadout(self) -> str:
        """ Get the LaTeX for loading its various packages. """
        filename = f"{self.loadout_id}.tex"
        path_to_loadout = \
            str(Path(Paths.PATH_TO_PACKAGE_LOADOUTS.value)/filename)
        with open(path_to_loadout, "r") as loadout_file:
            result = loadout_file.read()
        main_font = DEFAULT_FONT
        if self.print_run:
            main_font = PRINT_FONT
        result = result.replace(Markers.MAIN_FONT.value, main_font)
        return result

    def build_title(self) -> str:
        """ Ronseal. """
        result = "Font Check"
        if self.print_run:
            result = f"{result} (Print Run)"
        return result

    def build_tex(self):
        """ This is where the magic happens. """
        with open(Paths.PATH_TO_BASE_FONT_CHECK.value, "r") as base_file:
            tex = base_file.read()
        pairs = (
            (Markers.LOADOUT.value, self.loadout),
            (Markers.TITLE.value, self.title),
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

def purge_generated(path_to: str):
    """ Remove a given generated file, if it exists. """
    path_obj = Path(path_to)
    path_obj.unlink(missing_ok=True)

def purge_stem(stem: str):
    """ Remove all the files beginning with a given stem. """
    for path_obj in Path.cwd().glob(f"{stem}.*"):
        path_obj.unlink(missing_ok=True)

def build_pdf_font_check(**kwargs):
    """ An entry point function. """
    pdf_builder = PDFBuilderFontCheck(**kwargs)
    pdf_builder.build()

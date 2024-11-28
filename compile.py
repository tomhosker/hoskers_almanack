"""
This script can compile (1) the almanack PDF, or (2) the PDF form of a given
article, or (3) a font check PDF.
"""

# Standard imports.
import argparse

# Local imports.
from source import build_pdf, build_pdf_article, build_pdf_font_check

###################
# RUN AND WRAP UP #
###################

def make_parser():
    """ Return a parser argument. """
    result = \
        argparse.ArgumentParser(
            description="Compile an article from the database"
        )
    result.add_argument(
        "--article-id",
        dest="article_id",
        help="The key identifying the article to be compiled"
    )
    result.add_argument(
        "--font-check",
        action="store_true",
        default=False,
        dest="font_check",
        help="Indicate whether to compile a font check PDF"
    )
    result.add_argument(
        "--preserve-tex-files",
        action="store_true",
        default=False,
        dest="preserve_tex_files",
        help="Preserve the .tex files used to build the PDFs"
    )
    result.add_argument(
        "--print-run",
        action="store_true",
        default=False,
        dest="print_run",
        help="Ensure a printer-friendly font is used"
    )
    return result

def run():
    """ Run this file. """
    parser = make_parser()
    arguments = parser.parse_args()
    if arguments.article_id:
        build_pdf_article(
            article_id=arguments.article_id,
            clean=(not arguments.preserve_tex_files),
            print_run=arguments.print_run
        )
    elif arguments.font_check:
        build_pdf_font_check(
            clean=(not arguments.preserve_tex_files),
            print_run=arguments.print_run
        )
    else:
        build_pdf(
            clean=(not arguments.preserve_tex_files),
            print_run=arguments.print_run
        )

if __name__ == "__main__":
    run()

"""
This code tests the PDFBuilder class.
"""

# Standard imports.
from unittest.mock import Mock, patch

# Source imports.
from source.pdf_builder import PDFBuilder

###########
# TESTING #
###########

@patch("source.pdf_builder.compile_latex", Mock())
@patch("source.pdf_builder.run_bibtex", Mock())
@patch("source.pdf_builder.build_bib", Mock())
def test_pdf_builder():
    """ Test that we can create a PDFBuilder object, and that its methods behave
    as expected. """
    pdf_builder = PDFBuilder()
    pdf_builder.build()

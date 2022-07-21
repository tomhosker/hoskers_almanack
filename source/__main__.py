"""
This code provides a concise entry-point for the using the PDFBuilder class.
"""

# Local imports.
if __package__:
    from . import configs
else:
    import configs
from .pdf_builder import PDFBuilder

###################
# RUN AND WRAP UP #
###################

def run():
    builder = \
        PDFBuilder(
            path_to_output=configs.PATH_TO_OUTPUT,
            fullness=configs.FULLNESS,
            mods=configs.MODS,
            version=configs.VERSION
        )
    builder.build()

if __name__ == "__main__":
    run()

"""
This code checks the correctness of the HPML in the database.
"""

# Standard imports.
import json
import traceback
from pathlib import Path

# Non-standard imports.
from progressbar import progressbar

# Local imports.
from .check_encapsulator import CheckEncapsulator
from .check_utils import check_compile_latex, TEMP_TEX_FN
from .constants import ColumnNames
from .utils import fetch_to_dict

# Local constants.
PATH_TO_LOG = str(Path.home()/"validate_hpml_failures.json")

####################
# HELPER FUNCTIONS #
####################

def check_hpml_in_article(data, quiet=False):
    """ Check the HPML in a given article. """
    encapsulator = \
        CheckEncapsulator(
            data[ColumnNames.CONTENT.value],
            is_prose_poem=bool(data[ColumnNames.IS_PROSE_POEM.value]),
            title=str(data[ColumnNames.ID.value])
        )
    latex = encapsulator.digest()
    with open(TEMP_TEX_FN, "w") as temp_tex_file:
        temp_tex_file.write(latex)
    check_compile_latex(TEMP_TEX_FN, quiet=quiet)

def clean_files():
    """ Remove any temporary and generated files. """
    for path_obj in Path.cwd().glob("temp.*"):
        path_obj.unlink()

##############
# VALIDATION #
##############

def validate_hpml_in_article(article_id, clean=False):
    """ Check the correctness of the HPML is a SPECIFIC article. """
    result = True
    try:
        extract = \
            fetch_to_dict("SELECT * FROM Article WHERE id = ?;", (article_id,))
        data = extract[0]
        check_hpml_in_article(data, quiet=False)
    except:
        result = False
        traceback.print_exc()
    if clean:
        clean_files()
    if result:
        print("SUCCESS: Validated HPML in article with ID "+str(article_id))
    else:
        print(
            "FAIL: Unable to validate HPML in article with ID "+
            str(article_id)
        )
    return result

def validate_all_hpml(clean=True):
    """ Check the correctness of ALL the HPML in the database. """
    articles = fetch_to_dict("SELECT * FROM Article WHERE type != 3;")
    failures = []
    print("Attempting to compile each article...")
    for article in progressbar(articles):
        try:
            check_hpml_in_article(article, quiet=True)
        except:
            failures.append({
                "id": article[ColumnNames.ID.value],
                "exception": traceback.format_exc()
            })
            print(
                "\nException while processing article width ID: "+
                str(article[ColumnNames.ID.value])
            )
            traceback.print_exc()
    if clean:
        clean_files()
    if failures:
        with open(PATH_TO_LOG, "w") as log_file:
            log_file.write(json.dumps(failures))
        print("FAIL")
        print("Failures log written to: "+PATH_TO_LOG)
        return False
    return True

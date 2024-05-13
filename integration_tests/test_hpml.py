"""
This code checks the correctness of all the HPML in the database.
"""

# Standard imports.
import json
import traceback
from pathlib import Path

# Non-standard imports.
from progressbar import progressbar

# Local imports.
from .check_encapsulator import CheckEncapsulator
from .utils import fetch_to_dict, compile_latex

# Local constants.
TEMP_TEX_FN = "temp.tex"
TEMP_PDF_FN = "temp.pdf"
PATH_TO_LOG = str(Path.home()/"test_hpml_failures.json")

# This one's CRAAAAAAAAAZY! (If in doubt, set to None.)
SPECIFIC_ID = 1396

####################
# HELPER FUNCTIONS #
####################

def check_hpml_in_article(data):
    """ Check the HPML in a given article. """
    encapsulator = \
        CheckEncapsulator(
            data["content"],
            is_prose_poem=bool(data["is_prose_poem"])
        )
    latex = encapsulator.digest()
    with open(TEMP_TEX_FN, "w") as temp_tex_file:
        temp_tex_file.write(latex)
    compile_latex(TEMP_TEX_FN, quiet=True)

###########
# TESTING #
###########

def test_hpml_in_specific_article(article_id):
    """ Ronseal. """
    extract = \
        fetch_to_dict("SELECT * FROM Article WHERE id = ?;", (article_id,))
    data = extract[0]
    check_hpml_in_article(data)

def test_hpml():
    """ Run the test in question. """
    if SPECIFIC_ID:
        test_hpml_in_specific_article(SPECIFIC_ID)
        return True
    articles = fetch_to_dict("SELECT * FROM Article WHERE type != 3;")
    failures = []
    print("Attempting to compile each article...")
    for article in progressbar(articles):
        try:
            check_hpml_in_article(article)
        except:
            failures.append({
                "id": article["id"],
                "exception": traceback.format_exc()
            })
            print(
                "\nException while processing article width ID: "+
                str(article["id"])
            )
            traceback.print_exc()
    for path_obj in Path.cwd().glob("temp.*"):
        path_obj.unlink()
    if failures:
        with open(PATH_TO_LOG, "w") as log_file:
            log_file.write(json.dumps(failures))
        print("FAIL")
        print("Failures log written to: "+PATH_TO_LOG)
        return False
    return True

"""
This code tests the functions in the utils module.
"""

# Source imports.
from source.utils import fetch_to_dict

###########
# TESTING #
###########

def test_fetch_to_dict():
    """ Test that the function returns the correct output. """
    select = "SELECT * FROM Article WHERE id = ?;"
    extract = fetch_to_dict(select, (1,))
    expected_opening = "Thou still unravished bride of quietness"
    assert extract[0]["content"].startswith(expected_opening)

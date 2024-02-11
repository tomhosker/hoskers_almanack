"""
This code tests the functions in the almanack_utils module.
"""

# Source imports.
from source.almanack_utils import fetch_to_dict, get_loadout

###########
# TESTING #
###########

def test_fetch_to_dict():
    """ Test that the function returns the correct output. """
    select = "SELECT * FROM Article WHERE id = ?;"
    extract = fetch_to_dict(select, (1,))
    expected_opening = "Thou still unravished bride of quietness"
    assert extract[0]["content"].startswith(expected_opening)

def test_get_loadout():
    """ Test that the function runs. """
    assert isinstance(get_loadout("main"), str)

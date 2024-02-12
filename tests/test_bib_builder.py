"""
This code tests the functions in the bib_builder module.
"""

# Source imports.
from source.article import fetch_to_dict
from source.bib_builder import (
    fetch_sources,
    none_to_empty,
    get_book_summary,
    build_bib
)

###########
# TESTING #
###########

def test_fetch_sources():
    """ Test that this function runs. """
    assert fetch_sources()

def test_none_to_empty():
    """ Test that this function returns the correct value. """
    assert none_to_empty(None) == ""
    assert none_to_empty(1) == "1"
    assert none_to_empty("one") == "one"

def test_get_book_summary():
    """ Test that this function returns the correct value. """
    extract = fetch_to_dict("SELECT * FROM Source WHERE code = ?;", ("kjv",))
    data = extract[0]
    actual_summary = get_book_summary(data)
    expected_summary = \
        "\n".join([
            "@book{kjv,",
            '    keywords = "source",',
            '    author = "",',
            '    title = "The Holy Bible, King James Version",',
            '    year = "1611",',
            '    editor = "",',
            '    translator = "",',
            "}"
        ])
    while actual_summary.endswith("\n"):
        actual_summary = actual_summary[:-1]
    assert actual_summary == expected_summary

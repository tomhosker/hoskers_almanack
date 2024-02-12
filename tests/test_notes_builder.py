"""
This code tests the NotesBuilder class.
"""

# Source imports.
from source.notes_builder import NotesBuilder

###########
# TESTING #
###########

def test_notes_builder():
    """ Test that we can create a NotesBuilder object, and that its methods
    behave as expected. """
    notes_builder = NotesBuilder(article_id=1)
    actual_notes = notes_builder.digest()
    expected_notes = \
        "`Ode on a Grecian Urn', John Keats (1795 -- 1821), \\cite{norton}."
    assert actual_notes == expected_notes

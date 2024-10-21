"""
This code tests the MonthBuilder class.
"""

# Source imports.
from source.month_builder import MonthBuilder

###########
# TESTING #
###########

def test_month_builder():
    """ Test that we can create a MonthBuilder object, and that its methods
    behave as expected. """
    month_builder = MonthBuilder(1, "Primilis")
    assert isinstance(month_builder.digest(), str)

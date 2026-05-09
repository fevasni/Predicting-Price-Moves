"""
Basic tests for the financial news analysis project.
"""

import pytest


def test_basic():
    """A basic test to ensure pytest works."""
    assert True


def test_imports():
    """Test that basic imports work."""
    try:
        import pandas
        import numpy
        import matplotlib.pyplot
        import seaborn
        # Use the imports to avoid F401 errors
        df = pandas.DataFrame()
        arr = numpy.array([1, 2, 3])
        fig = matplotlib.pyplot.figure()
        seaborn.set_style("whitegrid")

        # Use variables to avoid F841 errors
        assert len(df) == 0
        assert arr.size == 3
        assert fig is not None
        assert True
    except ImportError:
        pytest.fail("Failed to import required packages")

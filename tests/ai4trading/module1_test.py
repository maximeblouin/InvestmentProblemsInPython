"""This module provides functions to test the solved problems."""
import pandas
from problems.ai4trading import module1


def test_solve_lesson_4_chapter_4():
    """Test function for solve_lesson4_chapter4."""
    output = module1.solve_lesson_4_chapter_4()

    expected_output = pandas.Series({
        "ABC": 160.677143,
        "EFG": 155.704286,
        "XYZ": 60.467143
    }).rename_axis("ticker")

    pandas.testing.assert_series_equal(output, expected_output)

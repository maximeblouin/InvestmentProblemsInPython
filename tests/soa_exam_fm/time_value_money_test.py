"""This module provides functions to test the solved problems."""
from math import isclose
from problems.soa_exam_fm import time_value_money


def test_solve_question_1():
    """Test function for solve_question1."""
    actual = round(time_value_money.solve_question_1(), 4)
    expected = 0.0396

    assert isclose(actual, expected, rel_tol=1e-4)

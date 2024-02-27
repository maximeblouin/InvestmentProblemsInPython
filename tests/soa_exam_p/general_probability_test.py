"""This module provides functions to test the solved problems."""
from math import isclose
from problems.soa_exam_p import general_probability


def test_solve_question_3():
    """Test function for solve_question1."""
    answer = general_probability.solve_question_3()
    expected = 0.6000

    assert isclose(answer, expected, rel_tol=1e-4)

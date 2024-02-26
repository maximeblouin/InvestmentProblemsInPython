"""This module provides functions to test the solved problems."""
from problems.cfa_foundation import chapter8


def test_solve_example_1():
    """Test function for solve_example1."""
    actual_apr1, actual_apr2, actual_apr3 = chapter8.solve_example_1()

    assert round(actual_apr1, 4) == round(0.1646, 4)
    assert round(actual_apr2, 4) == round(0.0243, 4)
    assert round(actual_apr3, 4) == round(0.0614, 4)


def test_solve_example_2():
    """Test function for solve_example2."""
    best_investment_1, best_investment_2 = chapter8.solve_example_2()

    assert best_investment_1 == {
        "future_payout": 1350,
        "years": 5,
        "discount_rate": 0.09,
        "present_value": 877.41}

    assert best_investment_2 == {
        "future_payout": 1350,
        "years": 5,
        "discount_rate": 0.15,
        "present_value": 877.41}

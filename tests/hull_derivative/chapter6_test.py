"""This module provides functions to test the solved problems."""
from datetime import datetime
from problems.hull_derivative import chapter6


def test_solve_question_1():
    """Test function for solve_question1."""
    interest_accrued1, interest_accrued2 = chapter6.solve_question_1()

    assert round(interest_accrued1, 4) == round(0.6087, 4)
    assert round(interest_accrued2, 4) == round(0.6028, 4)


def test_solve_question_2():
    """Test function for solve_question1."""
    cash_price = chapter6.solve_question_2()

    assert round(cash_price, 2) == round(103.69, 2)


def test_solve_question_3():
    """Test function for solve_question3."""
    total_gain_or_loss = chapter6.solve_question_3()

    assert round(total_gain_or_loss, 1) == round(300.0, 1)


def test_solve_question_4():
    """Test function for solve_question4."""
    zero_rate = chapter6.solve_question_4()

    assert round(zero_rate, 4) == round(3.0409, 4)


def test_solve_question_5():
    """Test function for solve_question5."""
    position, nb_contract = chapter6.solve_question_5()

    assert position == "shorted"
    assert round(nb_contract, 0) == 60


def test_solve_question_6():
    """Test function for solve_question6."""
    continuously_return = chapter6.solve_question_6()

    assert round(continuously_return, 4) == round(0.1027, 4)


def test_solve_question_7():
    """Test function for solve_question7."""
    cash_price = chapter6.solve_question_7()

    assert round(cash_price, 4) == round(113.7799, 4)


def test_solve_question_8():
    """Test function for solve_question8."""
    cheapest_bond = chapter6.solve_question_8()

    assert cheapest_bond == 4


def test_solve_question_9():
    """Test function for solve_question9."""
    future = chapter6.solve_question_9()

    assert future["current_date"] == datetime(2021, 7, 30, 0, 0)
    assert future["delivery_date"] == datetime(2021, 9, 30, 0, 0)
    assert future["quoted_price"] == 110
    assert round(future["coupon"], 2) == round(0.13, 2)
    assert round(future["conv_factor"], 2) == round(1.5, 2)
    assert round(future["cash_price"], 2) == round(116.32, 2)
    assert round(future["present_value"], 4) == round(6.4896, 4)
    assert round(future["cash_future_price"], 2) == round(112.03, 2)
    assert round(future["interest_bond"], 4) == round(2.0136, 4)
    assert round(future["adj_interest"], 2) == round(110.01, 2)
    assert round(future["quoted_future_price"], 2) == round(73.34, 2)

"""Learning Objective 1: Time Value of Money."""
import numpy_financial as npf
import numpy as np


def solve_question_1():
    r"""
    Solve question 1.

    Bruce deposits 100 into a bank account. His account is credited interest
    at an annual nominal rate of interest of 4% convertible semiannually.
    At the same time, Peter deposits 100 into a separate account. Peter's
    account is credited interest at an annual force of interest of δ.
    After 7.25 years, the value of each account is the same.
    Calculate δ.
    """
    # Given data
    bruce = {
        "principal": 100,  # Principal for Bruce
        "annual_interest_rate": 0.04,  # Annual nominal interest rate for Bruce
        "compounding_frequency": 2,  # Compounded semiannually for Bruce
        "time_years": 7.25,  # Time in years
    }

    # Calculate the future value of Bruce's account
    bruce["account"] = npf.fv(
        rate=bruce["annual_interest_rate"] / bruce["compounding_frequency"],
        nper=bruce["compounding_frequency"] * bruce["time_years"],
        pmt=0,
        pv=-bruce["principal"],
    )

    delta = np.log(bruce["account"] / bruce["principal"]) / bruce["time_years"]

    return delta

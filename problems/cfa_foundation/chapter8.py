"""Chapter 8 - Quantitative Concepts."""


def solve_example_1():
    """
    Solve example 1.

    - A credit card charges interest at an APR of 15.24%, compounded daily.
    - A bank pays 0.2% monthly on the average amount on deposit over the month.
    - A loan is made with a 6.0% annual rate, compounded quarterly.

    Calculate EAR.
    """
    # Credit card which charges interest at an APR of 15.24%, compounded daily.
    apr = 0.1524
    periods = 365
    expected_apr1 = (1 + (apr / periods)) ** periods - 1

    # Bank pays 0.2% monthly on the average amount on deposit over the month.
    apr = 0.002 * 12
    periods = 12
    expected_apr2 = (1 + (apr / periods)) ** periods - 1

    # Loan made with a 6.0% annual rate, compounded quarterly.
    apr = 0.06
    periods = 4
    expected_apr3 = (1 + (apr / periods)) ** periods - 1

    return expected_apr1, expected_apr2, expected_apr3


def solve_example_2():
    """
    Solve example 2.

    Part 1:
    You are choosing between two investments of equal risk. You believe that
    given the risk, the appropriate discount rate to use is 9%. Your initial
    investment (outflow) for each is £500. One investment is expected to pay
    out £1,000 three years from now; the other investment is expected to pay
    out £1,350 five years from now. To choose between the two investments,
    you must compare the value of each investment at the same point in time.

    Part 2:
    You are choosing between the same two investments, but you have reassessed
    their risks. You now consider the five-year investment to be more risky
    than the first and estimate that a 15% return is required to justify making
    this investment.
    """
    investments_1 = [
        {
            # Present value of £1,000 in three years discounted at 9%
            "future_payout": 1000,
            "years": 3,
            "discount_rate": 0.09,
            "present_value": round(1000 / (1 + 0.09) ** 3, 2)
        },
        {
            # Present value of £1,350 in five years discounted at 9%
            "future_payout": 1350,
            "years": 5,
            "discount_rate": 0.09,
            "present_value": round(1350 / (1 + 0.09) ** 5, 2)
        },
    ]

    # Find the investment with the highest present value
    best_investment_1 = max(investments_1, key=lambda x: x["present_value"])

    investments_2 = [
        {
            # Present value of £1,000 in three years discounted at 9%
            "future_payout": 1000,
            "years": 3,
            "discount_rate": 0.09,
            "present_value": round(1000 / (1 + 0.09) ** 3, 2)
        },
        {
            # Present value of £1,350 in five years discounted at 9%
            "future_payout": 1350,
            "years": 5,
            "discount_rate": 0.15,
            "present_value": round(1350 / (1 + 0.09) ** 5, 2)
        },
    ]

    # Find the investment with the highest present value
    best_investment_2 = max(investments_2, key=lambda x: x["present_value"])

    return best_investment_1, best_investment_2

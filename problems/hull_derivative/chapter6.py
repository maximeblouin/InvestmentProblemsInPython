"""Chapter 6 - Interest Rate Futures."""
from datetime import datetime
import math
import QuantLib
import pandas as pd


def solve_question_1():
    """
    Solve question 1.

    A U.S. Treasury bond pays a 7% coupon on January 7 and July 7. How much
    interest accrues per $100 of principal to the bondholder between July 7,
    2017, and August 8, 2017?
    How would your answer be different if it were a corporate bond?
    """
    settlement_date = datetime(2017, 8, 8)
    issue_date = datetime(2017, 7, 7)
    maturity_date = datetime(2018, 1, 7)
    face_value = 100.0
    coupon_rate = 7.0

    # Convert settlement_date, issue_date, and maturity_date to QuantLib.Date
    settlement_date = QuantLib.Date(
        settlement_date.day, settlement_date.month, settlement_date.year
    )
    issue_date = QuantLib.Date(
        issue_date.day, issue_date.month, issue_date.year)
    maturity_date = QuantLib.Date(
        maturity_date.day, maturity_date.month, maturity_date.year
    )

    # Create a calendar and day-count convention based on the settlement date
    calendar = QuantLib.UnitedStates(QuantLib.UnitedStates.Settlement)

    day_count = QuantLib.ActualActual(QuantLib.UnitedStates.Settlement)

    # Set up the bond schedule
    tenor = QuantLib.Period(QuantLib.Semiannual)

    schedule = QuantLib.Schedule(
        issue_date,
        maturity_date,
        tenor,
        calendar,
        QuantLib.Unadjusted,
        QuantLib.Unadjusted,
        QuantLib.DateGeneration.Backward,
        False,
    )

    # Create the bond with settlement days set to 0
    coupons = [coupon_rate / 100]

    bond = QuantLib.FixedRateBond(0, face_value, schedule, coupons, day_count)

    # Return the accrued interest as a percentage of the face value
    accrued_amount = QuantLib.BondFunctions.accruedAmount(
        bond, settlement_date)

    interest_accrued1 = accrued_amount / face_value * 100

    settlement_date = datetime(2017, 8, 8)
    issue_date = datetime(2017, 7, 7)
    maturity_date = datetime(2018, 1, 7)
    face_value = 100.0
    coupon_rate = 7.0

    # Convert settlement_date, issue_date, and maturity_date to QuantLib.Date
    settlement_date = QuantLib.Date(
        settlement_date.day, settlement_date.month, settlement_date.year
    )
    issue_date = QuantLib.Date(
        issue_date.day, issue_date.month, issue_date.year)
    maturity_date = QuantLib.Date(
        maturity_date.day, maturity_date.month, maturity_date.year
    )

    # Create a calendar and day-count convention based on the settlement date
    calendar = QuantLib.UnitedStates(QuantLib.UnitedStates.Settlement)

    day_count = QuantLib.Thirty360(QuantLib.UnitedStates.Settlement)

    # Set up the bond schedule
    tenor = QuantLib.Period(QuantLib.Semiannual)

    schedule = QuantLib.Schedule(
        issue_date,
        maturity_date,
        tenor,
        calendar,
        QuantLib.Unadjusted,
        QuantLib.Unadjusted,
        QuantLib.DateGeneration.Backward,
        False,
    )

    # Create the bond with settlement days set to 0
    bond = QuantLib.FixedRateBond(
        0, face_value, schedule, [coupon_rate / 100], day_count
    )

    # Return the accrued interest as a percentage of the face value
    accrued_amount: float = QuantLib.BondFunctions.accruedAmount(
        bond, settlement_date)

    interest_accrued2 = accrued_amount / face_value * 100

    return interest_accrued1, interest_accrued2


def solve_question_2():
    """
    Solve question 2.

    It is January 9, 2018. The price of a Treasury bond with a 6% coupon
    that matures on October 12, 2030, is quoted as 102-07.
    What is the cash price?
    """
    settlement_date = datetime(2018, 1, 9)
    issue_date = datetime(2017, 10, 12)
    maturity_date = datetime(2018, 4, 12)
    face_value = 100.0
    coupon_rate = 6.0

    # Convert settlement_date, issue_date, and maturity_date to QuantLib.Date
    settlement_date = QuantLib.Date(
        settlement_date.day, settlement_date.month, settlement_date.year)

    issue_date = QuantLib.Date(
        issue_date.day, issue_date.month, issue_date.year)

    maturity_date = QuantLib.Date(
        maturity_date.day, maturity_date.month, maturity_date.year)

    # Create a calendar and day-count convention based on the settlement date
    calendar = QuantLib.UnitedStates(QuantLib.UnitedStates.Settlement)

    day_count = QuantLib.ActualActual(QuantLib.UnitedStates.Settlement)

    # Set up the bond schedule
    tenor = QuantLib.Period(QuantLib.Semiannual)

    schedule = QuantLib.Schedule(
        issue_date,
        maturity_date,
        tenor,
        calendar,
        QuantLib.Unadjusted,
        QuantLib.Unadjusted,
        QuantLib.DateGeneration.Backward,
        False,
    )

    # Create the bond with settlement days set to 0
    coupons = [coupon_rate / 100]

    bond = QuantLib.FixedRateBond(0, face_value, schedule, coupons, day_count)

    # Return the accrued interest as a percentage of the face value
    accrued_amount = QuantLib.BondFunctions.accruedAmount(
        bond, settlement_date)

    interest_accrued = accrued_amount / face_value * 100

    quoted_price = 102 + 7 / 32

    cash_price = quoted_price + interest_accrued

    return cash_price


def solve_question_3():
    """
    Solve question 3.

    A three-month SOFR futures price changes from 96.76 to 96.82. What is
    the gain or loss to a trader who is long two contracts?
    """
    initial_price = 96.76
    final_price = 96.82
    contract_multiplier = 25  # per_basis_point
    contract_size = 100
    num_contracts = 2

    # Calculate price change
    price_change = round(final_price - initial_price, 2)

    # Calculate gain per contract
    gain_per_contract = contract_multiplier * contract_size * price_change

    # Calculate total gain or loss
    total_gain_or_loss = num_contracts * gain_per_contract

    return total_gain_or_loss


def solve_question_4():
    """
    Solve question 4.

    The 350-day LIBOR rate is 3% with continuous compounding and the forward
    rate calculated from a Eurodollar futures contract that matures in 350 days
    is 3.2% with continuous compounding. Estimate the 440-day zero rate.
    """
    # 350-day LIBOR rate
    libor_rate = 0.03

    # Eurodollar futures' forward rate
    forward_rate = 0.032

    # Eurodollar futures' forward maturity (days)
    forward_maturity = 350

    zero_period = 440

    eurodollar_interest_earned = forward_rate * 90

    libor_interest_earned = libor_rate * forward_maturity

    accumulated_interest = eurodollar_interest_earned + libor_interest_earned

    # Estimated 440-day zero rate (%)
    zero_rate = accumulated_interest / zero_period

    return zero_rate * 100


def solve_question_5():
    """
    Solve question 5.

    It is January 30. You are managing a bond portfolio worth $6 million. The
    duration of the portfolio in 6 months will be 8.2 years. The September
    Treasury bond futures price is currently 108-15, and the
    cheapest-to-deliver bond will have a duration of 7.6 years in September.
    How should you hedge against changes in interest rates over the next
    6 months?
    """
    # September Treasury bond futures price
    quoted_price = 108 + 15 / 32

    # Portfolio worth
    portfolio_worth = 6000000

    # Portfolio duration
    portfolio_duration = 8.2

    # Cheapest-to-deliver bond duration
    bond_duration = 7.6

    # Value of a contract
    contract_value = quoted_price * 1000

    # Hedge against changes in interest rates
    position = "shorted"

    dollar_duration = portfolio_worth / contract_value * portfolio_duration

    # Number of contracts
    nb_contract = dollar_duration / bond_duration

    print(
        f"Position should be closed out \"{position}\" at the end of July.")

    return position, nb_contract


def solve_question_6():
    """
    Solve question 6.

    The price of a 90-day Treasury bill is quoted as 10.00. What continuously
    compounded return (on an actual/365 basis) does an investor earn on the
    Treasury bill for the 90-day period?
    """
    duration = 90  # 90-day Treasury bill

    quoted_price = 10.00

    cash_price = 100 - (duration / 360) * quoted_price

    continuously_return = 365 / duration * math.log(1 + 2.5 / cash_price)

    return continuously_return


def solve_question_7():
    """
    Solve question 7.

    It is May 5, 2021. The quoted price of a government bond with a 12% coupon
    that matures on July 27, 2034, is 110-17. What is the cash price?
    """
    current_date = datetime(2021, 5, 5)

    quoted_price = 110 + 17 / 32

    maturity_date = datetime(2034, 7, 27)

    coupon = 12

    date_bgn = datetime(2021, 1, 27)

    period1 = (current_date - date_bgn).days

    date_end = datetime(2021, maturity_date.month, maturity_date.day)

    period2 = (date_end - date_bgn).days

    accrued_interest = (coupon / 2) * period1 / period2

    cash_price = quoted_price + accrued_interest

    return cash_price


def solve_question_8():
    """
    Solve question 8.

    Suppose that the Treasury bond futures price is 101-12. Which of the
    following four bonds is cheapest to deliver?

    =====  =======  =======
    Bond   Price    Conversion factor
    =====  =======  =======
    1      125-05   1.2131
    2      142-15   1.3792
    3      115-31   1.1149
    4      144-02   1.4026
    =====  =======  =======
    """
    futures_price = 101 + 12 / 32

    data = {
        "bond": [1, 2, 3, 4],
        "price": [125 + 5 / 32, 142 + 15 / 32, 115 + 31 / 32, 144 + 2 / 32],
        "conversion_factor": [1.2131, 1.3792, 1.1149, 1.4026],
    }

    data = pd.DataFrame(data)

    # The cheapest-to-deliver bond is the one having the lowest factor:
    # Quoted Price - Futures Price * Conversion Factor
    factor = data["price"] - futures_price * data["conversion_factor"]

    data = data.assign(factor=factor)

    cheapest_bond = data["bond"][data["factor"].idxmin()]

    return cheapest_bond


def solve_question_9():
    """
    Solve question 9.

    It is July 30, 2021. The cheapest-to-deliver bond in a September 2021
    Treasury bond futures contract is a 13% coupon bond, and delivery is
    expected to be made on September 30, 2021.
    Coupon payments on the bond are made on February 4 and August 4 each year.
    The term structure is flat, and the rate of interest with semiannual
    compounding is 12% per annum. The conversion factor for the bond is 1.5.
    The current quoted bond price is 110. Calculate the quoted futures price
    for the contract.
    """
    future = {}

    # Define dates
    date_1: datetime = datetime(2021, 2, 4)
    date_2: datetime = datetime(2021, 8, 4)
    future["current_date"] = datetime(2021, 7, 30)
    future["delivery_date"] = datetime(2021, 9, 30)

    # Constants
    future["quoted_price"] = 110
    future["coupon"] = 0.13
    future["conv_factor"] = 1.5

    # Calculate accrued interest for the bond
    period1 = (future["current_date"] - date_1).days
    period2 = (date_2 - date_1).days
    accrued_interest: float = (100 * future["coupon"] / 2) * period1 / period2

    # Calculate cash price
    future["cash_price"] = future["quoted_price"] + accrued_interest

    # Calculate present value for the bond
    interest_rate = 2 * math.log(1.06)
    time = 5 / 365
    future["present_value"] = (100 * future["coupon"] / 2) * \
        math.exp(-time * interest_rate)

    # Calculate duration of futures contract
    duration = (future["delivery_date"] - future["current_date"]).days / 365

    # Calculate net cash flow
    net_cash_flow = future["cash_price"] - future["present_value"]

    # Calculate cash future price
    future["cash_future_price"] = net_cash_flow * \
        math.exp(duration * interest_rate)

    # Calculate accrued interest for the bond
    n_days = (future["delivery_date"] - date_2).days
    n_days_2: int = 184
    future["interest_bond"] = (100 * future["coupon"] / 2) * n_days / n_days_2

    # Adjusted accrued interest for the bond
    future["adj_interest"] = future["cash_future_price"] - \
        future["interest_bond"]

    # Calculate quoted future price
    future["quoted_future_price"] = future["adj_interest"] / \
        future["conv_factor"]

    return future

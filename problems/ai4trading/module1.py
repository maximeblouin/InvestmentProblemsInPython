"""Module 1 - Trading with Momentum."""


import os
import pandas


def solve_lesson_4_chapter_4():
    """
    Solve lesson 4  - chapter 4 - Stock Prices.

    Find out the mean value for each stock using the `DataFrame.mean` function
    using the `DataFrame.pivot` function to get mean for each stock.
    """
    price_csv_file = os.path.join(os.path.dirname(os.path.abspath(
        __file__)), '..', '..', 'data', 'ai4trading', 'prices.csv')

    field_names = ['ticker', 'date', 'open', 'high', 'low',
                   'close', 'volume', 'adj_close', 'adj_volume']

    price_df = pandas.read_csv(price_csv_file, names=field_names)

    close_prices = price_df.pivot(
        index='date', columns='ticker', values='close')

    output = close_prices.mean()

    return output

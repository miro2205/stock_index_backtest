import pandas as pd

def generate_weekend_reversal_signals(data_universe: pd.DataFrame) -> pd.DataFrame:
    """
    Add a 'Signal' column to the DataFrame.
    Buy on Monday close if the previous Friday had a drop of 3% or more.
    """
    data_universe = data_universe.copy()
    data_universe["Weekday"] = data_universe.index.dayofweek
    data_universe["Daily Return"] = data_universe["Close"].pct_change()

    # Find Fridays with big drops
    data_universe["Big Friday Drop"] = (
        (data_universe["Weekday"] == 4) & (data_universe["Daily Return"] <= -0.03)
    )

    # Buy Monday if Friday had a big drop
    data_universe["Signal"] = 0
    data_universe.loc[
        data_universe["Big Friday Drop"].shift(1) & (data_universe["Weekday"] == 0),
        "Signal"
    ] = 1

    return data_universe

import pandas as pd

def generate_weekend_reversal_signals(data: pd.DataFrame) -> pd.DataFrame:
    # Copy the input DataFrame to avoid modifying the original
    data = data.copy()

    # Add a column to track the weekday (0 = Monday, 4 = Friday)
    data["Weekday"] = data.index.dayofweek

    # Calculate the daily percentage return
    data["Daily Return"] = data["Close"].pct_change()

    # Identify Fridays with a large drop (e.g., more than -1%)
    data["Big Friday Drop"] = (data["Weekday"] == 4) & (data["Daily Return"] <= -0.01)

    # Initialize signal column to 0 (no trade)
    data["Signal"] = 0

    # Generate buy signal on the Monday following a big Friday drop
    data.loc[(data["Big Friday Drop"].shift(1)) & (data["Weekday"] == 0), "Signal"] = 1

    return data

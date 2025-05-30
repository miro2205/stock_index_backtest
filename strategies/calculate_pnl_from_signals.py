import pandas as pd
from strategies.trade import Trade

def calculate_pnl_from_signals(data: pd.DataFrame, trade_size: float = 10000):
    # Copy the input data to preserve original structure
    data = data.copy()
    trades = []  # List to store all generated trades

    # Loop through the dataset and find points where a buy signal is triggered
    for i in range(len(data) - 1):
        if data["Signal"].iloc[i] == 1:
            entry_date = data.index[i]
            exit_date = data.index[i + 1]
            entry_price = data["Close"].iloc[i]
            exit_price = data["Close"].iloc[i + 1]

            # Create a Trade object for each signal
            trade = Trade(entry_date, entry_price, exit_date, exit_price)
            trade_summary = trade.summary(trade_size)
            trades.append(trade_summary)

            # Annotate trade information in the dataset
            data.loc[data.index[i], "Entry Price"] = entry_price
            data.loc[data.index[i + 1], "Exit Price"] = exit_price
            data.loc[data.index[i], "Trade PnL (%)"] = trade.pnl_percentage()
            data.loc[data.index[i], "Trade PnL ($)"] = trade.pnl_dollars(trade_size)

    # Return both the annotated dataset and list of trades
    return data, trades

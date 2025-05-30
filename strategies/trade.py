class Trade:
    def __init__(self, entry_date, entry_price, exit_date, exit_price):
        # Store trade entry and exit data
        self.entry_date = entry_date
        self.entry_price = entry_price
        self.exit_date = exit_date
        self.exit_price = exit_price

    def pnl_percentage(self) -> float:
        # Calculate percentage return from the trade
        return ((self.exit_price - self.entry_price) / self.entry_price) * 100

    def pnl_dollars(self, trade_size=10000) -> float:
        # Calculate absolute PnL in dollars based on trade size
        return self.pnl_percentage() / 100 * trade_size

    def summary(self, trade_size=10000) -> dict:
        # Ensure correct types for entry and exit prices in case they are pandas Series
        entry_price = self.entry_price.iloc[0] if hasattr(self.entry_price, "iloc") else self.entry_price
        exit_price = self.exit_price.iloc[0] if hasattr(self.exit_price, "iloc") else self.exit_price

        pnl_pct = self.pnl_percentage()
        if hasattr(pnl_pct, "iloc"):
            pnl_pct = pnl_pct.iloc[0]

        pnl_dollars = self.pnl_dollars(trade_size)
        if hasattr(pnl_dollars, "iloc"):
            pnl_dollars = pnl_dollars.iloc[0]

        # Return a dictionary summarizing the trade
        return {
            "Entry Date": self.entry_date,
            "Entry Price": float(entry_price),
            "Exit Date": self.exit_date,
            "Exit Price": float(exit_price),
            "PnL (%)": round(pnl_pct, 2),
            "PnL ($)": round(pnl_dollars, 2),
        }


import pandas as pd
import os

def summarize_performance(data: pd.DataFrame, trades: list, output_path: str = None):
    # Convert list of trades into a DataFrame
    trades_df = pd.DataFrame(trades)

    # Attempt to convert PnL columns to numeric (in case of formatting issues)
    trades_df["PnL ($)"] = pd.to_numeric(trades_df["PnL ($)"], errors="coerce")
    trades_df["PnL (%)"] = pd.to_numeric(trades_df["PnL (%)"], errors="coerce")

    # Drop any rows with invalid (NaN) data
    trades_df = trades_df.dropna(subset=["PnL ($)", "PnL (%)"])

    total_trades = len(trades_df)
    if total_trades == 0:
        print("No valid trades to summarize after filtering.")
        if output_path:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            empty_df = pd.DataFrame([{"Note": "No trades executed or all were invalid"}])
            empty_df.to_csv(output_path, index=False)
            print(f"Empty summary saved to: {output_path}")
        return

    # Calculate summary statistics
    wins = trades_df[trades_df["PnL ($)"] > 0]
    losses = trades_df[trades_df["PnL ($)"] <= 0]
    win_rate = len(wins) / total_trades
    avg_win = wins["PnL ($)"].mean() if not wins.empty else 0
    avg_loss = losses["PnL ($)"].mean() if not losses.empty else 0
    total_pnl = trades_df["PnL ($)"].sum()

    summary_stats = {
        "Total Trades": total_trades,
        "Win Rate": round(win_rate * 100, 2),
        "Average Win ($)": round(avg_win, 2),
        "Average Loss ($)": round(avg_loss, 2),
        "Total PnL ($)": round(total_pnl, 2)
    }

    # Print the summary to the console
    print("\nPerformance Summary")
    for k, v in summary_stats.items():
        print(f"{k}: {v}")

    # Optionally save to CSV if output path is provided
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        pd.DataFrame([summary_stats]).to_csv(output_path, index=False)
        print(f"Summary saved to: {output_path}")

        trades_csv = output_path.replace(".csv", "_trades.csv")
        trades_df.to_csv(trades_csv, index=False)
        print(f"Trade list saved to: {trades_csv}")
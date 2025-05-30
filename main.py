from data_fetcher.yahoo_downloader import download_index_data, save_data_to_csv
from strategies.weekend_reversal import generate_weekend_reversal_signals
from strategies.calculate_pnl_from_signals import calculate_pnl_from_signals
from strategies.summarize_performance import summarize_performance
import os

if __name__ == "__main__":
    # Configuration parameters
    ticker_symbol = "^GSPC"  # S&P 500 Index ticker symbol
    start_date = "2010-01-01"
    end_date = "2024-12-31"
    raw_data_path = "data/sp500_data.csv"
    signal_data_path = "data/sp500_signals.csv"
    results_path = "results/performance_summary.csv"

    # Step 1: Download historical index data from Yahoo Finance
    data_universe = download_index_data(ticker_symbol, start_date, end_date)

    if data_universe is not None:
        # Save the raw data to a CSV file
        save_data_to_csv(data_universe, raw_data_path)

        # Step 2: Generate buy/sell signals based on weekend reversal logic
        data_with_signals = generate_weekend_reversal_signals(data_universe)

        # Step 3: Calculate PnL for each trade based on signals
        data_with_pnl, trades = calculate_pnl_from_signals(data_with_signals, trade_size=10000)

        # Step 4: Summarize the performance and save results
        summarize_performance(data_with_pnl, trades, output_path=results_path)

        # Save the signal-enhanced dataset
        save_data_to_csv(data_with_pnl, signal_data_path)
    else:
        # Fail-safe if data download fails
        print(" Data download failed. Aborting.")







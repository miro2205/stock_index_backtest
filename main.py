from data_fetcher.yahoo_downloader import download_index_data, save_data_to_csv
from strategies.weekend_reversal import generate_weekend_reversal_signals

if __name__ == "__main__":

    # --- Configuration section ---
    ticker_symbol = "^GSPC"
    start_date = "2010-01-01"
    end_date = "2024-12-31"
    output_path = "data/sp500_data.csv"
    signal_output_path = "data/sp500_signals.csv"

    # --- Step 1: Download data ---
    data_universe = download_index_data(ticker_symbol, start_date, end_date)

    if data_universe is not None:
        # --- Step 2: Save raw data ---
        save_data_to_csv(data_universe, output_path)

        # --- Step 3: Generate signals ---
        data_with_signals = generate_weekend_reversal_signals(data_universe)

        # --- Step 4: Save signal-enhanced data ---
        save_data_to_csv(data_with_signals, signal_output_path)



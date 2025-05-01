from data_fetcher.yahoo_downloader import download_index_data, save_data_to_csv

if __name__ == "__main__":

    # --- Configuration section ---
    ticker_symbol = "^GSPC"  # S&P 500 index
    start_date = "2010-01-01"
    end_date = "2024-12-31"
    output_path = "data/sp500_data.csv"

    # --- Step 1: Download historical data ---
    data_universe = download_index_data(ticker_symbol, start_date, end_date)

    # --- Step 2: Save to CSV (if download was successful) ---
    if data_universe is not None:
        save_data_to_csv(data_universe, output_path)



import yfinance as yf
import pandas as pd
import os

def download_index_data(ticker_symbol, start_date, end_date):

    print(f" Downloading data for {ticker_symbol} from {start_date} to {end_date}...")

    try:
        ticker_data = yf.download(ticker_symbol, start=start_date, end=end_date)
    except Exception as error:
        print(f"❌ Download error: {error}")
        return None

    if ticker_data.empty:
        print("⚠️ No data returned. Check ticker or date range.")
        return None

    print("✅ Download successful.")
    return ticker_data


def save_data_to_csv(ticker_data, output_path):

    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        ticker_data.to_csv(output_path, index_label="Date")
        print(f"💾 Data saved to: {output_path}")
    except Exception as error:
        print(f"❌ Failed to save data: {error}")


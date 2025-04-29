# 1. Import necessary libraries
import yfinance as yf
import pandas as pd
import os


# 2. Define a function to download index data
def download_index_data(ticker, start_date, end_date, save_path):

    print(f"Downloading data for {ticker} from {start_date} to {end_date}...")

    # Use yfinance to download the data
    data = yf.download(ticker, start=start_date, end=end_date)

    # Check if data was downloaded
    if data.empty:
        print("⚠️ No data found. Please check ticker symbol or date range.")
        return

    # Save to CSV
    data.to_csv(save_path)
    print(f"✅ Data saved successfully to {save_path}.")


# 3. Set parameters
ticker = "^GSPC"  # S&P 500 index
start_date = "2010-01-01"
end_date = "2024-12-31"
save_path = os.path.join("data", "sp500_data.csv")

# 4. Make sure 'data/' directory exists
os.makedirs("data", exist_ok=True)

# 5. Download and save the data
download_index_data(ticker, start_date, end_date, save_path)

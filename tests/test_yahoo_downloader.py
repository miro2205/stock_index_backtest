import pandas as pd
from data_fetcher.yahoo_downloader import download_index_data

def test_download_index_data_valid():
    df = download_index_data("^GSPC", "2022-01-01", "2022-01-10")
    assert isinstance(df, pd.DataFrame)
    assert "Close" in df.columns

def test_download_index_data_invalid_ticker():
    df = download_index_data("INVALID_TICKER", "2022-01-01", "2022-01-10")
    assert df is None or df.empty
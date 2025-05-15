import pandas as pd
from strategies.weekend_reversal import generate_weekend_reversal_signals

def test_generate_signals_structure():
    # Mock data
    dates = pd.date_range("2024-04-25", periods=5, freq="D")
    close_prices = [100, 97, 98, 96, 95]  # Friday is last (drop of 1.04%)
    df = pd.DataFrame({"Close": close_prices}, index=dates)

    result = generate_weekend_reversal_signals(df)

    assert isinstance(result, pd.DataFrame)
    assert "Signal" in result.columns
    assert set(result["Signal"].unique()).issubset({0, 1})
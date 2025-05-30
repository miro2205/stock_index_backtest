# Stock Index Backtesting System

This project implements a fully automated backtesting framework for the Weekend Reversal Strategy, applied to the S&P 500 (^GSPC). It is designed as an educational tool to demonstrate how algorithmic trading strategies can be developed, validated, and summarized using real market data.

## Features
- Data Download via Yahoo Finance API (yfinance)
- Signal Generation based on Monday buy triggers after large Friday drops
- Trade Modeling using an object-oriented Trade class
- PnL Calculation for each signal using historical price data
- Performance Summary including win rate, average win/loss, total return
- Unit Testing for robustness and academic compliance

## Structure
stock_index_backtest/
├── main.py
├── data/                        # Raw and signal-enhanced CSV files
├── results/                     # Performance summary outputs
├── data_fetcher/
│   └── yahoo_downloader.py     # API-based data download module
├── strategies/
│   ├── trade.py                # Trade class with PnL logic
│   ├── weekend_reversal.py    # Signal generation logic
│   ├── calculate_pnl_from_signals.py
│   └── summarize_performance.py
└── tests/
    ├── test_trade.py
    ├── test_yahoo_downloader.py
    └── test_weekend_reversal.py

## Goals
- Build a complete stock index backtesting system.
- Learn GitHub-based professional project management.

## Author
Miroslav Kello
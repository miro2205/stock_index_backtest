import unittest
from strategies.trade import Trade

class TestTrade(unittest.TestCase):

    def test_pnl_percentage_positive(self):
        trade = Trade("2022-01-01", 100.0, "2022-01-02", 110.0)
        self.assertAlmostEqual(trade.pnl_percentage(), 10.0, places=2)

    def test_pnl_percentage_negative(self):
        trade = Trade("2022-01-01", 100.0, "2022-01-02", 90.0)
        self.assertAlmostEqual(trade.pnl_percentage(), -10.0, places=2)

    def test_pnl_dollars_default_trade_size(self):
        trade = Trade("2022-01-01", 100.0, "2022-01-02", 110.0)
        self.assertAlmostEqual(trade.pnl_dollars(), 1000.0, places=2)

    def test_summary_structure(self):
        trade = Trade("2022-01-01", 100.0, "2022-01-02", 110.0)
        summary = trade.summary()
        self.assertIsInstance(summary, dict)
        self.assertIn("Entry Date", summary)
        self.assertIn("Exit Price", summary)
        self.assertAlmostEqual(summary["PnL (%)"], 10.0, places=2)
        self.assertAlmostEqual(summary["PnL ($)"], 1000.0, places=2)

if __name__ == '__main__':
    unittest.main()

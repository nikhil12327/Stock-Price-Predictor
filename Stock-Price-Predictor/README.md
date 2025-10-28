# Stock Price Predictor

This project predicts stock closing prices using historical data (sample CSV included).

## Quick Start
1. Create a Python environment and install requirements: `pip install -r requirements.txt`
2. Run training: `python src/model.py`
3. Visualize results: open `notebooks/stock_price_prediction.ipynb` or run `python src/visualize.py`

## Notes
- A synthetic sample dataset is included at `data/aapl_sample.csv` for offline demonstration.
- To fetch real data, use `src/data_fetch.py` (requires yfinance and network access).

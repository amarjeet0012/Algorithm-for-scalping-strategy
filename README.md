
# Optimized Scalping Algorithm for AAPL and TSLA Stocks

This repository contains a backtesting algorithm built with QuantConnect that optimizes a scalping trading strategy for **Apple Inc. (AAPL)** and **Tesla Inc. (TSLA)** stocks. The algorithm utilizes moving averages and RSI indicators to capture short-term price movements and manage risk with stop loss and take profit targets.

## Features

- **Stocks**: Focused on **AAPL** and **TSLA** stocks.
- **Indicators**: Uses 10-period and 30-period SMA, along with a 14-period RSI.
- **Risk Management**: Implements 1% stop loss and 2% take profit strategies.
- **Warm-Up Period**: Uses 30-minute warm-up to initialize indicators.
- **Backtesting Period**: Runs from 2022-09-11 to 2024-09-11.
- **Resolution**: Backtests on minute-level price data for both stocks.

## Algorithm Logic

1. **Buy Signal**: 
   - Short-term SMA crosses above the long-term SMA.
   - RSI value is below 30 (indicating oversold conditions).
   - No previous buy action is active.
   
2. **Sell Signal**: 
   - Short-term SMA crosses below the long-term SMA.
   - RSI value is above 70 (indicating overbought conditions).
   - No previous sell action is active.
   
3. **Stop Loss & Take Profit**:
   - A 1% stop loss and 2% take profit are applied after entering a position to manage risk.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```

2. Ensure you have a QuantConnect account and environment set up to run the backtest.

3. Modify and test the algorithm using the `backtest.py` file in QuantConnect or another backtesting platform.

## Performance

- **AAPL Stock Strategy**: 
   - The algorithm yields an **estimated 10% return** over the last two years based on backtested results.
   
- **TSLA Stock Strategy**:
   - The algorithm yields an **estimated 14% return** over the last two years based on backtested results.

## License

This project is licensed under the MIT License.

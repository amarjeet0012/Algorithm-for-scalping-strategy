# region imports
from AlgorithmImports import *
# endregion

from AlgorithmImports import *

class OptimizedScalpingAlgorithm(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2022, 9, 11)  # Set Start Date
        self.SetEndDate(2024, 9, 11)    # Set End Date
        self.SetCash(100000)            # Set Strategy Cash
        self.symbol = self.AddEquity("AAPL", Resolution.Minute).Symbol  # Add equity with minute resolution

        # Define moving averages
        self.sma_short = self.SMA(self.symbol, 10, Resolution.Minute)  # Adjusted periods
        self.sma_long = self.SMA(self.symbol, 30, Resolution.Minute)  # Adjusted periods

        # Define thresholds
        self.last_action = None
        self.stop_loss = 0.01  # 1% stop loss
        self.take_profit = 0.02  # 2% take profit

        self.SetWarmUp(30, Resolution.Minute)  # Warm-up for 30 minutes

        # Initialize indicators
        self.rsi = self.RSI(self.symbol, 14, MovingAverageType.Wilders, Resolution.Minute)

    def OnData(self, slice):
        if self.IsWarmingUp:
            return

        # Check if the required data is available
        if not self.sma_short.IsReady or not self.sma_long.IsReady or not self.rsi.IsReady:
            return

        if self.symbol not in slice.Bars:
            return

        price = slice.Bars[self.symbol].Close
        rsi_value = self.rsi.Current.Value

        # Trading signals
        if self.sma_short.Current.Value > self.sma_long.Current.Value and rsi_value < 30 and self.last_action != 'BUY':
            self.SetHoldings(self.symbol, 1)  # Buy
            self.last_action = 'BUY'
            self.stop_loss_price = price * (1 - self.stop_loss)
            self.take_profit_price = price * (1 + self.take_profit)
        elif self.sma_short.Current.Value < self.sma_long.Current.Value and rsi_value > 70 and self.last_action != 'SELL':
            self.SetHoldings(self.symbol, -1)  # Sell
            self.last_action = 'SELL'
            self.stop_loss_price = price * (1 + self.stop_loss)
            self.take_profit_price = price * (1 - self.take_profit)

        # Stop loss and take profit management
        for position in self.Portfolio.Values:
            if position.Invested:
                if position.Quantity > 0:
                    if price <= self.stop_loss_price or price >= self.take_profit_price:
                        self.Liquidate(self.symbol)
                elif position.Quantity < 0:
                    if price >= self.stop_loss_price or price <= self.take_profit_price:
                        self.Liquidate(self.symbol)

    def OnOrderEvent(self, orderEvent):
        self.Debug(f"Order Event: {orderEvent}")

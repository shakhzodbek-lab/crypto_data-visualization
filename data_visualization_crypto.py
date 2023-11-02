import matplotlib.pyplot as plt
import mplfinance
import yfinance as yf

crypto = "ETH-USD"  # Example: Etherium in USD

# Create a Ticker object
crypto_data = yf.Ticker(crypto)

# Fetch historical data
data = crypto_data.history(period="1y")  # You can adjust the period as needed

# Print the data
mplfinance.plot(data, type = "candle", volume = True)


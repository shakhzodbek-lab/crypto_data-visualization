
---

# Cryptocurrency Historical Data Visualization

This Python script allows you to fetch and visualize historical data for a specific cryptocurrency in USD (e.g., Ethereum, denoted as ETH-USD) using the `yfinance` and `mplfinance` libraries.

## Prerequisites

Before using this script, ensure that you have the following Python libraries installed in your environment:

- `yfinance`: A library for accessing Yahoo Finance data.
- `mplfinance`: A library for creating financial and stock charts.

You can install these libraries using `pip`:

```bash
pip install yfinance mplfinance
```

## Usage

1. Open the Python script in your code editor or IDE.

2. Update the `crypto` variable to specify the cryptocurrency and currency pair you want to fetch data for (e.g., "ETH-USD" for Ethereum in USD).

3. Adjust the period for which you want to retrieve historical data by modifying the `period` parameter in the following line:

   ```python
   data = crypto_data.history(period="1y")  # You can adjust the period as needed
   ```

   For the last 6 months, you can change it to:

   ```python
   data = crypto_data.history(period="6mo")
   ```

4. Save your changes.

5. Run the script, and it will fetch the historical data and display a candlestick chart with volume data using `mplfinance`.

## Example

Here's an example using Ethereum (ETH) historical data in USD for the last year:

```python
crypto = "ETH-USD"  # Example: Ethereum in USD

# Create a Ticker object
crypto_data = yf.Ticker(crypto)

# Fetch historical data for the last year (you can adjust the period)
data = crypto_data.history(period="1y")

# Visualize the data as a candlestick chart with volume
mplfinance.plot(data, type="candle", volume=True)
```

## License

This script is provided under an open-source license. Feel free to modify and use it as needed for your projects.

---

You can save this README file in the same directory as your Python script to provide instructions and information about your code.

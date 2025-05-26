"""
Crypto Data Visualization: Simple Cryptocurrency Analysis Tool

This program fetches cryptocurrency prices using the CoinGecko API 
and creates candlestick chart visualizations using matplotlib. Users can
select which cryptocurrency they want to analyze.

Features:
- View current cryptocurrency prices
- Generate candlestick charts for price analysis
- Support for multiple time periods (1 day, 7 days, 30 days, 90 days)
- Error handling and input validation

Required packages:
- requests: For API communication
- matplotlib: For data visualization
- pandas: For data manipulation
- mplfinance: For candlestick charts

Inspired by ChatGPT
"""

import sys
import requests
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
from datetime import datetime

# List of cryptocurrencies to fetch data for
CRYPTOS = [
    {"id": "bitcoin",     "symbol": "BTC",  "name": "Bitcoin"},
    {"id": "ethereum",    "symbol": "ETH",  "name": "Ethereum"},
    {"id": "ripple",      "symbol": "XRP",  "name": "XRP"},
    {"id": "binancecoin", "symbol": "BNB",  "name": "Binance Coin"},
    {"id": "solana",      "symbol": "SOL",  "name": "Solana"},
    {"id": "dogecoin",    "symbol": "DOGE", "name": "Dogecoin"},
    {"id": "cardano",     "symbol": "ADA",  "name": "Cardano"},
    {"id": "tron",        "symbol": "TRX",  "name": "TRON"},
    {"id": "hyperliquid", "symbol": "HYPE","name": "Hyperliquid"},
    {"id": "sui",         "symbol": "SUI",  "name": "Sui"}
]

# Base URL for CoinGecko API
API_BASE = "https://api.coingecko.com/api/v3"


def fetch_current_prices():
    """
    Fetch current USD prices for each cryptocurrency defined in CRYPTOS.
    Returns:
        pd.DataFrame: columns ['Name', 'Symbol', 'Price'] with formatted price strings.
    Raises:
        SystemExit: on network or API errors.
    """
    try:
        # Join all coin IDs into comma-separated string for API call
        ids = ",".join(c['id'] for c in CRYPTOS)
        # Request market data from CoinGecko
        resp = requests.get(
            f"{API_BASE}/coins/markets",
            params={"vs_currency": "usd", "ids": ids, "order": "market_cap_desc"}
        )
        resp.raise_for_status()  # Throws HTTPError for bad responses
        data = resp.json()       # Parse JSON into Python objects

        # Load into DataFrame and select relevant columns
        df = pd.DataFrame(data)[['name', 'symbol', 'current_price']]
        df.rename(columns={'name': 'Name', 'symbol': 'Symbol', 'current_price': 'Price'}, inplace=True)

        # Format price values as strings with dollar sign and two decimals
        df['Price'] = df['Price'].apply(lambda x: f"${x:,.2f}")
        return df

    except requests.RequestException as e:
        # Print error and exit if network/API call fails
        print(f"Error fetching current prices: {e}")
        sys.exit(1)


def fetch_historical_data(coin_id, days=7):
    """
    Fetch OHLC (open, high, low, close) data for a given coin over a specified time window.

    Args:
        coin_id (str): CoinGecko ID of the cryptocurrency.
        days (int): Time window in days (supported values: 1, 7, 14, 30, 90).

    Returns:
        pd.DataFrame: Indexed by timestamp, with columns ['open', 'high', 'low', 'close'].

    Raises:
        SystemExit: on HTTP errors or no data returned.
    """
    try:
        # Call CoinGecko OHLC endpoint
        resp = requests.get(
            f"{API_BASE}/coins/{coin_id}/ohlc",
            params={"vs_currency": "usd", "days": days}
        )
        resp.raise_for_status()
        data = resp.json()

        # Ensure data is a non-empty list
        if not isinstance(data, list) or not data:
            raise ValueError("No historical data returned.")

        # Construct DataFrame and convert timestamp to datetime index
        df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        return df

    except (requests.RequestException, ValueError) as e:
        # Print any errors and exit program
        print(f"Error fetching historical data for {coin_id}: {e}")
        sys.exit(1)


def plot_candlestick(df, title: str, days: int):
    """
    Generate and display a candlestick chart for the provided OHLC DataFrame.

    Args:
        df (pd.DataFrame): DataFrame with datetime index and OHLC columns.
        title (str): Title for the chart.
        days (int): Number of days of data; adjusts x-axis timestamp format.
    """
    # Define market colors: green for up days, red for down days
    mc = mpf.make_marketcolors(up='green', down='red')
    # Create style based on classic template and custom colors
    style = mpf.make_mpf_style(base_mpf_style='classic', marketcolors=mc)

    # Create matplotlib figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.suptitle(title, fontsize=16, y=0.95)

    # Choose datetime label format: hours for 1-day data, dates otherwise
    fmt = '%H:%M' if days == 1 else '%Y-%m-%d'
    mpf.plot(
        df,
        type='candle',         # Candlestick chart
        style=style,
        ax=ax,
        ylabel='Price (USD)',  # Y-axis label
        datetime_format=fmt,
        xrotation=15,          # Rotate x-axis labels for readability
        tight_layout=True      # Minimize padding
    )
    plt.show()  # Display the chart


def select_option(prompt, options):
    """
    Present numbered menu to the user and validate their selection.

    Args:
        prompt (str): Prompt message to display before options.
        options (list): List of option strings to choose from.

    Returns:
        int: Index of the selected option (0-based).
    """
    while True:
        # Print prompt and options
        print(prompt + "\n")
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")
        try:
            # Read user input and convert to integer
            choice = int(input(f"Enter choice [1-{len(options)}]: "))
            if 1 <= choice <= len(options):
                return choice - 1
            else:
                print(f"\nPlease enter a number between 1 and {len(options)}.\n")
        except ValueError:
            # Handle non-integer inputs
            print("\nInvalid input; please enter a number.\n")


def main():
    """
    Main execution function to:
      1. Fetch and display current prices
      2. Prompt user to select a cryptocurrency and time window
      3. Fetch historical OHLC data and plot candlestick chart
    """
    try:
        # Fetch and display current prices
        df_prices = fetch_current_prices()
        now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("\n===== Crypto Data =====")
        print(f"Prices as of {now_str}\n")
        # Print DataFrame without row indices
        print(df_prices.to_string(index=False), "\n")

        # Build menu labels for selection
        names = [f"{r['Name']} ({r['Symbol']})" for _, r in df_prices.iterrows()]
        idx = select_option("Select a cryptocurrency:", names)
        coin = CRYPTOS[idx]

        # Offer historical time periods
        day_opts = ["1", "7", "14", "30", "90"]
        idx_days = select_option("\nSelect historical data period (days):", day_opts)
        days = int(day_opts[idx_days])

        print(f"\nFetching {coin['name']} data for last {days} days...\n")
        # Retrieve historical data and plot
        df_hist = fetch_historical_data(coin['id'], days)
        plot_candlestick(df_hist, f"{coin['name']} - Last {days} Days", days)

    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
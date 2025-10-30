import yfinance as yf
from datetime import datetime, timedelta


def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        # Get the most recent price
        data = stock.history(period='1d')

        if data.empty:
            return None

        current_price = data['Close'].iloc[-1]
        return round(current_price, 2)

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None


def get_stock_info(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        # Get historical data to calculate volatility
        hist = stock.history(period='1y')

        if hist.empty:
            return None

        # Calculate annual volatility from historical returns
        returns = hist['Close'].pct_change().dropna()
        volatility = returns.std() * (252 ** 0.5)  # Annualized volatility

        return {
            'symbol': ticker.upper(),
            'name': info.get('longName', 'N/A'),
            'current_price': round(hist['Close'].iloc[-1], 2),
            'volatility': round(volatility, 4),
            'currency': info.get('currency', 'USD')
        }

    except Exception as e:
        print(f"Error fetching info for {ticker}: {e}")
        return None


def display_stock_info(info):
    """Display stock information in a formatted way."""
    print("\n" + "=" * 50)
    print("STOCK INFORMATION")
    print("=" * 50)
    print(f"Symbol: {info['symbol']}")
    print(f"Company: {info['name']}")
    print(f"Current Price: ${info['current_price']}")
    print(f"Estimated Annual Volatility: {info['volatility'] * 100:.2f}%")
    print(f"Currency: {info['currency']}")
    print("=" * 50)

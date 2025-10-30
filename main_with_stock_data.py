import math
from scipy.stats import norm
from stock_data import get_stock_info


def black_scholes_call(S, K, T, r, sigma):
    """Calculate Black-Scholes call option price."""
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    return call_price


def black_scholes_put(S, K, T, r, sigma):
    """Calculate Black-Scholes put option price."""
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    put_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price


def calculate_greeks(S, K, T, r, sigma, option_type='call'):
    """Calculate option Greeks."""
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        delta = norm.cdf(d1)
    else:
        delta = norm.cdf(d1) - 1

    gamma = norm.pdf(d1) / (S * sigma * math.sqrt(T))
    vega = S * norm.pdf(d1) * math.sqrt(T) / 100

    if option_type == 'call':
        theta = (-S * norm.pdf(d1) * sigma / (2 * math.sqrt(T)) -
                 r * K * math.exp(-r * T) * norm.cdf(d2)) / 365
    else:
        theta = (-S * norm.pdf(d1) * sigma / (2 * math.sqrt(T)) +
                 r * K * math.exp(-r * T) * norm.cdf(-d2)) / 365

    if option_type == 'call':
        rho = K * T * math.exp(-r * T) * norm.cdf(d2) / 100
    else:
        rho = -K * T * math.exp(-r * T) * norm.cdf(-d2) / 100

    return {
        'delta': delta,
        'gamma': gamma,
        'vega': vega,
        'theta': theta,
        'rho': rho
    }


def main():
    """Interactive option pricing calculator with real stock data."""
    print("=" * 50)
    print("BLACK-SCHOLES OPTION PRICING MODEL")
    print("=" * 50)

    # Ask user if they want to use real stock data
    print("\nChoose input method:")
    print("1. Use real stock data (enter ticker symbol)")
    print("2. Manual input (enter all parameters)")

    choice = input("\nEnter choice (1 or 2): ").strip()

    if choice == "1":
        # Get real stock data
        ticker = input("\nEnter stock ticker (e.g., AAPL, TSLA, MSFT): ").upper()
        stock_info = get_stock_info(ticker)

        if not stock_info:
            print(f"Could not retrieve data for {ticker}. Please try again.")
            return

        # Display stock info
        print("\n" + "=" * 50)
        print("STOCK INFORMATION")
        print("=" * 50)
        print(f"Symbol: {stock_info['symbol']}")
        print(f"Company: {stock_info['name']}")
        print(f"Current Price: ${stock_info['current_price']}")
        print(f"Estimated Volatility: {stock_info['volatility'] * 100:.2f}%")

        # Use stock price, ask for other parameters
        S = stock_info['current_price']
        sigma = stock_info['volatility']

        K = float(input(f"\nEnter strike price (current price is ${S}): $"))
        T = float(input("Enter time to expiration (years): "))
        r = float(input("Enter risk-free rate (as decimal, e.g., 0.05 for 5%): "))

        # Ask if user wants to use estimated volatility or custom
        use_estimated = input(f"\nUse estimated volatility of {sigma * 100:.2f}%? (y/n): ").lower()
        if use_estimated != 'y':
            sigma = float(input("Enter custom volatility (as decimal, e.g., 0.2 for 20%): "))

    else:
        # Manual input
        S = float(input("\nEnter current stock price: $"))
        K = float(input("Enter strike price: $"))
        T = float(input("Enter time to expiration (years): "))
        r = float(input("Enter risk-free rate (as decimal, e.g., 0.05 for 5%): "))
        sigma = float(input("Enter volatility (as decimal, e.g., 0.2 for 20%): "))

    # Calculate prices and greeks
    call = black_scholes_call(S, K, T, r, sigma)
    put = black_scholes_put(S, K, T, r, sigma)
    greeks_call = calculate_greeks(S, K, T, r, sigma, 'call')
    greeks_put = calculate_greeks(S, K, T, r, sigma, 'put')

    # Display results
    print("\n" + "=" * 50)
    print("CALL OPTION")
    print("=" * 50)
    print(f"Price: ${call:.2f}")
    print(f"Delta: {greeks_call['delta']:.4f}")
    print(f"Gamma: {greeks_call['gamma']:.4f}")
    print(f"Vega: {greeks_call['vega']:.4f}")
    print(f"Theta: {greeks_call['theta']:.4f}")
    print(f"Rho: {greeks_call['rho']:.4f}")

    print("\n" + "=" * 50)
    print("PUT OPTION")
    print("=" * 50)
    print(f"Price: ${put:.2f}")
    print(f"Delta: {greeks_put['delta']:.4f}")
    print(f"Gamma: {greeks_put['gamma']:.4f}")
    print(f"Vega: {greeks_put['vega']:.4f}")
    print(f"Theta: {greeks_put['theta']:.4f}")
    print(f"Rho: {greeks_put['rho']:.4f}")


if __name__ == "__main__":
    main()
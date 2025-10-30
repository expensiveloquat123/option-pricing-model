import math
from scipy.stats import norm


def black_scholes_call(S, K, T, r, sigma):
    """
    Calculate Black-Scholes call option price.

    Parameters:
        S: Current stock price
        K: Strike price
        T: Time to expiration (years)
        r: Risk-free rate
        sigma: Volatility
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    return call_price


def black_scholes_put(S, K, T, r, sigma):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    put_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price


def calculate_greeks(S, K, T, r, sigma, option_type='call'):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    # Delta: rate of change of option price with respect to stock price
    if option_type == 'call':
        delta = norm.cdf(d1)
    else:  # put
        delta = norm.cdf(d1) - 1

    # Gamma: rate of change of delta with respect to stock price
    gamma = norm.pdf(d1) / (S * sigma * math.sqrt(T))

    # Vega: rate of change of option price with respect to volatility
    vega = S * norm.pdf(d1) * math.sqrt(T) / 100  # Divided by 100 for 1% change

    # Theta: rate of change of option price with respect to time (per day)
    if option_type == 'call':
        theta = (-S * norm.pdf(d1) * sigma / (2 * math.sqrt(T)) -
                 r * K * math.exp(-r * T) * norm.cdf(d2)) / 365
    else:  # put
        theta = (-S * norm.pdf(d1) * sigma / (2 * math.sqrt(T)) +
                 r * K * math.exp(-r * T) * norm.cdf(-d2)) / 365

    # Rho: rate of change of option price with respect to interest rate
    if option_type == 'call':
        rho = K * T * math.exp(-r * T) * norm.cdf(d2) / 100  # Divided by 100 for 1% change
    else:  # put
        rho = -K * T * math.exp(-r * T) * norm.cdf(-d2) / 100

    return {
        'delta': delta,
        'gamma': gamma,
        'vega': vega,
        'theta': theta,
        'rho': rho
    }

def main():
    """Interactive option pricing calculator."""
    print("=" * 50)
    print("BLACK-SCHOLES OPTION PRICING MODEL")
    print("=" * 50)

    # Inputs
    S = float(input("\nEnter current stock price: $"))
    K = float(input("Enter strike price: $"))
    T = float(input("Enter time to expiration (years): "))
    r = float(input("Enter risk-free rate (as decimal, e.g., 0.05 for 5%): "))
    sigma = float(input("Enter volatility (as decimal, e.g., 0.2 for 20%): "))

    # Formulas
    call = black_scholes_call(S, K, T, r, sigma)
    put = black_scholes_put(S, K, T, r, sigma)
    greeks_call = calculate_greeks(S, K, T, r, sigma, 'call')
    greeks_put = calculate_greeks(S, K, T, r, sigma, 'put')


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


main()
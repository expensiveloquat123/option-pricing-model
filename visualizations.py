import matplotlib.pyplot as plt
import numpy as np
from main import black_scholes_call, black_scholes_put


def plot_option_price_vs_stock_price(K, T, r, sigma):
    """
    Plot how option prices change as stock price changes.
    """
    # Create range of stock prices around the strike
    stock_prices = np.linspace(K * 0.5, K * 1.5, 100)

    call_prices = [black_scholes_call(S, K, T, r, sigma) for S in stock_prices]
    put_prices = [black_scholes_put(S, K, T, r, sigma) for S in stock_prices]

    plt.figure(figsize=(10, 6))
    plt.plot(stock_prices, call_prices, label='Call Option', linewidth=2)
    plt.plot(stock_prices, put_prices, label='Put Option', linewidth=2)
    plt.axvline(x=K, color='gray', linestyle='--', label=f'Strike Price (${K})')

    plt.xlabel('Stock Price ($)', fontsize=12)
    plt.ylabel('Option Price ($)', fontsize=12)
    plt.title('Option Prices vs Stock Price', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_option_price_vs_volatility(S, K, T, r):
    """
    Plot how option prices change as volatility changes.
    """
    volatilities = np.linspace(0.05, 0.8, 100)

    call_prices = [black_scholes_call(S, K, T, r, sigma) for sigma in volatilities]
    put_prices = [black_scholes_put(S, K, T, r, sigma) for sigma in volatilities]

    plt.figure(figsize=(10, 6))
    plt.plot(volatilities * 100, call_prices, label='Call Option', linewidth=2)
    plt.plot(volatilities * 100, put_prices, label='Put Option', linewidth=2)

    plt.xlabel('Volatility (%)', fontsize=12)
    plt.ylabel('Option Price ($)', fontsize=12)
    plt.title('Option Prices vs Volatility', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_option_price_vs_time(S, K, r, sigma):
    """
    Plot how option prices change as time to expiration changes.
    """
    times = np.linspace(0.01, 2, 100)  # From ~3 days to 2 years

    call_prices = [black_scholes_call(S, K, T, r, sigma) for T in times]
    put_prices = [black_scholes_put(S, K, T, r, sigma) for T in times]

    plt.figure(figsize=(10, 6))
    plt.plot(times, call_prices, label='Call Option', linewidth=2)
    plt.plot(times, put_prices, label='Put Option', linewidth=2)

    plt.xlabel('Time to Expiration (years)', fontsize=12)
    plt.ylabel('Option Price ($)', fontsize=12)
    plt.title('Option Prices vs Time to Expiration', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# Test the visualizations
S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

print("Generating visualizations...")
print("Close each chart window to see the next one.")

def main(S,K,T,r,sigma):
    plot_option_price_vs_stock_price(K, T, r, sigma)
    plot_option_price_vs_volatility(S, K, T, r)
    plot_option_price_vs_time(S, K, r, sigma)

if __name__ == "__main__":
    main(S, K, T, r, sigma)
# Black-Scholes Option Pricing Model

A Python implementation of the Black-Scholes model for pricing European call and put options, including calculation of option Greeks.

## Features

- **Real-Time Stock Data**: Pull live stock prices and calculate historical volatility from Yahoo Finance
- **Option Pricing**: Calculate theoretical prices for both call and put options
- **Greeks Calculation**: Compute all five primary Greeks (Delta, Gamma, Vega, Theta, Rho)
- **Interactive Interface**: User-friendly command-line interface for inputting parameters
- **Visualizations**: Generate charts showing how option prices change with different parameters
  - Option price vs stock price
  - Option price vs volatility
  - Option price vs time to expiration
- **Accurate Implementation**: Based on the classic Black-Scholes-Merton formula

## What are Options?

Options are financial derivatives that give the holder the right (but not obligation) to buy or sell an underlying asset at a specified price (strike price) before a certain date.

- **Call Option**: Right to BUY the asset at the strike price
- **Put Option**: Right to SELL the asset at the strike price

## The Black-Scholes Model

The Black-Scholes model calculates the theoretical value of European-style options using five key inputs:

1. **S** - Current stock price
2. **K** - Strike price
3. **T** - Time to expiration (in years)
4. **r** - Risk-free interest rate
5. **σ** (sigma) - Volatility of the underlying asset

## The Greeks

The "Greeks" measure the sensitivity of option prices to various factors:

- **Delta (Δ)**: Rate of change of option price with respect to stock price
- **Gamma (Γ)**: Rate of change of Delta with respect to stock price
- **Vega (ν)**: Sensitivity to volatility changes
- **Theta (Θ)**: Time decay - how much value the option loses per day
- **Rho (ρ)**: Sensitivity to interest rate changes

## Installation

1. Clone this repository:
```bash
git clone https://github.com/expensiveloquat123/option-pricing-model.git
cd option-pricing-model
```

2. Install required dependencies:
```bash
pip3 install scipy matplotlib numpy yfinance --break-system-packages
```

## Usage

### Option 1: Use Real Stock Data

Run the enhanced program with real-time stock data:
```bash
python main_with_stock_data.py
```

Choose option 1 and enter a stock ticker (e.g., AAPL, TSLA, GOOGL). The program will:
- Fetch current stock price
- Calculate historical volatility
- Let you customize strike price, expiration, and risk-free rate

### Option 2: Manual Input

Run the program with manual inputs:
```bash
python main.py
```

Or choose option 2 in `main_with_stock_data.py` to enter all parameters manually.

## Visualizations

To generate visualizations showing how option prices change with different parameters:
```bash
python visualizations.py
```

This will generate three charts:
1. **Option Price vs Stock Price** - Shows call and put values across different stock prices
2. **Option Price vs Volatility** - Demonstrates how volatility affects option pricing
3. **Option Price vs Time** - Illustrates time decay (theta) effect

Close each chart window to see the next visualization.

### Example
```
Enter current stock price: $100
Enter strike price: $100
Enter time to expiration (years): 1
Enter risk-free rate (as decimal, e.g., 0.05 for 5%): 0.05
Enter volatility (as decimal, e.g., 0.2 for 20%): 0.20
```

Output:
```
==================================================
CALL OPTION
==================================================
Price: $10.45
Delta: 0.6368
Gamma: 0.0188
Vega: 0.3752
Theta: -0.0176
Rho: 0.5323

==================================================
PUT OPTION
==================================================
Price: $5.57
Delta: -0.3632
Gamma: 0.0188
Vega: 0.3752
Theta: -0.0045
Rho: -0.4189
```

## Requirements

- Python 3.x
- scipy
- matplotlib
- numpy
- yfinance

## Future Enhancements

- Implement Monte Carlo simulation for exotic options
- Add real-time stock data integration via API
- Create web-based interface
- Add implied volatility calculator

## License

MIT License

## Author

Ana Lucia Leon

# Option Chain Strategy Builder

Option Strategy Builder is a Python library designed to help traders and investors calculate the profit and loss (PnL) of various option strategies and visualize their potential outcomes. Utilizing the Mibian library for options pricing and matplotlib for plotting, this tool simplifies the analysis of complex options strategies.

## Features

-   Calculate the PnL of option strategies considering current and expected prices.
-   Visualize strategy PnL across different expected prices of the underlying asset.
-   Support for 'call' and 'put' options, including buy and sell positions.

## Installation

To install Option Strategy Builder, ensure you have Python installed on your system, then run the following command:

shCopy code

`pip install option-strategy-builder` 

## Usage

Here is a quick example of how to use Option Strategy Builder to calculate and plot the PnL of an options strategy:


```
from option_strategy_builder import calculate_strategy_pnl, plot_strategy_pnl_with_labels

options = [
    # (strike_price, premium, qty, IV, time to expiry in days, call or put, buy or sell)
    (22650, 18.50, 50*1, 11.72, 7.4, "call", "buy"),
    (21750, 20.05, 50*1, 11.19, 7.4, "put", "buy"),
]

current_price = 22147  # Current price of the Nifty 50 index
expected_price = current_price - 100  # Expected price at expiration
interest_rate = 7.087  # Risk-free interest rate (in percent)


# Calculate and print the strategy PnL

pnl = calculate_strategy_pnl(options, current_price, expected_price, interest_rate)
print(f"Strategy PnL: {pnl:.2f}")
```

# Plot the strategy PnL
```
plot_strategy_pnl_with_labels(options, current_price, interest_rate, price_range=(21700, 22600), step=100)` 
```

## Contributing

We welcome contributions from the community! If you're interested in improving Option Strategy Builder, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or fix.
3.  Implement your changes.
4.  Submit a pull request.

Please ensure your code adheres to the existing style and includes appropriate tests. Contributions should be made under the same license as the project.

## Support

If Option Strategy Builder has been a valuable tool in your trading arsenal, please consider showing your support with a donation. Your contributions directly help in maintaining and improving the project. Whether big or small, every donation is deeply appreciated and makes a real difference.

**Here's how you can contribute:**

-   **PayPal**: https://www.paypal.com/paypalme/optionstretegybuilde

Your generosity supports the journey of continuous development and enhancement of Option Strategy Builder, ensuring it stays free, accessible, and beneficial to all. Thank you for considering a donation!

## License

Option Strategy Builder is open-source software licensed under the MIT license. See the LICENSE file for more details.
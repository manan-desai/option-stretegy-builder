import mibian
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

def calculate_strategy_pnl(options, current_price, expected_price, interest_rate=7.087):
    total_pnl = 0

    for strike_price, premium, quantity,volatility,days_to_expiration, option_type, trade_direction in options:
        if option_type.lower() == 'call':
            bs_current = mibian.BS([current_price, strike_price, interest_rate, days_to_expiration], volatility=volatility)
            bs_expected = mibian.BS([expected_price, strike_price, interest_rate, days_to_expiration], volatility=volatility)
            pnl_per_contract = (bs_expected.callPrice - premium) if trade_direction.lower() == 'buy' else (premium - bs_expected.callPrice)
        elif option_type.lower() == 'put':
            bs_current = mibian.BS([current_price, strike_price, interest_rate, days_to_expiration], volatility=volatility)
            bs_expected = mibian.BS([expected_price, strike_price, interest_rate, days_to_expiration], volatility=volatility)
            pnl_per_contract = (bs_expected.putPrice - premium) if trade_direction.lower() == 'buy' else (premium - bs_expected.putPrice)
        else:
            raise ValueError("Invalid option type. Please use 'call' or 'put'.")

        total_pnl += pnl_per_contract * quantity

    return total_pnl

def calculate_hours_to_expiration(expiration_datetime_value,ist):
    current_datetime = datetime.now(ist) + timedelta(hours=1)
    expiration_datetime = expiration_datetime_value.replace(tzinfo=ist)
    time_delta = expiration_datetime - current_datetime
    total_seconds_remaining = time_delta.total_seconds()
    hours_remaining = total_seconds_remaining / (3600 * 24)
    
    return hours_remaining

def plot_strategy_pnl_with_labels(options, current_price, interest_rate, price_range, step=100):

    
    expected_prices = np.arange(price_range[0], price_range[1] + step, step)

    
    pnls = [calculate_strategy_pnl(options, current_price, price, interest_rate) for price in expected_prices]

    
    plt.figure(figsize=(10, 6))
    plt.plot(expected_prices, pnls, marker='o', linestyle='-', color='blue')

    
    for i, price in enumerate(expected_prices):
        plt.annotate(f"{pnls[i]:.2f}",  
                     (price, pnls[i]),
                     textcoords="offset points",  
                     xytext=(0,-20),  
                     ha='center')  

    plt.title('Strategy PnL across Different Expected Prices')
    plt.xlabel('Expected Price of Underlying Asset')
    plt.ylabel('Expected PnL')
    plt.grid(True)
    plt.axhline(0, color='black', lw=2)  
    plt.axvline(current_price, color='red', linestyle='--', label='Current Price')  
    plt.legend()
    plt.show()



from option_stretegy_builder import calculate_strategy_pnl,plot_strategy_pnl_with_labels

options = [
        # (strike_price,premium, qty, IV,time to expity in day, call or put, buy or sell),
          (22650,18.50, 50*1, 11.72, 7.4, "call", "buy"),
          (21750, 20.05, 50*1, 11.19, 7.4, "put", "buy"),
          ]
current_price = 22147  # Current price of the Nifty 50 index
expected_price = current_price - 100  # Expected price of the Nifty 50 index at expiration
interest_rate = 7.087  # Risk-free interest rate (in percent)

print(calculate_strategy_pnl(options,current_price,expected_price,interest_rate)) # returns 203.0516646234878 pnl



price_range = (21700, 22600)  

plot_strategy_pnl_with_labels(options, current_price, 7.087, price_range,step=100)
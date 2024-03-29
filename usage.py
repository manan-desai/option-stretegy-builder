from option_stretegy_builder import calculate_strategy_pnl,plot_strategy_pnl_with_labels

options = [
        # (strike_price,premium, qty, IV,time to expity in day, call or put, buy or sell),
          (22650,40, 50*1, 11.72, 0.1, "call", "sell"),
          (22750, 12, 50*1, 11.19, 0.1, "call", "buy"),
        #     (21450,40, 50*1, 11.72, 0.1, "put", "sell"),
        #   (21350, 12, 50*1, 11.19, 0.1, "put", "buy"),
          ]
current_price = 22000 # Current price of the Nifty 50 index
expected_price = current_price   # Expected price of the Nifty 50 index at expiration
interest_rate = 7.087  # Risk-free interest rate (in percent)

print(calculate_strategy_pnl(options,current_price,expected_price,interest_rate)) # returns 203.0516646234878 pnl



price_range = (21000, 24000)  

plot_strategy_pnl_with_labels(options, current_price, 7.087, price_range,step=500)
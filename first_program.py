from vnstock import Trading
trading = Trading(source='KBS')

trading.price_board(['MBB'])

# print the price board
print(trading.price_board(['MBB']))
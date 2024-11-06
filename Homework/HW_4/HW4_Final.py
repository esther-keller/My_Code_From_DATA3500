import numpy as np
prices = [round(float(price), 2) for price in open("/home/ubuntu/environment/Homework/HW_4/TSLA2.txt").readlines()]
#print(prices)

i = 0
buy = 0
first_buy = 0
total_profit = 0

for price in prices:   
    current_price = price
    if i > 4:
        avg_price = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
        avg_price = round(avg_price, 2)
        #print("counter:", i)
    
        #print("Moving Average Price: $",avg_price)
        if current_price < avg_price * .98 and buy == 0:
            buy = current_price
            if first_buy == 0:
                first_buy += buy
            print("Buying at:",buy)
        elif current_price > avg_price * 1.02 and buy != 0:
            print("Selling at:", current_price)
            total_profit += current_price - buy
            trade_profit = current_price - buy
            trade_profit = round(trade_profit, 2)
            print("Trade profit:", trade_profit)
            buy = 0
    i += 1

print("----------")
print("Total trade profit:", round(total_profit,2))
print("First Buy:", first_buy)
final_profit_percentage = ( total_profit / first_buy ) * 100
print("% profit:", round(final_profit_percentage,2))

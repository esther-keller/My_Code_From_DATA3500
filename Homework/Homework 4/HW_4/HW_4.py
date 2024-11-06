import numpy as np
prices = [round(float(price), 2) for price in open("/home/ubuntu/environment/Homework/HW_4/TSLA2.txt").readlines()]

for price in prices:
    print(price)

# i = 0
# buy = 0
# sell = 0
# day_one_price = 0

# for price in prices:
#     if price == prices[0]:
#         day_one_price += price
#         print(f"Day one price: ${day_one_price}")
#     else:
#         print()
#         if i > 4: 
#             five_day_avg = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-4]) / 5
#             five_day_avg = round(five_day_avg, 2)
#             print(f"Current Price: ${prices[i]}")
#             print(f"5 Day Average: ${five_day_avg}")
#             print("counter:", i)
#             i += 1
#             if i <= 251:
#                 if prices[i] < (five_day_avg * .98): #buy
#                     # buy = (five_day_avg * .98)
#                     # buy = round(buy, 2)
#                     buy += prices[i]
#                     print(f"Buying at: ${price[i]}")
#                     #total_profit -= buy  #may create an issue
#                     # update buy variable
#                     # update frst_buy variable if this is the first time you buy
#                     print()
                
#                 elif prices[i] > (five_day_avg * 1.02): #sell
#                     # sell = (five_day_avg * 1.02)
#                     # sell = round(sell, 2)
#                     sell += prices[i]
#                     print(f"Selling at: ${price[i]}")
#                     # profit = sell - buy
#                     # profit = round(profit, 2)
#                     # print(f"Profit: ${profit}")
#                      #total_profit += sell
#                     print()
#                     #calculate profit of this induvidual trade
#                     #keep a running total of all profit
#                 else:
#                     print()#do nothing this iteration
#                     pass
#         else: 
#             i += 1 
#             pass 

# print()
# total_profit = sell - buy
# total_profit = round(total_profit, 2)
# print(f"Total Profit: ${total_profit}")
# percent_return = (total_profit / first_buy) * 100
# percent_return = round(percent_return, 2)    
# print(f"% return: {percent_return}%")












'''
Loop through all the prices, calculating a 5 day moving 
average each time. 

Each iteration of the loop should update the current_price
(the newest line), and the 5 day moving average (the average 
of the previous 5 days).

Add an if statement which checks to see if the current price
is below the 5 day moving average * .98.  If it is, “buy” the
stock, meaning keep track of the price you bought at.  Update
a variable called “buy” with the buy price.

Add an elif statement along with the if statement which c
hecks to see if the current price is above the 5 day moving
average * 1.02.  If it is, “sell” the stock, meaning calculate
the profit of that trade: sell - buy.  You want to buy low and
sell high, so sell - buy is hopefully positive.

Add an else statement along with the if else if which does not
buy or sell.

Keep track of the first price you buy.

Keep track of the profit each time you sell.  Print out the 
profit for each trade.  Keep a running total of profit from 
all trades.

After the loop is complete, calculate the final_profit_percentage
and print it to the console:
'''



# # total_profit = round(total_profit, 2)

# #     elif prices[i] > (five_day_avg * 1.02): #sell
# #         sell = (five_day_avg * 1.02)
# #         sell = round(sell, 2)
# #         print(f"Selling at: ${sell}")
# #         # profit = sell - buy
# #         # profit = round(profit, 2)
# #         # total_profit += sell
# #         # print(f"Profit: ${profit}")
        
# #         #calculate profit of this induvidual trade
# #         #keep a running total of all profit
    
# #     else: #do nothing this iteration
# #         pass
        
# #     #print() #seperate lines so it's easier to read
    
# # #final profit percentage
# # percent_return = (total_profit / first_buy) * 100
# # percent_return = round(percent_return, 2)

# # print(f"Total Profit: ${total_profit}")
# # print(f"% return: {percent_return}")









# file = open("/home/ubuntu/environment/Homework/HW_4/TSLA.txt")
# lines = file.readlines()
# #print(lines)
# # array = np.array(file.readlines())
# file.close()


# #create a new list to store float values
# prices = []
# for line in lines:
#     line = float(line)
#     prices.append(line)
# #print(prices)
"""
Programming Activity 5

1. Download one year worth of stock data from yahoo finance. 
The instructions to do this are in the HW4 description.
2. After you have one year worth of stock data, use a for loop to 
iterate through the data, and calculate the average for the entire 
data set.
3. After you have calculated the average for the entire data set, see 
if you can calculate the average for the first 5 days only.  
(you will need this logic for your homework).
"""

file = open("/home/ubuntu/environment/Programming_Activities/AAPL.txt")
print(file)

lines = file.readlines()
print("lines:", lines)

prices = []

for line in lines:
    prices.append(float(line))

def average_list(lines):
    return sum(lines) / len(lines)
    
print(average_list(prices))



"""
Programming Activity 5.2 
This activity is a continuation from the last one and is meant to help 
you with your homwork.
Write a Python program to read in the stock prices from a file, into a 
list.
Create a list of floats from the list of strings you read in, from step 2.
Calculate the average of the first 4 days in your list.
Calculate the average of the last 4 days in your list.
In a for loop, calculate a 4 day moving average for the floats in the list.
Add logic in the for loop to implement a simple moving average 
trading strategy.
Display the profit from the strategy, after the for loop has finished.
"""
print()
print()

# print(prices)

i = 0

for price in prices:
    if i >= 3:
        avg = (prices[i] + prices[i+1] + prices[i+2] + prices[i+3]) /4
    i += 1
    print(avg)
    

#Programming Activity 1
 #1. make a variable called apple_price (set it to whatever you want)
 #2. make a variable called number_purchased (set it to whatever you want)
 #3. make a variable called tax and set it equal to 1.07
 #4. make a variable, total_bill and calculate it by: total_bill = apple_price * number_purchased * tax
 #5. print clearly and cleanly how many apples were purchased and the total_bill
 #6. add a check before the final print statement to see if total_bill is equal to 0.  If so, print a message to the user to check their inputs.

#set up variables
apple_price = 1
number_purchased = 100
tax = 1.07
#calculate results
total_bill = apple_price * number_purchased * tax

while True:
 if total_bill == 0: 
  print("Error. Please check all inputs and try again.")
 else:
  print("Number of apples purchased:", number_purchased)
  print("Total bill is:", round(total_bill, 3))
  break
 
 
 # WHAT DOES THIS CODE DO? Create the variables x = 2 and y = 3, then determine what each of the following statements displays:

x = 2
y = 3

print('x =', x)
# x = 2
print('Value of', x, '+', x, 'is', (x + x))
# Value of 2 + 2 is 4
print('x =')
# x = 4
print((x + y), 'x =', (y + x))
# 5 x = 5
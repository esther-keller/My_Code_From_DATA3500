'''
get user input and change it into an integer
seperate digets into induvidual numbers 



'''



while True:
    number = input("Please enter a 7-10 digit number.")
    ui = len(number)
    if ui == 7:
        num = int(number)
        print((num%10000000)//1000000)
        print((num%1000000)//100000)
        print((num%100000)//10000)
        print((num%10000)//1000)
        print((num%1000)//100)
        print((num%100)//10)
        print(num%10)
        break
    elif ui == 8:
        num = int(number)
        print((num%100000000)//10000000)
        print((num%10000000)//1000000)
        print((num%1000000)//100000)
        print((num%100000)//10000)
        print((num%10000)//1000)
        print((num%1000)//100)
        print((num%100)//10)
        print(num%10)
        break
    elif ui == 9:
        num = int(number)
        print((num%1000000000)//100000000)
        print((num%100000000)//10000000)
        print((num%10000000)//1000000)
        print((num%1000000)//100000)
        print((num%100000)//10000)
        print((num%10000)//1000)
        print((num%1000)//100)
        print((num%100)//10)
        print(num%10)
        break
    elif ui == 10:
        num = int(number)
        print((num%10000000000)//1000000000)
        print((num%1000000000)//100000000)
        print((num%100000000)//10000000)
        print((num%10000000)//1000000)
        print((num%1000000)//100000)
        print((num%100000)//10000)
        print((num%10000)//1000)
        print((num%1000)//100)
        print((num%100)//10)
        print(num%10)
        break
    else:
        print('Error. Please enter a 7-10 digit number.')    





        
# num = int(number)

# print((num%10000000000)//1000000000)
# print((num%1000000000)//100000000)
# print((num%100000000)//10000000)
# print((num%10000000)//1000000)
# print((num%1000000)//100000)
# print((num%100000)//10000)
# print((num%10000)//1000)
# print((num%1000)//100)
# print((num%100)//10)
# print(num%10)
#print((num%100)//10)
















#print(type(user_input))
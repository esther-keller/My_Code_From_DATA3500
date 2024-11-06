while True:

    ui = input("Please input a 5 digit number.")
    if len(ui) != 5:
        print("Error. Please try again.")
    else:
        pass

    ui = int(ui)

# print(ui // 100000)
# print(ui % 1)
# print(ui)

    if (ui // 10000) == (ui % 10) and (ui // 100000) == (ui % 1):
        print("Palindrome!")
        stop = input("Would you like to continue? Please input y for yes or n for no.")
        if stop == 'y':
            break
        else:
            pass
    else:
        print("Yikes. Not a Palindrome.")
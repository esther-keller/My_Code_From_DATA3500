# #my_list = [item for iterable in iterable if optional]


# # lst = []

# # text = "hello world"
# # letters_sorted = []
# # for letter in text:
# #     if letter != " ":
# #         letters_sorted.append(letter)

# # letters_sorted.sort()
# # print(letters_sorted)

# # print()

# # let_sort = sorted([letter for letter in text if letter != " "])
# # print(let_sort)



# #mixed data
# mixed = [10,3.5,"yee-haw", 'yarn', 7, False, 6]
# #isinstance(variable, type)
# # monday = True
# # print(isinstance(monday,bool))

# squares = [integer**2 for integer in mixed if isinstance(integer,int)]
# print(squares)



# #palindrome
# words = ["level", 'python', 'madam', 'civic', 'data', 'racecar']
# #return a list with just the palindromes with lst comprehension
# pal = [word for word in words if word == word[::-1]]
# print(pal)


#Programming Activity 1
numlst = range(2,101)
evennum = [num for num in numlst if num // 2]
print(evennum)
#Programming Activity 2
strings = ["   hello  ", "whitespace      ", "   :)  "]
new_list = [string.strip() for string in strings]
print(new_list)
#Programming Activity 3
name = input("Please input your name: ")
name = name.upper()
print(f"Welcome {name}!")
#Programming Activity 4
sentence = "dude, I just biked down that mountain and at first I was like Whoa and then I was like Whoa"
print(sentence)
print()
sentence = sentence.capitalize()
print(sentence)
first_whoa = False
i = 0
words = []
words = [word for word in sentence.split()]
words[0] = words[0].capitalize()
for word in words:
    if words[i].lower() == "whoa" and not first_whoa:
        words[i] = words[i].lower()
        first_woah = True
    elif words[i].lower == "whoa" and first_whoa:
        words[i] = words[i].upper()
    i += 1
print("Words:", words)
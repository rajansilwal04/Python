
"""
convert digit to integer only if sting is on digit if not print we can't convert into integer

"""

# a = "123"

# print(type(a))

# # b = a.isdigit()

# if a.isdigit():
#     c= int(a)
#     print(c)
#     print(type(c))
# else:
#     print("We can't convert")

""" Question: 132
Ask a string from user. Count how many alphabets are there in that
string.

"""
# my_string = input("Please enter a string: ")
# count = 0
# for i in my_string:
#     if i.isalpha():
#         count += 1
# print(count)

""" Question: 133
Ask a string from user. Count the number of uppercase and
lowercase characters in that String.
"""
# my_string = input("Please enter a string: ")

# uper = 0
# lower = 0

# for i in my_string:
#     if i.isupper():
#         uper = uper + 1
#     elif i.islower():
#         lower = lower + 1
        
# print(uper , lower )

# my_string = "Rajan"
# uper = 0
# lower = 0

# for i in my_string:
#     ascii = ord(i)
#     if ascii>=65 and ascii<=90:
#         uper = uper+  1
#     elif ascii>-97 and ascii<=122:
#         lower = lower + 1
# print(uper , lower )

"""Q134,134 
        Ask a string from user. Convert all the alphabets to uppercase.
"""

# my_string = input("Please enter a string: ")

# # print(my_string.upper())
# print(my_string.lower())


"""Q135
    Ask a string from user. Convert uppercase to lowercase and convert
lowercase to uppercase and don’t change the other letters.
"""
# my_string = input("Please enter a string: ")
# new_string = ""
# for i in my_string:
#     if i.isupper():
#         new_string += i.lower()
#     elif i.islower():
#         new_string += i.upper()
#     else:
#         new_string += i
# print(new_string)

"""Q136
Count the number of spaces in a string entered by user.
"""
# my_string = input("Please enter a string: ")
# count = 0

# for i in my_string:
#     if i.isspace():
#         count += 1
# print(count)

"""Q137
Ask a string from user. Print the count of how many alphabets, digits,
spaces and symbols (everything else) are there in that string.
"""
# my_string = input("Please enter a string: ")

# alphabets = 0
# digit_count = 0
# spaces = 0
# symbol_count = 0

# for i in my_string:
#     if i.isalpha():
#         alphabets += 1
#     elif i.isdigit():
#         digit_count += 1
#     elif i.isspace():
#         spaces += 1
#     else:
#         symbol_count += 1
# print(f"alphabets is {alphabets} Digit is {digit_count} Symbols is {symbol_count} and spaces are {spaces}")




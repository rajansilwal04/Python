"""Question: 138
Write a program to reverse the order of words
"""

# my_string = "Good idea to put in a ticket to have that corrected"

# word= my_string.split()
# # result = word[::-1]
# print(" ".join(word[::-1]))


"""Question: 139
Write a program that accepts a string and capitalizes the first letter
of each word while converting all other letters to lowercase.
"""
# my_sting = input("Please enter a string: ")

# print("".join(my_sting.title()))

"""Question: 140
Write a program that reverses each word in a sentence while
maintaining the word order. For example, "Hello World" should become
"""

# my_sting = input("Please enter a string: ")

# word = my_sting.split()
# print([i[::-1] for i in word])


"""Question: 141
Write a program that converts a string in camelCase to snake_case.
For example, converting "helloWorldHowAreYou" should result in
"hello_world_how_are_you"
"""
# my_string = "helloWorldHowAreYou"

# result = []

# for i in my_string:
#     if i.isupper():
#         result.append('_')
#         result.append(i.lower())
#     else:
#         result.append(i)
# print("".join(result))
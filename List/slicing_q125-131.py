"""Q125. 
    Write a python program to reverse a list using slicing
"""

# my_list = [51, 100,85,1748,51,44,66, 68]


# result = [my_list[::-1]]
# print(result)


"""Q126 
Write a python program to get every third element from a list using
slicing
"""
# my_list = [51, 100,85,1748,51,44,66, 68]
# result = [my_list[ : : 3]]
# print(result)

"""Q127
Implement a python program to split a list into two equal parts using
slicing. One list should contain 1st half and another list should contain 2nd
half
"""
# my_list = [51, 100,85,1748,51,44,66, 68]

# first = [my_list[ : len(my_list)//2 ]]
# second = [my_list[len(my_list)//2 : ]]

# print("Firs half: ",first, "\n", "Second half is:",second)



"""Q128
Q128. Implement a python program to get the last 'n' elements from a list
using slicing.

"""
# my_list = [51, 100,85,1748,51,44,66, 68]
# num= int(input("Number : "))

# print(my_list[len(my_list)-num: :])

"""Q129. 
Ask ‘n’ from user. Create a list of last n elements but in reverse order
using slicing.
"""
# my_list = [51, 100,85,1748,51,44,66, 68]
# num= int(input("Number : "))
# result = my_list[len(my_list)-num: :]
# print(result[ : : -1])

"""Q131. 
Ask ‘n’ from user. Create a list of first n elements but in reverse order
using slicing.
"""
# my_list = [51, 100,85,1748,51,44,66, 68]
# num= int(input("Number : "))
# result = my_list[ : num]
# print(result[: : -1])

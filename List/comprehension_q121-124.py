
"""Question: 121. 
Generate a list of squares of numbers from 1 to 10 using list comprehension.
"""

# my_list = [i*i for i in range(1,11) ]
# print(my_list)


"""Q122. Given a list of strings, create a new list containing the lengths of each string using list comprehension.
[4, 6, 0, 6]
"""

# my_list = ["done", "python", "", "ok bye"]

# result = [len(i) for i in my_list]
# print(result)

"""
Q123. Generate a list of strings where each string repeats itself three times, using list comprehension.

"""

# my_list = ["a", "b", "c", "d"]

# result = [i*3 for i in my_list]
# print(result)

"""Q124. Generate a list of list using list comprehension where format should be 
[[1, 'ODD'], [2, 'EVEN'], [3, 'ODD'], [4, 'EVEN']]
"""
# my_list = [f"{i} ODD" if i%2!=0 else f"{i} EVEN" for i in range(1,5)]
# print(my_list)

# my_list = [[i, "ODD"] if i % 2 != 0 else [i, "EVEN"] for i in range(1, 5)]
# print(my_list)

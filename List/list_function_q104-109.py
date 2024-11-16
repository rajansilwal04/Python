""" Question: 104
    Write a program that prompts the user to specify the length of a list
    and then requests numbers to populate that list. Display the final list as
    the output: 
    Input the length of a list: 3
 Enter number : 45
 Enter number : 22
 Enter number : 31
Out put:  [45, 22, 31]
"""

# number= int (input("Input the length of a list: "))
# answer = []
# for i in range(0, number):
#     number1 = int (input(" Enter number : "))
#     answer.append(number1)
# print("Output: ",answer)

""" Question: 105
    Create a list and prompt the user for an 'old number' followed by a
    'new number.' If the 'old number' exists in the list, replace it with the 'new
    number' provided by the user
    
Enter the old number: 51
Enter the new number: 52
Updated list is  [52, 85, 1748, 52, 44, 100, 200]
"""

# my_list = [51, 85,1748,51,44,100,200]

# old= int(input(" Enter the old number: "))
# new = int(input(" Enter the new number: "))

# for i in range(0, len(my_list)):
#     if my_list[i] == old:
#         my_list[i] = new

# print("Updated list is ", my_list)

""" Question: 106
    Remove all the even numbers from the list.
    
    [45, 11, 11]
"""
# my_list = [51, 100,85,1748,51,44,66, 68]
# odd_list = [ ]
# for i in my_list:
#     if i%2 != 0:
#         odd_list.append(i)
# print(odd_list)

""" in reverse order
my_list = [45,66,66,66,66,78,11,11,12,12,12]
for i in range(len(my_list)-1,-1,-1):
    if my_list[i] % 2 == 0:
        my_list.pop(i)

    # if my_list[i] %2 == 0:
    #     my_list.pop(i)
print(my_list)
"""


""" Question: 107
    Ask the user for a number. Then, from a list of numbers, remove all
the numbers that can be divided by the number the user entered.

Enter a number: 2
[51, 85, 51, 66, 31]
"""
# my_list = [51, 100,85,1748,51,44,66, 68,31]
# num= int(input("Enter a number: "))

# for i in my_list:
#     if i% num ==0:
#         my_list.remove(i)
# print(my_list)

""" Question: 108
    Generate a list of at least 10 numbers. Then, create two separate
lists called 'odd' and 'even.' Put all the odd numbers from the original list
into the 'odd' list, and all the even numbers into the 'even' list
ODD number:  [51, 85, 51, -67, 31]
Even number  [100, 1748, 44, 66]
"""
# my_list = [51, 100,85,1748,51,44,66, -67,31]
# odd =[ ]
# even = [ ]
# for i in range(0, len(my_list)):
#     if my_list[i]%2 == 0:
#         even.append(my_list[i])
#     else:
#         odd.append(my_list[i])
# print("ODD number: ", odd)
# print("Even number ", even)

""" Question: 109
    Start by creating two separate lists with random numbers. Then,
create a third list that merges the numbers from the first and second lists
together.

[51, 85, 51, -67, 31, 100, 1748, 44, 66]
"""


# list1= [51, 85, 51, -67, 31]
# list2 = [100, 1748, 44, 66]
# mergedlist = []
# for i in range (0,len(list1)):
#     mergedlist.append(list1[i])

# for i in range (0,len(list2)):
#     mergedlist.append(list2[i]) 
# print(mergedlist)

## simple way
# list1= [51, 85, 51, -67, 31]
# list2 = [100, 1748, 44, 66]
# mergetlist = list1 + list2

# print(mergetlist)
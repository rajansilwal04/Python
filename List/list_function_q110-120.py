""" Question: 110
    Make a list of your own. And remove all the duplicates element from
that list.
O/p:
[44, 51, 100, 85, 1748, 66, 31, -67]
"""

# my_list = [44,51, 100,85,1748,66,51,44,66,31, -67,31,31]
# result = []
# for i in my_list:
#     if i not in result:
#         result.append(i)
#         print(result)

""" Question: 111
Make a list. Then ask a number from user. If number exists in that list
then print the position of the element else print -1
O/P:
Please enter a number: 100
2
Please enter a number: 100000
-1
"""
# my_list = [44,51, 100,85,1748,66,51,44,66,31, -67,31,31]
# num = int(input("Please enter a number: "))

# if num in my_list:
#     index=my_list.index(num)
#     print(index)
# else:
#     print(-1)

""" Question: 112
Take 10 integer inputs from user and store them in a list. Now, copy
all the elements in another list but in reverse order.
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
My original list is :  [1, 2, 3, 4]
my reverse list is:  [4, 3, 2, 1]
"""
# my_list = [ ]
# result = []
# for i in range(4):
#     num = int(input("Enter a number: "))
#     my_list.append(num)
# print("My original list is : ",my_list)

# for i in range( len(my_list)-1,-1,-1 ):
#     result.append(my_list[i])
# print("my reverse list is: ",result)

""" Question: 113
Write a program to find the average of all the numbers present in the
list.
"""
# my_list = [1, 2, 3, 4]
# average = 0
# sum =0
# for i in range(len(my_list)):
#     sum += my_list[i]
#     average = sum/len(my_list)
# print(average, sum)
    

""" Question: 114
Write a Python code to find the occurrence of each element in a list
and print the element with the highest occurrence
O/P:
Higest occuence number is 4 times and highest_occurrence_element is 66 
"""    
# # my_list = [5, 6, 6, 6, 6, 78, 11, 11, 12, 12, 12]
# my_list= [1,2,33,4,1,33,33,22,22,22,22,22]
# # num = 0
# for i in my_list:
#     y= my_list.count(i)
#     # num += 1
#     print(y, end= " ")
    
# x =[y]
# largest = 0
# occurrences = 0
# for j in x:
#     if j> largest:
#         largest = j
#         occurrences = i
# print(f"\n largest number :{largest} higest_occ_eleemt : {occurrences}")

""" this is a right way to do:
my_list = [45, 66, 66, 66, 66, 78, 11, 11, 12, 12, 12]
result = [ ]

for i in my_list:
    if i not in result:
        result.append(i)
# print(result)

highest_occurrence =0
highest_occurrence_element = 0

for i in result:
    y = my_list.count(i)
    
    if y > highest_occurrence:
        highest_occurrence = y
        highest_occurrence_element = i
print(f"Higest occuence number is {highest_occurrence} times and highest_occurrence_element is {highest_occurrence_element} ")
"""


""" Question: 115
Write a program that has two lists and make a new list that contains
only the common elements between them without duplicates.
O/P:
[5, 6, 7, 8, 9, 10]
""" 
# my_list1 = [1,2,3,4,5,5,6,7,8,9,10]
# my_list2 = [5,6,7,8,9,10,11,12,13,14]
# result = [ ]
# final = [ ]
# my_list3 = my_list1 + my_list2
# # print(my_list3)

# for i in my_list3:
#     y = my_list3.count(i)
#         # result.append(i)
#     if y>1:
#         result.append(i)

# for i in result:
#     if i not in final:
#         final.append(i) 
# print(final)

""" this is a right way to do:

my_list1 = [1,2,3,4,5,5,6,7,8,9,10]
my_list2 = [5,6,7,8,9,10,11,12,13,14]

result = [ ]

for i in my_list1:
    if i in my_list2:
        if i not in result:
            result.append(i)
print(result)

"""

""" Question: 116
Write a Python code to find the second largest element in a list
without sorting
O/P:
[99.5]
""" 

# my_list = [45,11, 99,66, 99.5,78,100]
# largest = float("-infinity")
# lowest_largest = float("-infinity")

# for i in my_list:
#     if i >largest:
#         lowest_largest = largest
#         largest = i
#     elif i > lowest_largest and i< largest:
#         lowest_largest =i
# print(lowest_largest)
        
"""Q117. Make a program that takes a list of integers and returns the product of all the elements.
o/p:
13340580
"""
# my_list = [41,87,85,44]
# product = 1
# for i in my_list:
#     product= i*product
# print(product)

"""Q118. Write a program to find and print all prime numbers within a given list.
o/p:
2 3 5 7 11 13
"""

# my_list = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]


# for i in my_list:
#     factor= 0
#     for j in range(1,i+1):
#         if i%j ==0:
#             factor +=1
#     if factor == 2:
#         print(i, end=" ")

"""Question: 119 
    Write a program to split a given list into two halves. 
    o/p:
    [2, 3, 4, 5, 6, 7, 8]
    [9, 10, 11, 12, 13, 14, 15]
"""
# my_list = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# my_first = [ ]
# my_second = [ ]

# y= len(my_list)//2
    
# for j in range(0,y):
#     my_first.append(my_list[j])
# for k in range(y,len(my_list)):
#     my_second.append(my_list[k])
# print(my_first)
# print(my_second)

"""Q120. Write a program that swaps the first and last elements of a given list.

"""
# my_list = [ 32,10, "rajan", 55.9, "xyz"]

# last_list = my_list[-1]
# first_list = my_list[0]

# my_list[0]= last_list
# my_list[-1]= first_list

# print(my_list)


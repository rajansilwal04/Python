"""Q142
Ask subject name and marks from the user and keep adding it to
dictionary.
"""

# numbers = int (input("Please enter the number of subjects :"))
# my_dictionary ={}
# for i in range (numbers):
#     subject = input("Please Enter the subject name: ")
#     mask = input(f"Please enter the mask for {subject}: ")
#     my_dictionary.update({subject:mask})

# print(my_dictionary)


"""Queston: 143
Convert two lists into a dictionary. Make two list on your own of
same length, and convert them to dictionary
"""

# my_key= ["name", "last_name", "age", "gender"]
# my_value= ["Rajan", "Silwal", 60, "male"]
# my_dictionary = {}

# for i in range(0,len(my_key)):
#     my_dictionary.update({my_key[i]:my_value[i]})
    
# print(my_dictionary)
# print(type(my_dictionary))

"""Queston: 144
Write a Python program to sum all the items in a dictionary.
"""
# my_mask ={"math": 99, "Science": 60, "English": 72, "Social": 80}
# total = 0

# for i in my_mask:
#     total += my_mask[i]
# print(total)


"""Queston: 145
Write a Python program to multiply all the items in a dictionary.
"""

# my_mask ={"math": 99, "Science": 60, "English": 72, "Social": 80}
# total = 1

# for i in my_mask:
#     total *= my_mask[i]
# print(total)

"""Question: 146
        Ask a string from user. Display the dictionary where each key is a
        character and value is the frequency of that character that comes in that
        string
"""

# my_string = "hello world"

# my_dictionary = {}

# for i in my_string:
#     if i in my_dictionary:
#         my_dictionary[i] += 1
#     else:
#         my_dictionary[i] = 1
# print(my_dictionary)
"""
# for i in range(0, len(my_string)):
#     count = my_string[i].count(i)
#     my_dictionary.update({my_string[i]:i})
#     # print(i, my_string[i])
# print(my_dictionary)

# for i in my_string:
#     if i is not my_dictionary:
#         my_dictionary.update({i:count})
#     else:
#         my_dictionary[i] +=  1
# # for i in range(0, len(my_string)):
# #     if my_string[i] is not my_dictionary:
# #         my_dictionary.update({my_string[i]:count}) 
# #         # count += 1
# # # print(my_dictionary)
#     # else:
#     #     my_string[i] + = 1
# print(my_dictionary)
"""

"""Question: 147
Store “name” of a student as Key, “list of 5 marks” of that student as
a Value. Store atleast 5 student names. Print the sum and percentage of all
the students
"""
student_dic = {"student": [85,90,78,92,88], "student2": [85,79,89,77]}

for name,mask in student_dic.items():
    print(f"{name}",sum(mask), "Percentage is : ", sum(mask)/5)
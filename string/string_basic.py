
""""
String is immutable as well
"""
my_string = "rajan silwal"
# print(type(my_string))
# print(my_string)
# # print(my_string[1])
# # for i in my_string: print(i)

# print(my_string[-1], end=" ")

# my_list = [i for i in my_string]
# print(my_list, end=" ")
count = 0
for i in range(len(my_string)-1,-1,-1):
    count += 1
    print(f"alpabhate: {my_string[i]}", count)
print(my_string[ : : -1])

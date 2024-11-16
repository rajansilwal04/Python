


"""
Basic implementation for tuples
"""
my_tuple = (20,30,40,50)

print(my_tuple, type(my_tuple))
print(my_tuple[0])
# my_tuple[1] = 100

# print(my_tuple[1]) //TypeError: 'tuple' object does not support item assignment

# for i in my_tuple:
#     print(i)


my_list = list(my_tuple)
print(my_list)
my_list.append(100)

my_tuple1 = tuple(my_list)
print(my_tuple)

print(my_tuple1)
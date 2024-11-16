

# x ={"name ": "Rajan", "lastname": "Silwal", "gender":"male", "age": 20, "mask": [50,60,70]}

# result = x.split()
# print(x)

"""
Get, add, update, delete
"""

### GET:

# my_dict = {"name": "Rajan", "lastname": "Silwal", "gender":"male", "age": 20, "mask": [50,60,70]} 

# # print(my_dict["name"])
# # print(my_dict.get("lastname "))

# k = input("Enter a key :")
# # result = my_dict.get(k)
# if k in my_dict:
#     print(my_dict.get(k))
# else:
#     print("Please enter a correct key!!")


### ADD:

# my_dict = {"name": "Rajan", "lastname": "Silwal", "gender":"male", "age": 20, "mask": [50,60,70]} 
# print(my_dict)

# # add methods:
# # my_dict["age"]= 100
# # my_dict["zone"] = "a"
# # print(my_dict)

# ## Advnce way to update:

# my_dict.update({"name":"xyz"})
# print(my_dict)

### Remove methods:
my_dict = {"name": "Rajan", "lastname": "Silwal", "gender":"male", "age": 20, "mask": [50,60,70]} 

print(my_dict)

# del my_dict["lastname"]
my_dict.pop("name")
print(my_dict)

my_dict.popitem()
print(my_dict)

my_dict.popitem()
print(my_dict)

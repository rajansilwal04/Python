

# my_string = "My name is Rajan Silwal"

# print(my_string.count("a")) # 4 times
# print(my_string.count("na")) # 1 times
# print(my_string.startswith("na")) # false
# print(my_string.endswith("wal")) # true
# print(my_string.index("y")) # index at 1
# print(my_string.find("z")) # index at -1 we dont have z on the string
# print(my_string.replace("a","@")) # replace a with @ -- o/p: My n@me is R@j@n Silw@l

### Strip:
"""
I/p:   My name is Rajan Silwal      
o/p:  My name is Rajan Silwal
"""
my_string = "   My name is Rajan Silwal      "

result = my_string.strip()

print(my_string)
print(result)

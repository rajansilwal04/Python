my_list = ["abc", "Rajan", "silwal",78, 90]

my_string = " ".join(str(i)[::-1] for i in my_list)

print(my_string)
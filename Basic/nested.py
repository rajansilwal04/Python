
"""
nested if else
print postive, negative or zero
"""

number=int(input("Enter any number: "))

if number >=0:
    if number ==0:
        print(f"{number} is equals to 0")
    else:
        print(f"{number} is positive")
else:
    print(f"{number} is negative")
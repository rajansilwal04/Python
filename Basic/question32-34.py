
""" Question 32:
ask number from user;
print fizz if the number is divisible by 3
print Buzz if the number is divisible by 5
print fizzbuzz if the number is divisible by 3 and 5
print none if the number  for else

"""

# number=int(input("Please enter a number: "))

# if number %3 ==0 and number % 5 == 0:
#     print(f" Number you entered {number} is fizzbuzz")
# elif number % 5 == 0:
#     print(f" Number you entered {number} is buzz")
# elif number %3 ==0:
#     print(f" Number you entered {number} is fizz")
# else:
#     print(f" Number you entered {number} is none")
    
    
""" Question 33:
Take a salary and update the salary of an employee:
1: 10000< 5% increment
2. 10000>= and 20000< 10% increment
3. 20000>= and 50000< 15% increment
4. 50000>= 20% increment
"""
# salary=int(input(" Enter the salary of a employee: "))

# inc5= salary *1.05
# inc10= salary *1.10
# inc15= salary *1.15
# inc20= salary *1.20

# if salary<10000:
#     print(f"Your updated salary is {inc5:.2f} which is 5% and your previous salary is {salary}")
# elif salary>=10000 and salary<20000:
#     print(f"Your updated salary is {inc10:.2f} which is 10% and your previous salary is {salary}")
# elif salary>=20000 and salary<50000:
#     print(f"Your updated salary is {inc15:.2f} which is 15% and your previous salary is {salary}")
# else:
#     print(f"Your updated salary is {inc20:.2f} which is 20% and your previous salary is {salary}")


""" Question 34:
Get a last digit of the number:

"""
# num = int(input("Enter any number:"))
# result= num%10

# print(f" The last digit of {num} is", result)
    
# print(f"Lets check if the last digit of {num} which is {result}, divisible by 5 or not: ")
# if result%5==0:
#     print(f" The last digit of {result} is divisible by 5")
# else:
#     print(f" The last digit of {result} is not divisible by 5")
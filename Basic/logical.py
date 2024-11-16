physic_mask=int(input("Please enter the mask you got in physics:"))
chemistry_mask=int(input("Please enter the mask you got in chemistry:"))

# if(physic_mask & chemistry_mask >= 40):
#     print("Pass")
# elif(physic_mask | chemistry_mask >= 20 & physic_mask | chemistry_mask >= 40 ):
#     print("You are eiligable for re-exam")
if(physic_mask or chemistry_mask != 19):
    print("good")
else:
    print("fail")
    
    """
    Enter age if you are above the age 18  only you are allowed, and if you are above 16 you are eligible for Driving license and if you are
    above the age 10 you are eligible for high school license and less than 10 you are kids
    
    """
    
age = int(input("Please Enter your aga: "))

if(age >=18):
    print("You are eiligable to vote")
elif(age <=18 and age >=16):
    print(f"Since you are {age} you are eligible for Drive license")
elif(age <=16 and age >=10):
    print(f"Since you are {age} you are eligible for High School license")
else:
    print(f"since you are {age} you are a kids")
    
    
    """
    Ask number from user and print if the number is odd or even
    """
number = int(input("Please enter any number: "))

if(number%2==0):
    print(f"Number you entered {number} is even")
else:
    print(f"Number you entered {number} is odd")
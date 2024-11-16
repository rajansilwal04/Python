## Question 4 Add 2 number:
one = int(input("Please enter first number: "))
two = int(input("Please enter second number: "))

print(f"The sum of the two numbers {one} and {two} is", one + two)

## Question 5 Convert int to str and str to int:
print("\n Convert to str from int")
x ="50"
y ="60"

z =int(x) + int(y)
print(f"the sum of the two numbers {x} and {y} is ", z)

print("\n Convert to int from str")
a= 50
b= 60
c= str(a) + str(b)
print(f"the sum of the two numbers {a} and {b} is ", c)

## Question 6 calculate average:

one = int(input("Please enter first number: "))
two = int(input("Please enter second number: "))
three = int(input("Please enter third number: "))
avg = float(one+two+three)/3

print(f"the average of the three numbers {one}, {two}, {three} is ", avg)


## Question 9 Convert temp to fahrenheit

fahrenheit = float(input("Please enter temp in fahrenheit: "))

celcius = float((fahrenheit-32))*5/9

print(f"the temperature of the fahrenheit is {celcius} degrees")


## Question 11 game point calculation:

game = int(input("Please enter Number of game played: "))
won = int(input("Please enter   Number of games won: "))
loss = int(input("Please enter Number of games losses: "))

game_tie = game-won-loss

print(f"Game tie: {game_tie}")

print(f"Total point of {won}: ", (won*4) + (game_tie*2))


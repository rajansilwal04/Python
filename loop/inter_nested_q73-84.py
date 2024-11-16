
""" Question: 73 Print pattern
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

"""
# for i in range (1,6):
#     for j in range (1,i+1):
#         print(j, end = " ")
#         # print(j)
#         # break
#         # print(k[j] , end =" ")
#     print()
    
    
# i = 1
# while i<=5:
#     j =1
#     while j<=i:
#         print(j, end = " ")
#         j = j + 1
#     i=i+1
#     print()
    

""" Question: 74 Print pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 

"""

# for i in range(1,6):
#     for j in range(0,i):
#         print(i, end= " ")
#     print()
    
# i =1
# while i<=5:
#     j =1
#     while j<=i:
#         print(i, end= " ")
#         j = j + 1
#     i=i+1
#     print()


"""Question 75; Print the pattern:
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 

"""

# for i in range (1,6):
#     for j in range (i, 0, -1):
#         print(j, end= " ")
#     print()
    
"""Question 76; Print the pattern:
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1

"""

# for i in range(5, 0,-1):
#     for j in range(5, i-1,-1):
#         print(j, end= " ")
#     print()
    
# i =5
# while i >= 1:
#     j =5
#     while j>= i:
#         print(j, end= " ")
#         j = j -1 
#     i = i-1
#     print()
    
"""Question 77; Print the pattern:
5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1 
"""
# i =5
# while i >=1:
#     j =5
#     while j >=i:
#         print (i, end=" ")
#         j= j-1
#     i = i -1
#     print()

"""Question 78; Print the pattern:
* 
* * 
* * * 
* * * * 
* * * * * 

"""

# for i in range(5,0,-1):
#     for j in range (6,i, -1):
#         print("*", end= " ")
#     print()

"""Question 79; Print the pattern:
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5  

"""

# i = 1
# while i <= 5:
#     j =5
#     while j >= i:
#         print(j, end= " ")
#         j = j - 1 
#     i = i + 1
#     print()

# for i in range( 1, 6):
#     for j in range (5,i-1, -1):
#         print(j, end= " ")
#     print()

"""Question 80; Print the pattern:
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 

"""

# for i in range(5,0,-1):
#     for j in range(i,0, -1):
#         print(i, end=" ")
#     print()

"""Question 81; Print the pattern:
* * * * * 
* * * * 
* * * 
* * 
* 
"""

# for i in range(0,5):
#     for j in range(5,i,-1):
#         print("*", end= " ")
#     print()

"""Question 82; Print the pattern:
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
"""

# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end= " ")
#     print()

"""Question 83; Print the pattern:
1 
2 3 
4 5 6 
7 8 9 10 
"""
# count =1
# for i in range(1, 6):
#     for j in range (i):
#         print(count, end=" ")
#         count += 1
#     print()
    
"""Question 84; Print the pattern:
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 
"""
for i in range(1,6):
    for j in range(i, 0, -1):
        print(j, end= " ")
    print()
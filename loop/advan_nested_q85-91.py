"""Question 85; Print the pattern:
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
* * * * * * 
"""
# for i in range(0, 6):
#     for j in range(i,5):
#         print(" ", end= " ")
#     # print()
    
#     for k in range(0, i+1):
#         print("*", end= " ")
#     print()

"""Question 86; Print the pattern:
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
"""
# for i in range(1,6):
#     for j in range(i,5):
#         print(" ", end= " ")
#     for k in range(1, i+1):
#         print(k, end= " ")
#     print()

"""Question 86; Print the pattern:
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
"""

# for i in range(1, 6):
#     for j in range(i,6):
#         print(" ", end= " ")
#     # print ()
    
#     for j in range(i):
#         print(i , end= " ")
#     print()



"""Question 87; Print the pattern:
        x 
      x x x 
    x x x x x 
  x x x x x x x 
x x x x x x x x x 
"""
# for i in range(1,6):
#     for j in range(5,i, -1):
#         print(" ", end=" ")
#     # print()
    
#     for k in range((i*2)-1):
#         print("x", end=" ")
#     # for m in range(i):
#     #     print("x", end=" ")
#     print()

"""Question 88; Print the pattern:
        x 
      x x x 
    x x x x x 
  x x x x x x x 
x x x x x x x x x 
"""

# for i in range(1,6):
#     for j in range(i,5):
#         print(" ", end= " ")
        
#     for k in range((i*2)-1):
#         print("*", end= " ")
    
#     print()
    

    
"""Question 89; Print the pattern:
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
"""  
    

# for i in range(1,6):
#     for j in range(i,5):
#         print(" ", end= " ")
    
#     for k in range((i*2)-1):
#         print("*", end= " ")

#     print()

# for i in range(4,0,-1):
#     for j in range(5,i,-1 ):
#         print(" ", end= " ")
    
#     for k in range((i*2)-1):
#         print("*", end= " ")
#     print()
    
    
""" Question: 90
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
"""


# for i in range (1,6):
#     for j in range(0,i):
#         print(" ", end= " ")
#     # print()
    
#     for k in range (10, (i*2)-1, -1 ): # 9(4*2+1),7(3*2+1), 5(2*2+1), 3(1*2+1), 1(0*2+1) 
#         print("*", end= " ")
#     print()
    
    
""" Question: 91
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
"""
# for i in range (1,6):
#     for j in range(0,i):
#         print(" ", end= " ")
#     # print()
    
#     for k in range (10, (i*2)-1, -1 ): # 9(4*2+1),7(3*2+1), 5(2*2+1), 3(1*2+1), 1(0*2+1) 
#         print("*", end= " ")
#     print()
    
# ## Second half   
 
# for i in range(1,5):
#     for j in range(5,i,-1):
#         print(" ", end= " ")
#     for k in range((i*2)+1): # 3(1*2+1) 5(2*2+1) 7(3*2+1) 9(4*2+1)
#         print("*", end= " ")
#     print()

""" Question: 91
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
"""


for i in range (1,6):
  for j in range (1,i+1):
    print (" ", end= " ")
  # print()
  for k in range (10, (i*2)-1,-1): #9= 10(5*2)-1, 7(4*2)-1,5,3,1
    print ("*", end= " ")
  print()
  
for i in range(1,5):
  for j in range(5,i,-1):
    print(" ", end=" ")
  # print()
  for k in range((i*2)+1): #3(1*2+1),5(2*2+1),7(3*2+1),9(4*2+1)
    print("*", end=" ")
  print()
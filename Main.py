"""
# LAB_FUNCTIONS_1


## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   

### Document the newly created function. describe what it does, then print the documentation. 
"""

def patter(Number:int):
    for i in range(Number,0,-1):
        for j in range(i,0,-1):
            if j<= Number:
                print(j,end=" ")
            else:
                Number=-1
        print(" ")

"""
def patter(Number:int):
    x=1
    
    while x<Number:
        print(x,end=" ")
        x+=1
"""


patter(5)

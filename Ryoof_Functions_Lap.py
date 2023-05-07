# LAB_FUNCTIONS_1


## Create a function that takes 1 parameter of type int , 
# then it prints out the result formatted like the following patter
# (if we give it 5 for example):

# 5 4 3 2 1   
# 4 3 2 1   
# 3 2 1   
# 2 1   
# 1   

### Document the newly created function. describe what it does, then print the documentation. 

n =int( input("Enter any number:"))
def Descending_numbers(n:int) ->int:
    '''This funtion takes one parameter of type int and return the number as an Inverted 
    hierarchical shape'''
    for i in range(0,n+1):
        for j in range(n-i,0,-1):
            print(j,end=" ")
        print('\r')
        

Descending_numbers(n)

#reading the documentation
print(Descending_numbers.__doc__)


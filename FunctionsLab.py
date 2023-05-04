'''Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter
 (if we give it 5 for example):
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

Document the newly created function. describe what it does, then print the documentation.'''


def descending (number:int):
    '''This function prints a half pyramid in descending order'''
    
    for num1 in range (number,0,-1):
        for num2 in range (num1-1,-1,-1):
            print(num2+1, end=" ")
        print("\n")
        


num = int(input('Please enter an integer positive number: '))
descending(num)
print(descending.__doc__)
def numbers (number: int) -> str:
    '''The function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1  '''
    while number > 0:
     nestedNumber = number
     while nestedNumber > 0:
        print(nestedNumber, end=" ")
        nestedNumber -= 1
     print()
     number -=1

numbers(5)

print("_____________")
print(numbers.__doc__)
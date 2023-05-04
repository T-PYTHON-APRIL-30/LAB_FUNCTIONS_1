'''LAB_FUNCTIONS_1
Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

Document the newly created function. describe what it does, then print the documentation.'''
def Printrectangle(number:int):
      
    for number in range(6,0,-1):
        print("")
        number=number-1
        for number in range(number,0,-1):
            print(number,end=" ")
Printrectangle(5)
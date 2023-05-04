'''
Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

Document the newly created function. describe what it does, then print the documentation.'''

def countDown(number_input:int):
    
    while True:
        for number in range(number_input,0,-1):
            print(number,end=" ")
        print("\n")
        number_input-=1
        if number_input == 0:
            break
        
user_input= int(input("Pleasr enter the number: "))    
countDown(user_input)

    

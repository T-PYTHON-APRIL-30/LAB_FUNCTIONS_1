'''
Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

Document the newly created function. describe what it does, then print the documentation.
'''

def desc_Numbers (number:int):
    '''This function take one parameter then prints the result in iteration descending format'''
    for i in range(number,0,-1):
        for j in range(i):
            print(i , end =" ")
            i-=1
        print()

print("")
print(desc_Numbers.__doc__)
user_input= int(input("\nEnter an integer number: "))
desc_Numbers(user_input)



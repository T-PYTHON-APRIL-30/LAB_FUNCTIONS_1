'''
# LAB_FUNCTIONS_1


## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   

### Document the newly created function. describe what it does, then print the documentation. 
'''
def toStringPatter(number : int) :
    '''print the number by decrease way and also repeat this for each line as decrease '''
    for diget in range(number, 0, -1):
        line : str = str(diget)
        for item in range(diget-1, 0, -1):
            line += f" {str(item)}"
        print(line)

toStringPatter(9)
print(toStringPatter.__doc__)

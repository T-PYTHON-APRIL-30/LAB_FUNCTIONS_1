def p_number(numbers:int):
    '''this function get an input from user and print it like decrease sort then decrease a one number and repeat'''
    c_numbers = range(numbers,0,-1)
    for n in c_numbers :
        for a in range(numbers,0,-1):
            print(n,end=" ")
            
            n-= 1
           
        print()
        n-= 1
        numbers-= 1
           

           

p_number(int(input("Enter a number! ")))
print(p_number.__doc__)

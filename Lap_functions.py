def p_number(numbers:int):
    '''Document the newly created function. describe what it does, then print the documentation'''
    c_numbers = range(numbers,0,-1)
    for n in c_numbers :
        for a in range(numbers,0,-1):
            print(n,end=" ")
            
            n-= 1
           
        print()
        n-= 1
        numbers-= 1
           

           

p_number(int(input("Enter a number! ")))


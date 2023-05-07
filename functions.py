def one_parameter (numb:int)->int:
    '''printing the numbers from 5 to 1, and removing a number each line'''
    for numb in range (numb,0,-1):
        for i in range (numb,0,-1):
            print(i,end ="")
        print()    
one_parameter(5)
print (one_parameter.__doc__)
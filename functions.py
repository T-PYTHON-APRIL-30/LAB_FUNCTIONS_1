def one_parameter (numb:int)->int:
    for numb in range (numb,0,-1):
        for i in range (numb,0,-1):
            print(i,end ="")
        print()    
one_parameter(5)            
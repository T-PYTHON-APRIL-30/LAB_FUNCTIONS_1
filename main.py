def countDown(x) -> int :
    '''This function it will prints out the result formatted ! '''
    for i in range(x,0,-1):
        for j in range(i,0,-1) :
            print(j,end=" ")
        print()
    
print(countDown.__doc__)

x = int(input("Enter a number: "))

countDown(x)
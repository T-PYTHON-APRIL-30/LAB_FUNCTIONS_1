def reversepyramid(number:int):
    '''this function will take an intger from user and then does a reverse pyramid while decreesing the number'''
    for number in range(number,0,-1):
            for j in range(number-1):
                print(number,end=" ")
                number=number-1
            print(1)



'''
for i in range(5,0,-1):
    for j in range(i-1):
        print(i,end=" ")
    print("p")

print("p")
'''
    
print(reversepyramid.__doc__)

number= int(input("please inter a number: "))
reversepyramid(number)

#for(i=0;i<5;i++)
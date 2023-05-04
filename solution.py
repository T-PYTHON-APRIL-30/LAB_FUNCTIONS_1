def rows(Number:int):
    '''
creating pettren of 5 rows as showen 
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
    '''
    for i in range(Number,0,-1):
        for j in range(i,0,-1):
            if j<= Number:
                print(j,end=" ")
            else:
                Number=-1
        print(" ")


rows(5)
print(rows.__doc__)

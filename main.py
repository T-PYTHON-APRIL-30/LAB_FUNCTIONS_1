def numbers(num1:int):
    ''' this function print numbers out the result formatted  
'''

    if num1<0:
        print("only postive number ")
    else:
      
        while num1>=1:
            num2=num1
            num1-=1

            while num2>=1:
                print(num2,end=" ")
                if num2==1:
                   print()
                num2-=1
                              
numbers(10)
print(numbers.__doc__)
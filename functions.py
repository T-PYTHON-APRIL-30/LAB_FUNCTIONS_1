num = int(input(print("enter any number: ")))
def reverse (num:int):
    '''This function executes what's inside it when called!'''
    for number1 in range(num,0,-1):
        for number2 in range(number1, 0, -1):
            print(number2, end="")
        print()
reverse(num)
print(reverse.__doc__)
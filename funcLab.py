


def reversed_print(x:int):
    '''This is a func that prints the passed arguemnt reversed'''
    for number in range(x, 0, -1):
        for number in range(number, 0, -1):
            print(number, end = " ")
        if number == 0:
            break
        print("\n")


number1 = int(input("Select a number: "))
reversed_print(number1)
print(reversed_print.__doc__)
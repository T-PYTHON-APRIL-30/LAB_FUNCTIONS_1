def print_cut(num:int):
    '''function that takes 1 parameter of type int , then it prints out the result formatted '''
    for number in range(num, 0, -1):
        for result in range(number, 0, -1):
            print(result, end=' ')
        print()
user_input= int(input("Enter your number : "))
print_cut(user_input)
print(print_cut.__doc__)



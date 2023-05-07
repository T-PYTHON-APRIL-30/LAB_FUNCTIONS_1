def series_number(num: int):
    ''' this function for print a serises of number in inverted triangle shape. '''
    for i in range(0, num + 1):
        for j in range(num - i, 0, -1):
            print(j, end = " ")
        print("\n")


print(series_number.__doc__)

while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        series_number(int(user_input))
        break
    else:
        print("type a integer number pleas!!")
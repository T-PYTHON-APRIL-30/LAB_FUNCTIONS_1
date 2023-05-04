def numbers (number: int) -> str:

    while number > 0:
     nestedNumber = number
     while nestedNumber > 0:
        print(nestedNumber, end=" ")
        nestedNumber -= 1
     print()
     number -=1

numbers(5)
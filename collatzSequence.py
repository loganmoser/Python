def collatz(number):
    if number % 2 == 0:
        evenNum = number // 2
        print(evenNum)
        return evenNum
    elif number % 2 == 1:
        oddNum = number * 3 + 1
        print(oddNum)
        return oddNum


try:
    print('please input a number')
    number = int(input())
    test = collatz(number)
    while test != 1:
        test = collatz(test)
except:
    print('You must enter an integer')

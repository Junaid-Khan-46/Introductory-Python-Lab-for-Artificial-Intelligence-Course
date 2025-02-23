def factorials(number):
    factorial = 1
    for i in range (number, 1, -1):
        factorial = factorial * i

    print ("Factorial : ", factorial)
number = int(input("Enter number for the factorial: "))
factorials(number)
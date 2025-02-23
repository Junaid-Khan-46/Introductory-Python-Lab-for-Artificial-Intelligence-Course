
import os

def Menu():
    print("!!! Welcome !!! ")
    print("Enter 1:Addition ")
    print("Enter 2:Subtraction ")
    print("Enter 3:Multiplication ")
    print("Enter 2:Division ")
    choice = int(input("Enter your choices"))
    return choice

def addition(val1, val2):
  return val1 + val2

def subtract(val1, val2):
  return val1 - val2

def Multiply(val1, val2):
  return val1 * val2

def division(val1, val2):
  return val1 / val2


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def calculation():
    val1 = int(input("Enter value: "))
    answer = val1
    while True:

        val2 = int(input("Enter value: "))
        choice = Menu()
        print(" ")
        match choice:
            case 1:
                answer = addition(answer, val2)
            case 2:
                answer = subtract(answer, val2)
            case 3:
                answer = Multiply(answer, val2)
            case 4:
                answer = division(answer, val2)
        print("Answer" , answer)
        more = input("for more calculation then write y")
        if more == 'y':

            print()
        else:
            break


calculation()
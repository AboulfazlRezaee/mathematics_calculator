#Quadratic Equation
#import package
import colorama
from colorama import Fore , Style
colorama.init(autoreset= True)
import math
print(Fore.LIGHTMAGENTA_EX + '\n\nWelcome to the Quadratic Equation Calculator.\n\n' + Fore.RESET)

print(Fore.LIGHTGREEN_EX + "We are going to Solve a Quadratic Equation in the form of:\n" + Fore.RESET)
print(Fore.LIGHTGREEN_EX + "ax^2 + bx + c = 0\n" + Fore.RESET)


def Quadratic():
        print(Fore.LIGHTCYAN_EX + "\nPlease Enter Coefficients of this equation:" + Fore.RESET)

        a = float(input(Fore.LIGHTCYAN_EX + "a = "))
        b = float(input(Fore.LIGHTCYAN_EX + "b = "))
        c = float(input(Fore.LIGHTCYAN_EX + "c = "))

        if a == 0:
            if b == 0:
                print(Fore.RED + "\nError: The Equation Can not be Solved." + Fore.RESET)
            else:
                x1 = -c/b
                print(Fore.LIGHTYELLOW_EX + "\nThis equation if of the first-order and has a real root:" + Fore.RESET)
                print(f"x = {x1 : .5f}")
        else:
            delta = b*b - 4*a*c
            if delta == 0:
                print(Fore.LIGHTYELLOW_EX + "\nThis equation has a real double root: "  + Fore.RESET)
                x1 = -b/(2*a)
                print(f"x1 = x2 = {x1 : .5f}")
            elif delta > 0:
                print(Fore.LIGHTYELLOW_EX + "\nThis equation has two distinct real roots:" + Fore.RESET)
                x1 = (-b + math.sqrt(delta))/(2*a)
                x2 = (-b - math.sqrt(delta))/(2*a)
                print(f"x1 = {x1 : .5f}")
                print(f"x1 = {x2 : .5f}")
            else:
                if b == 0:
                    print(Fore.LIGHTYELLOW_EX + "\nThis equation has two imaginary root." + Fore.RESET)
                    print(f"x1 =  {math.sqrt(-delta)/(2*a) : .5f}i")
                    print(f"x2 = -{math.sqrt(-delta)/(2*a) : .5f}i")
                else:
                    print(Fore.LIGHTYELLOW_EX + "\nThis equation has two complex root." + Fore.RESET)
                    print(f"x1 = {-b/(2*a) : .5f} + {math.sqrt(-delta)/(2*a) : .5f}i")
                    print(f"x2 = {-b/(2*a) : .5f} - {math.sqrt(-delta)/(2*a) : .5f}i")

        print(Fore.YELLOW + "\n====================================================================\n")


while True:
    Quadratic()

    choice= input(Fore.LIGHTRED_EX + "Do you want to solve another one? (y or n): ").lower()
    if choice == 'y':
        continue
    elif choice == 'n':
        print("Goodbye! Exiting the program...")
        break
    else:
        print('\t\t!!!Invalid Input!!!')
        break



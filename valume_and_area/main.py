#This program is solving Area and Volume
import math
import colorama
from colorama import Fore ,Back #Style
colorama.init(autoreset= True)


def input_char():

    print(Fore.LIGHTMAGENTA_EX + "\n\nWelcome to the Different Geometrical Volume and Area Calculator.\n\n" + Fore.RESET)

    form = input(Fore.LIGHTYELLOW_EX +"Enter a to use Area or Enter v to use Volume: ")

    if form.upper() == "A" :
        print(Fore.GREEN + "You used Area form.\n")
        Find_Different_Geometrical_Areas()
    elif form.upper() == "V" :
        print(Fore.GREEN + "You used Volume form.\n")
        Find_Different_Geometrical_Volume()
    else:
        print(Fore.MAGENTA + Back.LIGHTRED_EX + "\n.....YOU USED WRONG KEY WORD.....\n")
        print(Fore.YELLOW + "================================================================\n")


#Area program
def Find_Different_Geometrical_Areas():
    
    Pi = 3.14

    print(Fore.CYAN + "1--> " + Fore.RESET  + "Circle")
    print(Fore.CYAN + "2--> " + Fore.RESET  + "Rectangle")
    print(Fore.CYAN + "3--> " + Fore.RESET  + "Triangle")
    print(Fore.CYAN + "4--> " + Fore.RESET  + "Square")
    print(Fore.CYAN + "5--> " + Fore.RESET  + "Ellipse")
    print(Fore.CYAN + "6--> " + Fore.RESET  + "Parallelogram")
    print(Fore.CYAN + "7--> " + Fore.RESET  + "Diamond")
    print(Fore.CYAN + "8--> " + Fore.RESET  + "Trapezius")
    fig_code = int(input(Fore.CYAN + "\nEnter the Figure code: " + Fore.RESET))


    match fig_code:
        case 1:
            radius = float(input("\nEnter the radius: "))
            area = Pi * radius * radius
            print(f"Area of Circle = {area : .2f}")
            print(Fore.YELLOW + "................................\n")
        case 2:
            breadth = float(input("\nEnter the breadth: "))
            length = float(input("Enter the lenght: "))
            area = breadth * length
            print(f"Area of Rectangle = {area : .2f}")
            print(Fore.YELLOW + "................................\n")
        case 3:
            height = float(input("\nEnter the height: "))
            base = float(input("Enter the base: "))
            area = (height * base) / 2
            print(f"Area of Triangle = {area : .2f}")
            print(Fore.YELLOW + "................................\n")
        case 4:
            side = float(input("\nEnter the side: "))
            area = side * side
            print(f"Area of Square = {area : .2f}")
            print(Fore.YELLOW + "................................\n")
        case 5:
            Bdiagonal = float(input("\nEnter the Bdiagonal: "))
            Sdiagonal = float(input("Enter the Sdiagonal: "))
            area = ( Pi * Bdiagonal * Sdiagonal) / 4
            print(f"Area of Ellipse = {area : .2f}")
            print(Fore.YELLOW + "................................\n")
        case 6:
            height = float(input("\nEnter the height: "))
            base = float(input("Enter the base: "))
            area = height * base
            print(f"Area of Parallelogram = {area : .2f}")
            print(Fore.YELLOW + "................................\n")
        case 7:
            Bdiagonal = float(input("\nEnter the Bdiagonal: "))
            Sdiagonal = float(input("Enter the Sdiagonal: "))
            area = (Bdiagonal * Sdiagonal) / 2
            print(f"Area of Diamond = {area : .2f}")
            print(Fore.YELLOW + "................................\n")
        case 8:
            Bbase = float(input("\nEnter the Bbase: "))
            Sbase = float(input("Enter the Sbase: "))
            height = float(input("\nEnter the height: "))
            area = ((Bbase + Sbase) * height) / 2
            print(f"Area of Trapezius = {area : .2f}")
            print(Fore.YELLOW + "................................\n")
        case _:
            fig_code = print(Fore.MAGENTA + Back.LIGHTRED_EX + "Error in Figure code\n")
            print(Fore.YELLOW + "..................................\n")



#Volume program
def Find_Different_Geometrical_Volume():

    pi = 3.14

    print(Fore.CYAN + "1--> " + Fore.RESET  + "Sphere")
    print(Fore.CYAN + "2--> " + Fore.RESET  + "Cone") 
    print(Fore.CYAN + "3--> " + Fore.RESET  + "Pyramid") 
    print(Fore.CYAN + "4--> " + Fore.RESET  + "Cube")
    print(Fore.CYAN + "5--> " + Fore.RESET  + "Cylinder")
    print(Fore.CYAN + "6--> " + Fore.RESET  + "Cuboid") 
    fig_code2 = int(input(Fore.CYAN + "\nEnter the Figure code: " + Fore.RESET))

    match fig_code2:
        case 1:
            radius = float(input("\nEnter value of radius (Sphere): "))
            surface_area = 4 * pi * radius * radius
            volume = (4.0 /3) * pi * radius * radius * radius
            print(f"Surface area of Sphere = {surface_area : .2f}")
            print(f"Volume of the Sphere = {volume : .2f}")
            print(Fore.YELLOW + "...............................\n")
        case 2:
            radius = float(input("\nEnter value of radius (Cone): "))
            height = float(input("Enter value of height (Cone): "))
            surface_area = pi * radius * (radius + math.sqrt(radius * radius + height))
            volume = (1.0 / 3) * pi * radius * radius * height
            print(f"Surface area of Cone = {surface_area : .2f}")
            print(f"Volume of the Cone = {volume : .2f}")
            print(Fore.YELLOW + "...............................\n")
        case 3:
            side = float(input("Enter value of side (Pyramid): "))
            base = float(input("Enter value of base (Pyramid): "))
            height = float(input("Enter value of height (Pyramid): "))
            surface_area = (base * base) + (((height * base) / 2) * 4)
            volume = (1.0 / 3) * base * side * height
            print(f"Surface area of Pyramid = {surface_area : .2f}")
            print(f"Volume of the Pyramid = {volume : .2f}")
            print(Fore.YELLOW + "................................\n")
        case 4:
            side = float(input(("\nEnter value of side (Cube): ")))
            surface_area = 6.0 * side * side
            volume = math.pow(side, 3)
            print(f"Surface area of Cube = {surface_area : .2f}")
            print(f"Volume of the Cube = {volume : .2f}")
            print(Fore.YELLOW + "............................\n")
        case 5:
            radius = float(input(("\nEnter value of radius (Cylinder): ")))
            height = float(input(("Enter value of height (Cylinder): ")))
            surface_area = 2.0 * pi * radius * (radius + height)
            volume = pi * radius * radius * height
            print(f"Surface area of Cylinder = {surface_area : .2f}")
            print(f"Volume of the Cylinder = {volume : .2f}")
            print(Fore.YELLOW + "............................\n")
        case 6:
            width = float(input(("Enter value of width (Cuboid): ")))
            length = float(input(("Enter value of length (Cuboid): ")))
            height = float(input(("Enter value of height (Cuboid): ")))
            surface_area = 2.0 * ((width * length) + (length * height) + (height * width))
            volume = width * length * height
            print(f"Surface area of Cuboid = {surface_area : .2f}")
            print(f"Volume of the Cuboid = {volume : .2f}")
            print(Fore.YELLOW + "............................\n")
        case _:
            fig_code2 = print(Fore.MAGENTA + Back.LIGHTRED_EX + "Error figure code. \n")
            print(Fore.YELLOW + "..................................\n")



while True:
    input_char()

    choice= input(Fore.LIGHTRED_EX + "Do you want to solve another one? (y or n): ").lower()
    if choice == 'y':
        continue
    elif choice == 'n':
        print("Goodbye! Exiting the program.")
        break
    else:
        print('\tInvalid Input')


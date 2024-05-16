#this program is going to solve angle and change them to another angle.
import math
import colorama
from colorama import Fore ,Back, Style
colorama.init(autoreset= True)



def main():

    print(Fore.LIGHTMAGENTA_EX + '\n\nWelcome to the Angle Convertor.\n\n' + Fore.RESET)
    calculate_angle()


#calculate angle program
def calculate_angle():
    pi = 3.14
    
    print(Fore.LIGHTYELLOW_EX + "\nChose one of the following Angles to Calculate\n" + Fore.RESET)

    print(Fore.CYAN + "1--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "Degrees" + Fore.RESET + " to Radians")
    print(Fore.CYAN + "2--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "Degrees" + Fore.RESET + " to Gradians")
    print(Fore.CYAN + "3--> " + Fore.RESET + Fore.LIGHTRED_EX + "Radians" + Fore.RESET + " to Degrees")
    print(Fore.CYAN + "4--> " + Fore.RESET + Fore.LIGHTRED_EX + "Radians" + Fore.RESET + " to Gradians")
    print(Fore.CYAN + "5--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "Gradians" + Fore.RESET + " to Radians")
    print(Fore.CYAN + "6--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "Gradians" + Fore.RESET + " to Degrees")
    fig_code = int(input(Fore.CYAN + "\nEnter the Figure code: " + Fore.RESET))

    match fig_code:
        #degrees
        case 1 :
            degrees=float(input ("\nEnter Angle in Degree: "))
            radians=(degrees*pi)/180
            print(f"Your Angle in Radians is: {radians: .2f}")
            print(Fore.YELLOW +"................................\n")
        case 2 :
            degrees=float(input ("\nEnter Angle in Degree: "))
            grads=(degrees/9)*10
            print(f"Your Angle in Gradians is: {grads: .2f}")
            print(Fore.YELLOW +"................................\n")
            #radians
        case 3 :
            radians=float (input ("\nEnter angle in Radians: "))
            degree=radians*(180/pi)
            print(f"Your Angle in Degree is: {degree: .2f}")
            print(Fore.YELLOW +"................................\n")
        case 4 :
            radians=float (input ("\nEnter angle in Radians: "))
            grads=(radians/(math.pi))*200
            print(f"Your Angle in Gradians is: {grads: .2f}")
            print(Fore.YELLOW +"................................\n")
        #gradians
        case 5 :
            grads= float( input("\nEnter angle in Gradians: "))
            radians =(grads / 200)*(math.pi)
            print(f"Your Angle in Radians is: {radians: .2f}")
            print(Fore.YELLOW +"................................\n")
        case 6 :
            grads= float( input("\nEnter angle in Gradians: "))
            degree = grads * 0.9
            print(f"Your Angle in Degree is: {degree: .2f}")
            print(Fore.YELLOW +"................................\n")
        case _ :
            fig_code = print(Fore.MAGENTA + Style.BRIGHT + "\nError in Figure code\n" + Fore.RESET + Style.RESET_ALL)
            print(Fore.YELLOW + "================================================================\n")


while True:
    main()

    choice= input(Fore.LIGHTRED_EX + "Do you want to solve another one? (y or n): ").lower()
    if choice == 'y':
        continue
    elif choice == 'n':
        print("Goodbye! Exiting the program...")
        break
    else:
        print('\t\t!!!Invalid Input!!!')
        break

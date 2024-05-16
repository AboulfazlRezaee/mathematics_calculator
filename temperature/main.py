#this program is going to change temperature(c to f to k).
import colorama
from colorama import Fore ,Back, Style
colorama.init(autoreset= True)


def main():

    print(Fore.LIGHTMAGENTA_EX + '\n\nThis Program Calculate Different Temperature.\n\n' + Fore.RESET)
    change_temperature()


def change_temperature():
    print(Fore.LIGHTYELLOW_EX + "\nChose one of the following Temperature to Calculate\n" + Fore.RESET)

    #celsius
    print(Fore.CYAN + "1--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "Celsius" + Fore.RESET + " to Fahrenheit")
    print(Fore.CYAN + "2--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "Celsius" + Fore.RESET + " to Kelvin")
    #fahrenheit
    print(Fore.CYAN + "3--> " + Fore.RESET + Fore.LIGHTRED_EX + "Fahrenheit" + Fore.RESET + " to Celsius")
    print(Fore.CYAN + "4--> " + Fore.RESET + Fore.LIGHTRED_EX + "Fahrenheit" + Fore.RESET + " to Kelvin")
    #kelvin
    print(Fore.CYAN + "5--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "Kelvin" + Fore.RESET + " to Celsius")
    print(Fore.CYAN + "6--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "Kelvin" + Fore.RESET + " to Fahrenheit")
    #fig_code
    fig_code = int(input(Fore.CYAN + "\nEnter the Figure code: " + Fore.RESET))

    match fig_code:
        case 1 :
            celsius=float(input ("\nEnter Temperature in Celsius: "))
            fahrenheit=(celsius*1.8)+32
            print(f"Your Temperature in Fahrenheit is: {fahrenheit: .2f}")
            print(Fore.YELLOW +"................................\n")
        case 2 :
            celsius=float(input ("\nEnter Temperature in Celsius: "))
            kelvin=(celsius+273.15)
            print(f"Your Temperature in Kelvin is: {kelvin: .2f}")
            print(Fore.YELLOW +"................................\n")
        #fahrenheit
        case 3 :
            fahrenheit=float (input ("\nEnter temperature in Fahrenheit: "))
            celsius=(fahrenheit-32)/1.8
            print(f"Your Temperature in Celsius is: {celsius: .2f}")
            print(Fore.YELLOW +"................................\n")
        case 4 :
            fahrenheit=float (input ("\nEnter temperature in Fahrenheit: "))
            kelvin=(fahrenheit-32)/1.8+273.15
            print(f"Your Temperature in Kelvin is: {kelvin: .2f}")
            print(Fore.YELLOW +"................................\n")
        #kelvin
        case 5 :
            kelvin=float (input ("\nEnter temperature in Kelvin: "))
            celsius=(kelvin-273.15)
            print(f"Your Temperature in Celsius is: {celsius: .2f}")
            print(Fore.YELLOW +"................................\n")
        case 6 :
            kelvin=float (input ("\nEnter temperature in Kelvin: "))
            fahrenheit=(kelvin-273.15)*1.8+32
            print(f"Your Temperature in Fahrenheit is: {fahrenheit: .2f}")
            print(Fore.YELLOW +"................................\n")
        case _ :
            print(Fore.MAGENTA + Back.LIGHTRED_EX + "\n.....YOU USED WRONG KEY WORD.....\n")
            print(Fore.YELLOW + "================================================================\n")

#while loop for continue and exiting the program
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
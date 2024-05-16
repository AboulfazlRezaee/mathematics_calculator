#this program is going to solve speed and change them to all (km/h to m/s)
import math
import colorama
from colorama import Fore ,Back
colorama.init(autoreset= True)

#main program
def main():
    print(Fore.LIGHTMAGENTA_EX + "\n\nWelcome To The Speed Converter.\n\n" + Fore.RESET)
    speed_converter()

#speed converter function
def speed_converter():
    print(Fore.LIGHTYELLOW_EX + "\nChose one of the following Speed to Calculate\n" + Fore.RESET)
    #km/h
    print(Fore.CYAN + "1--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "km/h" + Fore.RESET + " to m/s")
    print(Fore.CYAN + "2--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "km/h" + Fore.RESET + " to cm/s")
    print(Fore.CYAN + "3--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "km/h" + Fore.RESET + " to ft/s")
    print(Fore.CYAN + "4--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "km/h" + Fore.RESET + " to mph")
    print(Fore.CYAN + "5--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "km/h" + Fore.RESET + " to knots")
    print(Fore.CYAN + "6--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "km/h" + Fore.RESET + " to mach")
    #m/s
    print(Fore.CYAN + "7--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m/s" + Fore.RESET + " to km/h")
    print(Fore.CYAN + "8--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m/s" + Fore.RESET + " to cm/s")
    print(Fore.CYAN + "9--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m/s" + Fore.RESET + " to ft/s")
    print(Fore.CYAN + "10--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m/s" + Fore.RESET + " to mph")
    print(Fore.CYAN + "11--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m/s" + Fore.RESET + " to knots")
    print(Fore.CYAN + "12--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m/s" + Fore.RESET + " to mach")
    #cm/s
    print(Fore.CYAN + "13--> " + Fore.RESET + Fore.LIGHTRED_EX + "cm/s" + Fore.RESET + " to km/h")
    print(Fore.CYAN + "14--> " + Fore.RESET + Fore.LIGHTRED_EX + "cm/s" + Fore.RESET + " to m/s")
    print(Fore.CYAN + "15--> " + Fore.RESET + Fore.LIGHTRED_EX + "cm/s" + Fore.RESET + " to ft/s")
    print(Fore.CYAN + "16--> " + Fore.RESET + Fore.LIGHTRED_EX + "cm/s" + Fore.RESET + " to mph")
    print(Fore.CYAN + "17--> " + Fore.RESET + Fore.LIGHTRED_EX + "cm/s" + Fore.RESET + " to knots")
    print(Fore.CYAN + "18--> " + Fore.RESET + Fore.LIGHTRED_EX + "cm/s" + Fore.RESET + " to mach")
    #ft/s
    print(Fore.CYAN + "19--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "ft/s" + Fore.RESET + " to km/h")
    print(Fore.CYAN + "20--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "ft/s" + Fore.RESET + " to m/s")
    print(Fore.CYAN + "21--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "ft/s" + Fore.RESET + " to cm/s")
    print(Fore.CYAN + "22--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "ft/s" + Fore.RESET + " to mph")
    print(Fore.CYAN + "23--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "ft/s" + Fore.RESET + " to knots")
    print(Fore.CYAN + "24--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "ft/s" + Fore.RESET + " to mach")
    #mph
    print(Fore.CYAN + "25--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "mph" + Fore.RESET + " to km/h")
    print(Fore.CYAN + "26--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "mph" + Fore.RESET + " to m/s")
    print(Fore.CYAN + "27--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "mph" + Fore.RESET + " to cm/s")
    print(Fore.CYAN + "28--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "mph" + Fore.RESET + " to ft/s")
    print(Fore.CYAN + "29--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "mph" + Fore.RESET + " to knots")
    print(Fore.CYAN + "30--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "mph" + Fore.RESET + " to mach")
    #knots
    print(Fore.CYAN + "31--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "knots" + Fore.RESET + " to km/h")
    print(Fore.CYAN + "32--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "knots" + Fore.RESET + " to m/s")
    print(Fore.CYAN + "33--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "knots" + Fore.RESET + " to cm/s")
    print(Fore.CYAN + "34--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "knots" + Fore.RESET + " to ft/s")
    print(Fore.CYAN + "35--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "knots" + Fore.RESET + " to mph")
    print(Fore.CYAN + "36--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "knots" + Fore.RESET + " to mach")
    #mach
    print(Fore.CYAN + "37--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "mach" + Fore.RESET + " to km/h")
    print(Fore.CYAN + "38--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "mach" + Fore.RESET + " to m/s")
    print(Fore.CYAN + "39--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "mach" + Fore.RESET + " to cm/s")
    print(Fore.CYAN + "40--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "mach" + Fore.RESET + " to ft/s")
    print(Fore.CYAN + "41--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "mach" + Fore.RESET + " to mph")
    print(Fore.CYAN + "42--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "mach" + Fore.RESET + " to knots")
    #fig_code
    fig_code = int(input(Fore.CYAN + "\nEnter the Figure code: " + Fore.RESET))

    #match case for fig code
    match fig_code:
        #km/h to m/s
        case 1 :
            kmh=float(input ("\nEnter Speed in km/h: "))
            mps=(kmh*1000)/3600
            print(f"Your Speed in m/s is: {mps: .2f}")
            print(Fore.YELLOW +"................................\n")
        #km/h to cm/s
        case 2 :
            kmh=float (input ("\nEnter Speed in km/h: "))
            cpm=(kmh*100000)/3600
            print(f"Your Speed in cm/s is: {cpm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #km/h to ft/s
        case 3 :
            kmh=float (input ("\nEnter Speed in km/h: "))
            fpm=(kmh*5280)/3600
            print(f"Your Speed in ft/s is: {fpm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #km/h to mph
        case 4 :
            kmh=float (input ("\nEnter Speed in km/h: "))
            mph=(kmh*3600)/1000
            print(f"Your Speed in mph is: {mph: .2f}")
            print(Fore.YELLOW +"................................\n")
        #km/h to knots
        case 5 :
            kmh=float (input ("\nEnter Speed in km/h: "))
            knots=(kmh*3600)/1852
            print(f"Your Speed in knots is: {knots: .2f}")
            print(Fore.YELLOW +"................................\n")
        #km/h to mach
        case 6 :
            kmh=float (input ("\nEnter Speed in km/h: "))
            mach=(kmh*3600)/3600
            print(f"Your Speed in mach is: {mach: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m/s to km/h
        case 7 :
            mps=float(input ("\nEnter Speed in m/s: "))
            kmh=(mps*3600)/1000
            print(f"Your Speed in km/h is: {kmh: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m/s to cm/s
        case 8 :
            mps=float (input ("\nEnter Speed in m/s: "))
            cpm=(mps*100000)/3600
            print(f"Your Speed in cm/s is: {cpm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m/s to ft/s
        case 9 :
            mps=float (input ("\nEnter Speed in m/s: "))
            fpm=(mps*5280)/3600
            print(f"Your Speed in ft/s is: {fpm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m/s to mph
        case 10 :
            mps=float (input ("\nEnter Speed in m/s: "))
            mph=(mps*3600)/1000
            print(f"Your Speed in mph is: {mph: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m/s to knots
        case 11 :
            mps=float (input ("\nEnter Speed in m/s: "))
            knots=(mps*3600)/1852
            print(f"Your Speed in knots is: {knots: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m/s to mach
        case 12 :
            mps=float (input ("\nEnter Speed in m/s: "))
            mach=(mps*3600)/3600
            print(f"Your Speed in mach is: {mach: .2f}")
            print(Fore.YELLOW +"................................\n")
        #cm/s to km/h
        case 13 :
            cpm=float(input ("\nEnter Speed in cm/s: "))
            kmh=(cpm*3600)/1000
            print(f"Your Speed in km/h is: {kmh: .2f}")
            print(Fore.YELLOW +"................................\n")
        #cm/s to m/s
        case 14 :
            cpm=float (input ("\nEnter Speed in cm/s: "))
            mps=(cpm*100000)/3600
            print(f"Your Speed in m/s is: {mps: .2f}")
            print(Fore.YELLOW +"................................\n")
        #cm/s to ft/s
        case 15 :
            cpm=float (input ("\nEnter Speed in cm/s: "))
            fpm=(cpm*5280)/3600
            print(f"Your Speed in ft/s is: {fpm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #cm/s to mph
        case 16 :
            cpm=float (input ("\nEnter Speed in cm/s: "))
            mph=(cpm*3600)/1000
            print(f"Your Speed in mph is: {mph: .2f}")
            print(Fore.YELLOW +"................................\n")
        #cm/s to knots
        case 17 :
            cpm=float (input ("\nEnter Speed in cm/s: "))
            knots=(cpm*3600)/1852
            print(f"Your Speed in knots is: {knots: .2f}")
            print(Fore.YELLOW +"................................\n")
        #cm/s to mach
        case 18 :
            cpm=float (input ("\nEnter Speed in cm/s: "))
            mach=(cpm*3600)/3600
            print(f"Your Speed in mach is: {mach: .2f}")
            print(Fore.YELLOW +"................................\n")
        #ft/s to km/h
        case 19 :
            fpm=float(input ("\nEnter Speed in ft/s: "))
            kmh=(fpm*3600)/1000
            print(f"Your Speed in km/h is: {kmh: .2f}")
            print(Fore.YELLOW +"................................\n")
        #ft/s to m/s
        case 20 :
            fpm=float (input ("\nEnter Speed in ft/s: "))
            mps=(fpm*100000)/3600
            print(f"Your Speed in m/s is: {mps: .2f}")
            print(Fore.YELLOW +"................................\n")
        #ft/s to cm/s
        case 21 :
            fpm=float (input ("\nEnter Speed in ft/s: "))
            cpm=(fpm*5280)/3600
            print(f"Your Speed in cm/s is: {cpm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #ft/s to mph
        case 22 :
            fpm=float (input ("\nEnter Speed in ft/s: "))
            mph=(fpm*3600)/1000
            print(f"Your Speed in mph is: {mph: .2f}")
            print(Fore.YELLOW +"................................\n")
        #ft/s to knots
        case 23 :
            fpm=float (input ("\nEnter Speed in ft/s: "))
            knots=(fpm*3600)/1852
            print(f"Your Speed in knots is: {knots: .2f}")
            print(Fore.YELLOW +"................................\n")
        #ft/s to mach
        case 24 :
            fpm=float (input ("\nEnter Speed in ft/s: "))
            mach=(fpm*3600)/3600
            print(f"Your Speed in mach is: {mach: .2f}")
            print(Fore.YELLOW +"................................\n")
        #mph to km/h
        case 25 :
            mph=float(input ("\nEnter Speed in mph: "))
            kmh=(mph*3600)/1000
            print(f"Your Speed in km/h is: {kmh: .2f}")
            print(Fore.YELLOW +"................................\n")
        #mph to m/s
        case 26 :
            mph=float (input ("\nEnter Speed in mph: "))
            mps=(mph*1000)/3600
            print(f"Your Speed in m/s is: {mps: .2f}")
            print(Fore.YELLOW +"................................\n")
        #mph to cm/s
        case 27 :
            mph=float (input ("\nEnter Speed in mph: "))
            cpm=(mph*5280)/3600
            print(f"Your Speed in cm/s is: {cpm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #mph to ft/s
        case 28 :
            mph=float (input ("\nEnter Speed in mph: "))
            fpm=(mph*5280)/3600
            print(f"Your Speed in ft/s is: {fpm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #mph to knots
        case 29 :
            mph=float (input ("\nEnter Speed in mph: "))
            knots=(mph*3600)/1852
            print(f"Your Speed in knots is: {knots: .2f}")
            print(Fore.YELLOW +"................................\n")
        #mph to mach
        case 30 :
            mph=float (input ("\nEnter Speed in mph: "))
            mach=(mph*3600)/3600
            print(f"Your Speed in mach is: {mach: .2f}")
            print(Fore.YELLOW +"................................\n")
        #knots to km/h
        case 31 :
            knots=float(input ("\nEnter Speed in knots: "))
            kmh=(knots*3600)/1000
            print(f"Your Speed in km/h is: {kmh: .2f}")
            print(Fore.YELLOW +"................................\n")
        #knots to m/s
        case 32 :
            knots=float (input ("\nEnter Speed in knots: "))
            mps=(knots*1000)/3600
            print(f"Your Speed in m/s is: {mps: .2f}")
            print(Fore.YELLOW +"................................\n")
        #knots to cm/s
        case 33 :
            knots=float (input ("\nEnter Speed in knots: "))
            cpm=(knots*5280)/3600
            print(f"Your Speed in cm/s is: {cpm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #knots to ft/s
        case 34 :
            knots=float (input ("\nEnter Speed in knots: "))
            fpm=(knots*5280)/3600
            print(f"Your Speed in ft/s is: {fpm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #knots to mph
        case 35 :
            knots=float (input ("\nEnter Speed in knots: "))
            mph=(knots*3600)/1000
            print(f"Your Speed in mph is: {mph: .2f}")
            print(Fore.YELLOW +"................................\n")
        #knots to mach
        case 36 :
            knots=float (input ("\nEnter Speed in knots: "))
            mach=(knots*3600)/3600
            print(f"Your Speed in mach is: {mach: .2f}")
            print(Fore.YELLOW +"................................\n")
        #mach to km/h
        case 37 :
            mach=float(input ("\nEnter Speed in mach: "))
            kmh=(mach*3600)/1000
            print(f"Your Speed in km/h is: {kmh: .2f}")
            print(Fore.YELLOW +"................................\n")
        #mach to m/s
        case 38 :
            mach=float (input ("\nEnter Speed in mach: "))
            mps=(mach*1000)/3600
            print(f"Your Speed in m/s is: {mps: .2f}")
            print(Fore.YELLOW +"................................\n")
        #mach to cm/s
        case 39 :
            mach=float (input ("\nEnter Speed in mach: "))
            cpm=(mach*5280)/3600
            print(f"Your Speed in cm/s is: {cpm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #mach to ft/s
        case 40 :
            mach=float (input ("\nEnter Speed in mach: "))
            fpm=(mach*5280)/3600
            print(f"Your Speed in ft/s is: {fpm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #mach to mph
        case 41 :
            mach=float (input ("\nEnter Speed in mach: "))
            mph=(mach*3600)/1000
            print(f"Your Speed in mph is: {mph: .2f}")
            print(Fore.YELLOW +"................................\n")
        #mach to knots
        case 42 :
            mach=float (input ("\nEnter Speed in mach: "))
            knots=(mach*3600)/1852
            print(f"Your Speed in knots is: {knots: .2f}")
            print(Fore.YELLOW +"................................\n")
        #error case
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

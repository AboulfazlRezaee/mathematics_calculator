#this program is going to change length like (cm to m to km inches to feed)
import colorama
from colorama import Fore ,Back, Style
colorama.init(autoreset= True)

#main program
def main():
    print(Fore.LIGHTMAGENTA_EX + "\n\nWelcome To The Length Converter.\n\n" + Fore.RESET)
    length_converter()


#Length converter function
def length_converter():
    print(Fore.LIGHTYELLOW_EX + "\nChose one of the following Length to Calculate\n" + Fore.RESET)
    #cm
    print(Fore.CYAN + "1--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "cm" + Fore.RESET + " to m")
    print(Fore.CYAN + "2--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "cm" + Fore.RESET + " to km")
    print(Fore.CYAN + "3--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "cm" + Fore.RESET + " to inches")
    print(Fore.CYAN + "4--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "cm" + Fore.RESET + " to feet")
    print(Fore.CYAN + "5--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "cm" + Fore.RESET + " to yards")
    print(Fore.CYAN + "6--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "cm" + Fore.RESET + " to miles")
    print(Fore.CYAN + "7--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "cm" + Fore.RESET + " to nanometers")
    print(Fore.CYAN + "8--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "cm" + Fore.RESET + " to micrometers")
    print(Fore.CYAN + "9--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "cm" + Fore.RESET + " to millimeters")
    #m
    print(Fore.CYAN + "10--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m" + Fore.RESET + " to cm")
    print(Fore.CYAN + "11--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m" + Fore.RESET + " to km")
    print(Fore.CYAN + "12--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m" + Fore.RESET + " to inches")
    print(Fore.CYAN + "13--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m" + Fore.RESET + " to feet")
    print(Fore.CYAN + "14--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m" + Fore.RESET + " to yards")
    print(Fore.CYAN + "15--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m" + Fore.RESET + " to miles")
    print(Fore.CYAN + "16--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m" + Fore.RESET + " to nanometers")
    print(Fore.CYAN + "17--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m" + Fore.RESET + " to micrometers")
    print(Fore.CYAN + "18--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "m" + Fore.RESET + " to millimeters")
    #km
    print(Fore.CYAN + "19--> " + Fore.RESET + Fore.LIGHTRED_EX + "km" + Fore.RESET + " to cm")
    print(Fore.CYAN + "20--> " + Fore.RESET + Fore.LIGHTRED_EX + "km" + Fore.RESET + " to m")
    print(Fore.CYAN + "21--> " + Fore.RESET + Fore.LIGHTRED_EX + "km" + Fore.RESET + " to inches")
    print(Fore.CYAN + "22--> " + Fore.RESET + Fore.LIGHTRED_EX + "km" + Fore.RESET + " to feet")
    print(Fore.CYAN + "23--> " + Fore.RESET + Fore.LIGHTRED_EX + "km" + Fore.RESET + " to yards")
    print(Fore.CYAN + "24--> " + Fore.RESET + Fore.LIGHTRED_EX + "km" + Fore.RESET + " to miles")
    print(Fore.CYAN + "25--> " + Fore.RESET + Fore.LIGHTRED_EX + "km" + Fore.RESET + " to nanometers")
    print(Fore.CYAN + "26--> " + Fore.RESET + Fore.LIGHTRED_EX + "km" + Fore.RESET + " to micrometers")
    print(Fore.CYAN + "27--> " + Fore.RESET + Fore.LIGHTRED_EX + "km" + Fore.RESET + " to millimeters")
    #inches
    print(Fore.CYAN + "28--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "inches" + Fore.RESET + " to cm")
    print(Fore.CYAN + "29--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "inches" + Fore.RESET + " to m")
    print(Fore.CYAN + "30--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "inches" + Fore.RESET + " to km")
    print(Fore.CYAN + "31--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "inches" + Fore.RESET + " to feet")
    print(Fore.CYAN + "32--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "inches" + Fore.RESET + " to yards")
    print(Fore.CYAN + "33--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "inches" + Fore.RESET + " to miles")
    print(Fore.CYAN + "34--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "inches" + Fore.RESET + " to nanometers")
    print(Fore.CYAN + "35--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "inches" + Fore.RESET + " to micrometers")
    print(Fore.CYAN + "36--> " + Fore.RESET + Fore.LIGHTYELLOW_EX + "inches" + Fore.RESET + " to millimeters")
    #feet
    print(Fore.CYAN + "37--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "feet" + Fore.RESET + " to cm")
    print(Fore.CYAN + "38--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "feet" + Fore.RESET + " to m")
    print(Fore.CYAN + "39--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "feet" + Fore.RESET + " to km")
    print(Fore.CYAN + "40--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "feet" + Fore.RESET + " to inches")
    print(Fore.CYAN + "41--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "feet" + Fore.RESET + " to yards")
    print(Fore.CYAN + "42--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "feet" + Fore.RESET + " to miles")
    print(Fore.CYAN + "43--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "feet" + Fore.RESET + " to nanometers")
    print(Fore.CYAN + "44--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "feet" + Fore.RESET + " to micrometers")
    print(Fore.CYAN + "45--> " + Fore.RESET + Fore.LIGHTCYAN_EX + "feet" + Fore.RESET + " to millimeters")
    #yards
    print(Fore.CYAN + "46--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "yards" + Fore.RESET + " to cm")
    print(Fore.CYAN + "47--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "yards" + Fore.RESET + " to m")
    print(Fore.CYAN + "48--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "yards" + Fore.RESET + " to km")
    print(Fore.CYAN + "49--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "yards" + Fore.RESET + " to inches")
    print(Fore.CYAN + "50--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "yards" + Fore.RESET + " to feed")
    print(Fore.CYAN + "51--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "yards" + Fore.RESET + " to miles")
    print(Fore.CYAN + "52--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "yards" + Fore.RESET + " to nanometers")
    print(Fore.CYAN + "53--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "yards" + Fore.RESET + " to micrometers")
    print(Fore.CYAN + "54--> " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "yards" + Fore.RESET + " to millimeters")
    #miles
    print(Fore.CYAN + "55--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "miles" + Fore.RESET + " to cm")
    print(Fore.CYAN + "56--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "miles" + Fore.RESET + " to m")
    print(Fore.CYAN + "57--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "miles" + Fore.RESET + " to km")
    print(Fore.CYAN + "58--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "miles" + Fore.RESET + " to inches")
    print(Fore.CYAN + "59--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "miles" + Fore.RESET + " to feed")
    print(Fore.CYAN + "60--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "miles" + Fore.RESET + " to yard")
    print(Fore.CYAN + "61--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "miles" + Fore.RESET + " to nanometers")
    print(Fore.CYAN + "62--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "miles" + Fore.RESET + " to micrometers")
    print(Fore.CYAN + "63--> " + Fore.RESET + Fore.LIGHTBLUE_EX + "miles" + Fore.RESET + " to millimeters")
    #nanometers
    print(Fore.CYAN + "64--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "nanometers" + Fore.RESET + " to cm")
    print(Fore.CYAN + "65--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "nanometers" + Fore.RESET + " to m")
    print(Fore.CYAN + "66--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "nanometers" + Fore.RESET + " to km")
    print(Fore.CYAN + "67--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "nanometers" + Fore.RESET + " to inches")
    print(Fore.CYAN + "68--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "nanometers" + Fore.RESET + " to feet")
    print(Fore.CYAN + "69--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "nanometers" + Fore.RESET + " to yards")
    print(Fore.CYAN + "70--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "nanometers" + Fore.RESET + " to miles")
    print(Fore.CYAN + "71--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "nanometers" + Fore.RESET + " to micrometers")
    print(Fore.CYAN + "72--> " + Fore.RESET + Fore.LIGHTWHITE_EX + "nanometers" + Fore.RESET + " to millimeters")
    #micrometers
    print(Fore.CYAN + "73--> " + Fore.RESET + Fore.LIGHTRED_EX + "micrometers" + Fore.RESET + " to cm")
    print(Fore.CYAN + "74--> " + Fore.RESET + Fore.LIGHTRED_EX + "micrometers" + Fore.RESET + " to m")
    print(Fore.CYAN + "75--> " + Fore.RESET + Fore.LIGHTRED_EX + "micrometers" + Fore.RESET + " to km")
    print(Fore.CYAN + "76--> " + Fore.RESET + Fore.LIGHTRED_EX + "micrometers" + Fore.RESET + " to inches")
    print(Fore.CYAN + "77--> " + Fore.RESET + Fore.LIGHTRED_EX + "micrometers" + Fore.RESET + " to feet")
    print(Fore.CYAN + "78--> " + Fore.RESET + Fore.LIGHTRED_EX + "micrometers" + Fore.RESET + " to yards")
    print(Fore.CYAN + "79--> " + Fore.RESET + Fore.LIGHTRED_EX + "micrometers" + Fore.RESET + " to miles")
    print(Fore.CYAN + "80--> " + Fore.RESET + Fore.LIGHTRED_EX + "micrometers" + Fore.RESET + " to nanometers")
    print(Fore.CYAN + "81--> " + Fore.RESET + Fore.LIGHTRED_EX + "micrometers" + Fore.RESET + " to millimeters")
    #millimeters
    print(Fore.CYAN + "82--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "millimeters" + Fore.RESET + " to cm")
    print(Fore.CYAN + "83--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "millimeters" + Fore.RESET + " to m")
    print(Fore.CYAN + "84--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "millimeters" + Fore.RESET + " to km")
    print(Fore.CYAN + "85--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "millimeters" + Fore.RESET + " to inches")
    print(Fore.CYAN + "86--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "millimeters" + Fore.RESET + " to feet")
    print(Fore.CYAN + "87--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "millimeters" + Fore.RESET + " to yards")
    print(Fore.CYAN + "88--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "millimeters" + Fore.RESET + " to miles")
    print(Fore.CYAN + "89--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "millimeters" + Fore.RESET + " to nanometers")
    print(Fore.CYAN + "90--> " + Fore.RESET + Fore.LIGHTGREEN_EX + "millimeters" + Fore.RESET + " to micrometers")
    #fig_code
    fig_code = int(input(Fore.CYAN + "\nEnter the Figure code: " + Fore.RESET))

    #match case for converting length
    match fig_code:
        # cm to m
        case 1:
            cm=float(input ("\nEnter Length in cm: "))
            m=cm/100
            print(f"Your Length in m is: {m: .2f}")
            print(Fore.YELLOW +"................................\n")
        #cm to km
        case 2:
            cm=float(input ("\nEnter Length in cm: "))
            km=cm/100000
            print(f"Your Length in km is: {km: .2f}")
            print(Fore.YELLOW +"................................\n")
        #cm to inches
        case 3:
            cm=float(input ("\nEnter Length in cm: "))
            inches=cm/2.54
            print(f"Your Length in inches is: {inches: .2f}")
            print(Fore.YELLOW +"................................\n")
        #cm to feet
        case 4:
            cm=float(input ("\nEnter Length in cm: "))
            feet=cm/30.48
            print(f"Your Length in feet is: {feet: .2f}")
            print(Fore.YELLOW +"................................\n")
        #cm to yards
        case 5:
            cm=float(input ("\nEnter Length in cm: "))
            yards=cm/91.44
            print(f"Your Length in yards is: {yards: .2f}")
            print(Fore.YELLOW +"................................\n")
        #cm to miles
        case 6:
            cm=float(input ("\nEnter Length in cm: "))
            miles=cm/160934
            print(f"Your Length in miles is: {miles: .2f}")
            print(Fore.YELLOW +"................................\n")
        #cm to nanometers
        case 7:
            cm=float(input ("\nEnter Length in cm: "))
            nanometers=cm/100000000
            print(f"Your Length in nanometers is: {nanometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #cm to micrometers
        case 8:
            cm=float(input ("\nEnter Length in cm: "))
            micrometers=cm/1000000
            print(f"Your Length in micrometers is: {micrometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #cm to millimeters
        case 9:
            cm=float(input ("\nEnter Length in cm: "))
            millimeters=cm/1000
            print(f"Your Length in millimeters is: {millimeters: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m to cm
        case 10:
            m=float(input ("\nEnter Length in m: "))
            cm=m*100
            print(f"Your Length in cm is: {cm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m to km
        case 11:
            m=float(input ("\nEnter Length in m: "))
            km=m/1000
            print(f"Your Length in km is: {km: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m to inches
        case 12:
            m=float(input ("\nEnter Length in m: "))
            inches=m*39.37
            print(f"Your Length in inches is: {inches: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m to feet
        case 13:
            m=float(input ("\nEnter Length in m: "))
            feet=m*3.281
            print(f"Your Length in feet is: {feet: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m to yards
        case 14:
            m=float(input ("\nEnter Length in m: "))
            yards=m*1.094
            print(f"Your Length in yards is: {yards: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m to miles
        case 15:
            m=float(input ("\nEnter Length in m: "))
            miles=m*0.000621
            print(f"Your Length in miles is: {miles: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m to nanometers
        case 16:
            m=float(input ("\nEnter Length in m: "))
            nanometers=m*1000000000
            print(f"Your Length in nanometers is: {nanometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m to micrometers
        case 17:
            m=float(input ("\nEnter Length in m: "))
            micrometers=m*1000000
            print(f"Your Length in micrometers is: {micrometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #m to millimeters
        case 18:
            m=float(input ("\nEnter Length in m: "))
            millimeters=m*1000
            print(f"Your Length in millimeters is: {millimeters: .2f}")
            print(Fore.YELLOW +"................................\n")
        #km to cm
        case 19:
            km=float(input ("\nEnter Length in km: "))
            cm=km*100000
            print(f"Your Length in cm is: {cm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #km to m
        case 20:
            km=float(input ("\nEnter Length in km: "))
            m=km*1000
            print(f"Your Length in m is: {m: .2f}")
            print(Fore.YELLOW +"................................\n")
        #km to inches
        case 21:
            km=float(input ("\nEnter Length in km: "))
            inches=km*39370
            print(f"Your Length in inches is: {inches: .2f}")
            print(Fore.YELLOW +"................................\n")
        #km to feet
        case 22:
            km=float(input ("\nEnter Length in km: "))
            feet=km*3280
            print(f"Your Length in feet is: {feet: .2f}")
            print(Fore.YELLOW +"................................\n")
        #km to yards
        case 23:
            km=float(input ("\nEnter Length in km: "))
            yards=km*1094
            print(f"Your Length in yards is: {yards: .2f}")
            print(Fore.YELLOW +"................................\n")
        #km to miles
        case 24:
            km=float(input ("\nEnter Length in km: "))
            miles=km*0.621
            print(f"Your Length in miles is: {miles: .2f}")
            print(Fore.YELLOW +"................................\n")
        #km to nanometers
        case 25:
            km=float(input ("\nEnter Length in km: "))
            nanometers=km*1000000000
            print(f"Your Length in nanometers is: {nanometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #km to micrometers
        case 26:
            km=float(input ("\nEnter Length in km: "))
            micrometers=km*1000000
            print(f"Your Length in micrometers is: {micrometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #km to millimeters
        case 27:
            km=float(input ("\nEnter Length in km: "))
            millimeters=km*1000
            print(f"Your Length in millimeters is: {millimeters: .2f}")
            print(Fore.YELLOW +"................................\n")
        #inches to cm
        case 28:
            inches=float(input ("\nEnter Length in inches: "))
            cm=inches*2.54
            print(f"Your Length in cm is: {cm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #inches to m
        case 29:
            inches=float(input ("\nEnter Length in inches: "))
            m=inches*0.0254
            print(f"Your Length in m is: {m: .2f}")
            print(Fore.YELLOW +"................................\n")
        #inches to km
        case 30:
            inches=float(input ("\nEnter Length in inches: "))
            km=inches/39370
            print(f"Your Length in km is: {km: .2f}")
            print(Fore.YELLOW +"................................\n")
        #inches to feet
        case 31:
            inches=float(input ("\nEnter Length in inches: "))
            feet=inches/12
            print(f"Your Length in feet is: {feet: .2f}")
            print(Fore.YELLOW +"................................\n")
        #inches to yards
        case 32:
            inches=float(input ("\nEnter Length in inches: "))
            yards=inches/36
            print(f"Your Length in yards is: {yards: .2f}")
            print(Fore.YELLOW +"................................\n")
        #inches to miles
        case 33:
            inches=float(input ("\nEnter Length in inches: "))
            miles=inches/63360
            print(f"Your Length in miles is: {miles: .2f}")
            print(Fore.YELLOW +"................................\n")
        #inches to nanometers
        case 34:
            inches=float(input ("\nEnter Length in inches: "))
            nanometers=inches*1000000000
            print(f"Your Length in nanometers is: {nanometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #inches to micrometers
        case 35:
            inches=float(input ("\nEnter Length in inches: "))
            micrometers=inches*1000000
            print(f"Your Length in micrometers is: {micrometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #inches to millimeters
        case 36:
            inches=float(input ("\nEnter Length in inches: "))
            millimeters=inches*25.4
            print(f"Your Length in millimeters is: {millimeters: .2f}")
            print(Fore.YELLOW +"................................\n")
        #feet to cm
        case 37:
            feet=float(input ("\nEnter Length in feet: "))
            cm=feet*30.48
            print(f"Your Length in cm is: {cm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #feet to m
        case 38:
            feet=float(input ("\nEnter Length in feet: "))
            m=feet*0.3048
            print(f"Your Length in m is: {m: .2f}")
            print(Fore.YELLOW +"................................\n")
        #feet to km
        case 39:
            feet=float(input ("\nEnter Length in feet: "))
            km=feet/3280
            print(f"Your Length in km is: {km: .2f}")
            print(Fore.YELLOW +"................................\n")
        #feet to inches
        case 40:
            feet=float(input ("\nEnter Length in feet: "))
            inches=feet*12
            print(f"Your Length in inches is: {inches: .2f}")
            print(Fore.YELLOW +"................................\n")
        #feet to yards
        case 41:
            feet=float(input ("\nEnter Length in feet: "))
            yards=feet/3
            print(f"Your Length in yards is: {yards: .2f}")
            print(Fore.YELLOW +"................................\n")
        #feet to miles
        case 42:
            feet=float(input ("\nEnter Length in feet: "))
            miles=feet/5280
            print(f"Your Length in miles is: {miles: .2f}")
            print(Fore.YELLOW +"................................\n")
        #feet to nanometers
        case 43:
            feet=float(input ("\nEnter Length in feet: "))
            nanometers=feet*1000000000
            print(f"Your Length in nanometers is: {nanometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #feet to micrometers
        case 44:
            feet=float(input ("\nEnter Length in feet: "))
            micrometers=feet*1000000
            print(f"Your Length in micrometers is: {micrometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #feet to millimeters
        case 45:
            feet=float(input ("\nEnter Length in feet: "))
            millimeters=feet*304.8
            print(f"Your Length in millimeters is: {millimeters: .2f}")
            print(Fore.YELLOW +"................................\n")
        #yards to cm
        case 46:
            yards=float(input ("\nEnter Length in yards: "))
            cm=yards*91.44
            print(f"Your Length in cm is: {cm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #yards to m
        case 47:
            yards=float(input ("\nEnter Length in yards: "))
            m=yards*0.9144
            print(f"Your Length in m is: {m: .2f}")
            print(Fore.YELLOW +"................................\n")
        #yards to km
        case 48:
            yards=float(input ("\nEnter Length in yards: "))
            km=yards/1094
            print(f"Your Length in km is: {km: .2f}")
            print(Fore.YELLOW +"................................\n")
        #yards to inches
        case 49:
            yards=float(input ("\nEnter Length in yards: "))
            inches=yards*36
            print(f"Your Length in inches is: {inches: .2f}")
            print(Fore.YELLOW +"................................\n")
        #yards to feet
        case 50:
            yards=float(input ("\nEnter Length in yards: "))
            feet=yards*3
            print(f"Your Length in feet is: {feet: .2f}")
            print(Fore.YELLOW +"................................\n")
        #yards to miles
        case 51:
            yards=float(input ("\nEnter Length in yards: "))
            miles=yards/1760
            print(f"Your Length in miles is: {miles: .2f}")
            print(Fore.YELLOW +"................................\n")
        #yards to nanometers
        case 52:
            yards=float(input ("\nEnter Length in yards: "))
            nanometers=yards*1000000000
            print(f"Your Length in nanometers is: {nanometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #yards to micrometers
        case 53:
            yards=float(input ("\nEnter Length in yards: "))
            micrometers=yards*1000000
            print(f"Your Length in micrometers is: {micrometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #yards to millimeters
        case 54:
            yards=float(input ("\nEnter Length in yards: "))
            millimeters=yards*914.4
            print(f"Your Length in millimeters is: {millimeters: .2f}")
            print(Fore.YELLOW +"................................\n")
        #miles to cm
        case 55:
            miles=float(input ("\nEnter Length in miles: "))
            cm=miles*160934.4
            print(f"Your Length in cm is: {cm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #miles to m
        case 56:
            miles=float(input ("\nEnter Length in miles: "))
            m=miles*1609.344
            print(f"Your Length in m is: {m: .2f}")
            print(Fore.YELLOW +"................................\n")
        #miles to km
        case 57:
            miles=float(input ("\nEnter Length in miles: "))
            km=miles/0.621
            print(f"Your Length in km is: {km: .2f}")
            print(Fore.YELLOW +"................................\n")
        #miles to inches
        case 58:
            miles=float(input ("\nEnter Length in miles: "))
            inches=miles*63360
            print(f"Your Length in inches is: {inches: .2f}")
            print(Fore.YELLOW +"................................\n")
        #miles to feet
        case 59:
            miles=float(input ("\nEnter Length in miles: "))
            feet=miles*5280
            print(f"Your Length in feet is: {feet: .2f}")
            print(Fore.YELLOW +"................................\n")
        #miles to yards
        case 60:
            miles=float(input ("\nEnter Length in miles: "))
            yards=miles*1760
            print(f"Your Length in yards is: {yards: .2f}")
            print(Fore.YELLOW +"................................\n")
        #miles to nanometers
        case 61:
            miles=float(input ("\nEnter Length in miles: "))
            nanometers=miles*1000000000
            print(f"Your Length in nanometers is: {nanometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #miles to micrometers
        case 62:
            miles=float(input ("\nEnter Length in miles: "))
            micrometers=miles*1000000
            print(f"Your Length in micrometers is: {micrometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #miles to millimeters
        case 63:
            miles=float(input ("\nEnter Length in miles: "))
            millimeters=miles*160934.4
            print(f"Your Length in millimeters is: {millimeters: .2f}")
            print(Fore.YELLOW +"................................\n")
        #nanometers to cm
        case 64:
            nanometers=float(input ("\nEnter Length in nanometers: "))
            cm=nanometers*0.0001
            print(f"Your Length in cm is: {cm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #nanometers to m
        case 65:
            nanometers=float(input ("\nEnter Length in nanometers: "))
            m=nanometers*0.0000001
            print(f"Your Length in m is: {m: .2f}")
            print(Fore.YELLOW +"................................\n")
        #nanometers to km
        case 66:
            nanometers=float(input ("\nEnter Length in nanometers: "))
            km=nanometers/1000000000
            print(f"Your Length in km is: {km: .2f}")
            print(Fore.YELLOW +"................................\n")
        #nanometers to inches
        case 67:
            nanometers=float(input ("\nEnter Length in nanometers: "))
            inches=nanometers*0.000000039
            print(f"Your Length in inches is: {inches: .2f}")
            print(Fore.YELLOW +"................................\n")
        #nanometers to feet
        case 68:
            nanometers=float(input ("\nEnter Length in nanometers: "))
            feet=nanometers*0.0000003048
            print(f"Your Length in feet is: {feet: .2f}")
            print(Fore.YELLOW +"................................\n")
        #nanometers to yards
        case 69:
            nanometers=float(input ("\nEnter Length in nanometers: "))
            yards=nanometers*0.0000009144
            print(f"Your Length in yards is: {yards: .2f}")
            print(Fore.YELLOW +"................................\n")
        #nanometers to miles
        case 70:
            nanometers=float(input ("\nEnter Length in nanometers: "))
            miles=nanometers/1000000000000
            print(f"Your Length in miles is: {miles: .2f}")
            print(Fore.YELLOW +"................................\n")
        #nanometers to micrometers
        case 71:
            nanometers=float(input ("\nEnter Length in nanometers: "))
            micrometers=nanometers*1000000000
            print(f"Your Length in micrometers is: {micrometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #nanometers to millimeters
        case 72:
            nanometers=float(input ("\nEnter Length in nanometers: "))
            millimeters=nanometers*0.000000039
            print(f"Your Length in millimeters is: {millimeters: .2f}")
            print(Fore.YELLOW +"................................\n")
        #micrometers to cm
        case 73:
            micrometers=float(input ("\nEnter Length in micrometers: "))
            cm=micrometers*0.000001
            print(f"Your Length in cm is: {cm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #micrometers to m
        case 74:
            micrometers=float(input ("\nEnter Length in micrometers: "))
            m=micrometers*0.000000001
            print(f"Your Length in m is: {m: .2f}")
            print(Fore.YELLOW +"................................\n")
        #micrometers to km
        case 75:
            micrometers=float(input ("\nEnter Length in micrometers: "))
            km=micrometers/1000000
            print(f"Your Length in km is: {km: .2f}")
            print(Fore.YELLOW +"................................\n")
        #micrometers to inches
        case 76:
            micrometers=float(input ("\nEnter Length in micrometers: "))
            inches=micrometers*0.000000000039
            print(f"Your Length in inches is: {inches: .2f}")
            print(Fore.YELLOW +"................................\n")
        #micrometers to feet
        case 77:
            micrometers=float(input ("\nEnter Length in micrometers: "))
            feet=micrometers*0.0000000003048
            print(f"Your Length in feet is: {feet: .2f}")
            print(Fore.YELLOW +"................................\n")
        #micrometers to yards
        case 78:
            micrometers=float(input ("\nEnter Length in micrometers: "))
            yards=micrometers*0.0000000009144
            print(f"Your Length in yards is: {yards: .2f}")
            print(Fore.YELLOW +"................................\n")
        #micrometers to miles
        case 79:
            micrometers=float(input ("\nEnter Length in micrometers: "))
            miles=micrometers/1000000000
            print(f"Your Length in miles is: {miles: .2f}")
            print(Fore.YELLOW +"................................\n")
        #micrometers to nanometers
        case 80:
            micrometers=float(input ("\nEnter Length in micrometers: "))
            nanometers=micrometers*1000000
            print(f"Your Length in nanometers is: {nanometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #micrometers to millimeters
        case 81:
            micrometers=float(input ("\nEnter Length in micrometers: "))
            millimeters=micrometers*0.000001
            print(f"Your Length in millimeters is: {millimeters: .2f}")
            print(Fore.YELLOW +"................................\n")
        #millimeters to cm
        case 82:
            millimeters=float(input ("\nEnter Length in millimeters: "))
            cm=millimeters*0.00001
            print(f"Your Length in cm is: {cm: .2f}")
            print(Fore.YELLOW +"................................\n")
        #millimeters to m
        case 83:
            millimeters=float(input ("\nEnter Length in millimeters: "))
            m=millimeters*0.000001
            print(f"Your Length in m is: {m: .2f}")
            print(Fore.YELLOW +"................................\n")
        #millimeters to km
        case 84:
            millimeters=float(input ("\nEnter Length in millimeters: "))
            km=millimeters/1000
            print(f"Your Length in km is: {km: .2f}")
            print(Fore.YELLOW +"................................\n")
        #millimeters to inches
        case 85:
            millimeters=float(input ("\nEnter Length in millimeters: "))
            inches=millimeters*0.000000039
            print(f"Your Length in inches is: {inches: .2f}")
            print(Fore.YELLOW +"................................\n")
        #millimeters to feet
        case 86:
            millimeters=float(input ("\nEnter Length in millimeters: "))
            feet=millimeters*0.0000003048
            print(f"Your Length in feet is: {feet: .2f}")
            print(Fore.YELLOW +"................................\n")
        #millimeters to yards
        case 87:
            millimeters=float(input ("\nEnter Length in millimeters: "))
            yards=millimeters*0.0000009144
            print(f"Your Length in yards is: {yards: .2f}")
            print(Fore.YELLOW +"................................\n")
        #millimeters to miles
        case 88:
            millimeters=float(input ("\nEnter Length in millimeters: "))
            miles=millimeters/1000000
            print(f"Your Length in miles is: {miles: .2f}")
            print(Fore.YELLOW +"................................\n")
        #millimeters to nanometers
        case 89:
            millimeters=float(input ("\nEnter Length in millimeters: "))
            nanometers=millimeters*1000
            print(f"Your Length in nanometers is: {nanometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #millimeters to micrometers
        case 90:
            millimeters=float(input ("\nEnter Length in millimeters: "))
            micrometers=millimeters*1000000
            print(f"Your Length in micrometers is: {micrometers: .2f}")
            print(Fore.YELLOW +"................................\n")
        #error case
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

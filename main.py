#import package
import colorama
from colorama import Fore ,Back, Style
colorama.init(autoreset= True)


def choose_program():
    print(Fore.LIGHTMAGENTA_EX +"\n\t\t\t!!!Welcome to the Calculator!!!\n\n" + Fore.RESET)
    print(Fore.LIGHTGREEN_EX + "This Program have some Choice for you to calculate\n" + Fore.RESET)

    print(Fore.CYAN + "1--> " + Fore.RESET + "Quadratic Equation")
    print(Fore.CYAN + "2--> " + Fore.RESET + "Angle")
    print(Fore.CYAN + "3--> " + Fore.RESET + "Volume and Area")
    print(Fore.CYAN + "4--> " + Fore.RESET + "Temperature")
    print(Fore.CYAN + "5--> " + Fore.RESET + "Speed")
    print(Fore.CYAN + "6--> " + Fore.RESET + "Length")
    print(Fore.CYAN + "7--> " + Fore.RESET + "Exit")
    #fig_code
    fig_code = int(input(Fore.CYAN + "\nEnter the code of your Choice to go to your calculator space: " + Fore.RESET))

    if fig_code == 1:
        import quadratic_equation.main
        # quadratic_equation.main.main()
    elif fig_code == 2:
        import angle.main
        # angle.main.main()
    elif fig_code == 3:
        import valume_and_area.main
        # valume_and_area.main.input_char()
    elif fig_code == 4:
        import temperature.main
        # temperature.main.main()
    elif fig_code == 5:
        import speed.main
        # speed.main.main()
    elif fig_code == 6:
        import length.main
        # length.main.main()
    elif fig_code == 7:
        print(Fore.LIGHTRED_EX + "Thank You For Using This Calculator...\n\n" + Fore.RESET)
        exit()
    else:
        print(Fore.MAGENTA + Style.BRIGHT + "\t\t\tWrong Code.\n\n" + Fore.RESET)
        print(Fore.YELLOW + "================================================================\n")
        choose_program()


choose_program()

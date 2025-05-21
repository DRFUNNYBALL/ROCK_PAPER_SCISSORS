import colorama
from colorama import Fore,Back,Style,init
init()
from getpass import getpass
a=int(input("how many round would you like to play ?"))

def sos ():
    print(f"player 1 chose {player1} and player 2 chose {player2}")
conter=0
conter_1=0
for i in range (a):

 print(Fore.LIGHTYELLOW_EX+"ROCK>>>>PAPER>>>>SCISSORS")
 player1=getpass(Fore.RED + "please inter your choise Player1:")
 player2=getpass(Fore.RED + "please inter your choise Player2:")

 if player1==("ROCK") and player2==("PAPER"): 
    print(Fore.GREEN+"paleyer 2 is WINNER")
    sos()
    conter=0
    conter_1=0+1
 elif player1==("ROCK") and player2==("SICCORS"):
    print=(Fore.GREEN+"player 1 is WINNER")
    sos()
    conter=0+1
    conter_1=0
 elif player1==("PAPER") and player2==("ROCK"):
    print=(Fore.GREEN+"player 1 is WINNER")
    sos()
    conter=0+1
    conter_1=0
 elif player1==("PAPER") and player2==("SICCORS"):
    print=(Fore.GREEN+"player 2 is WINNER")
    sos()
    conter=0
    conter_1=0+1
 elif player1==("SCISSORS") and player2==("ROCK"):
    print=(Fore.GREEN+"player 2 is WINNER")
    sos()
    conter=0
    conter_1=0+1
 elif player1==("SCISSORS") and player2==("PAPER"):
    print=(Fore.GREEN+"player 1 is WINNER")
    sos()
    conter=0+1
    conter_1=0
 elif player1==("ROCK") and player2==("ROCK"):
    print=(Fore.BLUE+"EQULS")
    sos()
    conter=0+0
    conter_1=0+0
 elif player1==("PAPER") and player2==("PAPER"):
    print=(Fore.BLUE+"EQULS")
    sos()
    conter=0+0
    conter_1=0+0
 elif player1==("SCISSORS") and player2==("SICCORS"):
    print=(Fore.BLUE+"EQULS")
    sos()
    conter=0+0
    conter_1=0+0
 else:
    print(Fore.LIGHTRED_EX+"Wrong choice")            

    print (conter)
    print(conter_1)
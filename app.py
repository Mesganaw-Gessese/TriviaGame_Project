import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


from utilities import Sport
from utilities import Film
from db_recorder import scoreRecorder

class Run_System():
    print(Fore.BLUE + "Welcome to this fun Trivia Game! \nAre you ready to test your knowledge ")
    while True:
        choose = input(Fore.GREEN + "Choose a category yiu want to play:\nA) Film Questions:\nB) Fore.YELLOW +Sport Questions:\nChoose: ")
        print(Fore.RED + "Please using to write by small letters! ")
        if choose == "a" or choose == "A":
            a = Film()
            a.filmBrain()

        elif choose == "b" or choose == "B":
            b = Sport()
            b.sportBrain()
        scoreRecorder()
        continue_ = input("do you want to continue?: ")
        if continue_ == "no" or continue_ == "NO" or continue_ == "No":
            break
        print("Thanks for playing! 💜")




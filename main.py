import random

retry_ = True
start_ = False


def getchoice():
    global user_choice
    choiceok = False

    list_choices = ["Pierre", "Feuille", "Ciseaux"]
    while not choiceok:
        user_choice = input("Choisissez entre Pierre, Feuille, ou Ciseaux : ")
        if user_choice == "Pierre" or user_choice == "Feuille" or user_choice == "Ciseaux":
            choiceok = True

    ia_choice = random.choice(list_choices)
    print("L'ordinateur a choisi " + ia_choice)
    choices_ = {"user_choice": user_choice, "ia_choice": ia_choice}
    return choices_


def check(user, ia):
    if user == ia:
        print("Egalité")
    elif user == "Feuille":
        if ia == "Ciseaux":
            print("L'ordinateur a gagné")
        else:
            print("Vous avez gagné")
    elif user == "Ciseaux":
        if ia == "Pierre":
            print("L'ordinateur a gagné")
        else:
            print("Vous avez gagné")
    elif user == "Pierre":
        if ia == "Feuille":
            print("L'ordinateur a gagné")
        else:
            print("Vous avez gagné")


def retry():
    y_ = False
    while not y_:
        global retry_
        choice = input("Souhaitez vous rejouer ? (y/n) ")
        if choice == "n":
            retry_ = False
            y_ = True
            print("Fin de la partie")
        elif choice == "y":
            y_ = True
            print("La partie continue")


def play():
    while retry_:
        choices = getchoice()
        check(choices["user_choice"], choices["ia_choice"])
        retry()



while not start_:
    print("Ecrivez Start pour commencer la partie. ")
    print("Cancel pour annuler")
    start = input()
    if start == "Start":
        play()
        start_ = True
    elif start == "Cancel":
        break

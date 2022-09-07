import random

# Actions jouables par les joueurs
actions = ['papier', 'pierre', 'ciseaux', 'puit']
# Points des joueurs 1 et 2 initialisés sur 0 de base
player1_score = 0
player2_score = 0
# Noms des joueurs par defaut initialisés
player1 = ""
player2 = ""
# Initialisation du gamemode
gamemode = 0
# Initialisatiob du nombre de parties
games = 0
# Initialisation de la liste pour vérifier le choix de l'utilisateur
liste_verif = ["0", "1", "2", "3"]

def game():
    choice_game()
    set()

def count_game():

    if(games == 5):
        print("fin de la partie le nombre de parties limite a été atteint !")
        if(player1_score > player2_score):
            print(f"{player1} a gagné avec {player1_score} parties, félicitation !")
            quit()
        if(player2_score > player1_score):
            print(f"{player2} a gagné avec {player2_score} parties, félicitation !")
            quit()
        else:
            print("égalité !")
            quit()

# choix du type de jeux 0 = offline | 1 = online
def choice_game():
    global player1_score
    global player1
    global player2_score
    global player2

    choice = input("Voulez jouer contre le robot ? O/N : ")

    if(choice != "O" and choice !=" N"):
        choice_game()

    else:

        if (choice == "O"):

            player1 = ""
            player2 = "Machine"

            while (player1 == "" or player1 == "Machine"):
                player1 = input("Joueur 1, merci de mettre votre nom : ")

            print(f"Bienvenu {player1} vous jouez contre la machine")

        else:

            player1 = input("Joueur 1, merci de mettre votre nom : ")
            player2 = input("Joueur 2, merci de mettre votre nom : ")

            print(f"Bienvenu {player1} vous jouez contre la {player2}")

            gamemode = 1

# Comptage du nombre de points par joueurs
def count_points(choice_player1:str, choice_player2:str, player:int):

    global player1_score
    global player1
    global player2_score
    global player2

    print(f"{player1} à jouer {choice_player1}, {player2} à jouer {choice_player2}")

    if (player == 1):
        player1_score += 1
        print(f"Le joueur {player1} gagne 1 partie il est donc à {player1_score} partie(s) gagnée(s)")
    if (player == 2):
        player2_score += 1
        print(f"Le joueur {player2} gagne 1 partie il est donc à {player2_score} partie(s) gagnée(s)")

    if(player1_score ==3):
        print(f"{player1} à gagner il a atteint les 3 points !")
        quit()

    if(player2_score ==3):
        print(f"{player2} à gagner il a atteint les 3 points !")
        quit()



def return_choice(choice_player: int):

    global actions

    match choice_player:
        case 0:
            return actions[0]
        case 1:
            return actions[1]
        case 2:
            return actions[2]
        case 3:
            #print(actions[3])
            return actions[3]

def indent_game():
    global games
    games +=1

# Relancer une partie
def restart():

    count_game()

    go = input(f"Souhaitez vous refaire une manche {player1} contre {player2} ? (O/N) : ")
    if go == 'O' and games < 5:
        set()
    elif go == 'N':
        print("Fin de la game à l'initiative des joueurs")
        if(player1_score > player2_score):
            print(f"Le gagnant est {player1} avec {player1_score} partie(s) gagnée(s) !")
            quit()
        if (player2_score > player1_score):
            print(f"Le gagnant est {player2} avec {player2_score} partie(s) gagnée(s) !")
            quit()
        else:
            print("C'est une égalité !")
            quit()

    else:
        print("Vous ne répondez pas à la question, on continue ")
        restart()

# Permet de vérifier que l'action est autorisée
def offline_check(choice_player1):
    return (choice_player1 in actions)

def online_check(choice_player1, choice_player2):
    return (choice_player1 in actions and choice_player2 in actions)

# Lancement des jeux
def set():

    choice_player1 = input(f"{player1} faîtes votre choix parmi (pierre = 0, papier = 1, ciseaux = 2, puit = 3): ")
    if (choice_player1 not in liste_verif):
        set()
    choice_player1 = return_choice(int(choice_player1))


    if gamemode == False:
        choice_player2 = random.choice(actions)
    else:
        choice_player2 = input(f"{player2} faîtes votre choix parmi (pierre = 0, papier = 1, ciseaux = 2, puit = 3")
        if (choice_player2 not in liste_verif):
            set()
        choice_player2 = return_choice(int(choice_player2))
        print(int(choice_player2))

    print("Joueur 1 ", choice_player1, "Joueur 2 ", choice_player2)

    match choice_player1:

        case "pierre":

            match choice_player2:

                case "papier":
                    count_points(choice_player1, choice_player2, 2)
                    indent_game()
                case "pierre":
                    print("Même action, égalité !")
                    indent_game()
                case "ciseaux":
                    count_points(choice_player1, choice_player2, 1)
                    indent_game()
                case "puit":
                    count_points(choice_player1, choice_player2, 2)
                    indent_game()


        case "papier":
            match choice_player2:
                case "papier":
                    print("Même action, égalité !")
                    indent_game()
                case "pierre":
                    count_points(choice_player1, choice_player2, 1)
                    indent_game()
                case "ciseaux":
                    count_points(choice_player1, choice_player2, 2)
                    indent_game()
                case "puit":
                    count_points(choice_player1, choice_player2, 1)
                    indent_game()

        case "ciseaux":
            match choice_player2:
                case "papier":
                    count_points(choice_player1, choice_player2, 1)
                    indent_game()
                case "pierre":
                    count_points(choice_player1, choice_player2, 2)
                    indent_game()
                case "ciseaux":
                    print("Même action, égalité !")
                    indent_game()
                case "puit":
                    count_points(choice_player1, choice_player2, 2)
                    indent_game()

        case "puit":
            match choice_player2:
                case "papier":
                    count_points(choice_player1, choice_player2, 1)
                    indent_game()
                case "pierre":
                    count_points(choice_player1, choice_player2, 1)
                    indent_game()
                case "ciseaux":
                    count_points(choice_player1, choice_player2, 1)
                    indent_game()
                case "puit":
                    print("Même action, égalité !")
                    indent_game()

    restart()

game()
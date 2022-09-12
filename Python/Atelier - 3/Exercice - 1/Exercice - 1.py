# Pascal, Python 3.10 | Développé le 12 Septembre 2022 sous l'IDE Pycharm

def full_name(str_arg : str) -> str:
    """
    La fonction full_name() à pour but de convertir un nom en MAJ et la première lettre du prénom en MAJ

    :param str_arg(str): Représente le nom + prénom
    :return name(str): La valeur de retour est un string représentant le nom et prénom de l'utilisateur converti
    """
    name = str_arg.split(" ")

    return(name[0].upper() + " " + name[1].capitalize())

def is_mail(str_arg:str)->(int,int):
    """
    La fonction is_mail() permet de vérifier si une adresse email est bien valide

    :param str_arg(str): Représente l'adresse mail sur laquelle la vérification doit être faite
    :return est_valid(bool): La valeur du
    """

    est_valid = (1, "x")

    separator = str_arg.split("@")

    print("---------------------------")

    if '@' not in str_arg:
        est_valid = (0, 2)
        print("ERREUR PAS DE @ DANS L'EMAIL")

    else:

        if(str_arg[0] == '@' or str_arg[len(str_arg) -1] == '@'):
            est_valid = (0, 2)
            print("ERREUR DE PLACEMENT POUR LE @")

        else:
            if(len(separator) > 2):
                est_valid = (0, 2)
                print("ERREUR NOMBRE DE @ > 1 DANS L'EMAIL")
            else:
                if len(separator[0]) -1 < 2:
                    est_valid = (0, 1)
                    print("ERREUR MAUVAISE TAILLE POUR L'EMAIL")
                else:

                    if (str_arg[0] == "." or str_arg[len(str_arg) - 1] == "."):
                        est_valid = (0, 1)
                        print("ERREUR LE . EST MAL MIS DANS VOTRE EMAIL")

                    if (regex(separator[0], 1) == False):
                        est_valid = (0, 1)
                        print("ERREUR CARACTERES INTERDITS DANS VOTRE EMAIL")

                    for i in range(len(separator[0])):
                        if separator[0][i] == "." and separator[0][i + 1] == ".":
                            est_valid = (0, 1)
                            print("ERREUR .. EST INTERDIT")

                    for i in range(len(separator[1])-1):
                        if separator[1][i] == "." and separator[1][i + 1] == ".":
                            est_valid = (0, 3)
                            print("ERREUR .. EST INTERDIT")

                    if (regex(separator[1], 2) == False):
                        est_valid = (0, 3)
                        print("ERREUR CARACTERES INTERDITS DANS VOTRE EMAIL")

                    if(separator[1][0] == "." or separator[1][len(separator[1]) -1] == "."):
                        est_valid = (0, 3)
                        print("ERREUR LE DOMAINE N'EST PAS BON LE PLACEMENT DU . N'EST PAS BON")

                    if "." not in separator[1]:
                        est_valid = (0, 4)
                        print("ERREUR PAS DE . DANS LE DOMAINE")

    return est_valid

def regex(str_arg:str, test:int)->bool:
    """
    La fonction regex() permet de vérifier la conformité d'une chaine de caractère

    :param str_arg(str): Représente la chaine caractère à vérifier
    :param test(int): Représente la séquence de test à vérifier
    :return:
    """
    valid = True

    if test == 1:

        for i in str_arg:
            c = ord(i)
            if 97 <= c <= 122 or 65 <= c <= 90 or 48 < c < 57 or 45 <= c <= 46 or c == 95 or c == 64: # Voir table ASCII pour les intervalles
                i=i
            else:
                valid = False

    if test == 2:
        for b in str_arg:
            a = ord(b)
            if 97 <= a <= 122 or 65 <= a <= 90 or 45 <= a <= 46 or a == 64: # Voir table ASCII pour les intervalles
                b = b
            else:
                valid = False


    return valid

if __name__ == '__main__':
    #Test de la fonction full_name()
    print(full_name("vigneau Pascal"))
    #Test de la fonction is_email()
    print(is_mail(".@gmail.com")) # Test . au début
    print(is_mail("Pascal.Vigneau@gmailcom."))  # Test . à la fin
    print(is_mail("Pascal..Vigneau@gmailcom.")) # Test 2 . à la suite
    print(is_mail("Pascal.&Vigneau@gmail.com"))  # Test caractère non autorisé
    #Test présence @ dans email
    print(is_mail("Pascal.Vigneaugmail.com"))
    print(is_mail("@Pascal.Vigneaugmail.com")) # Test mauvais placement @ au début
    print(is_mail("Pascal.Vigneaugmail.com@"))  # Test mauvais placement @ à la fin
    #Test du domaine du mail et @
    print(is_mail("Pascal.Vigneaugmail@..com"))  # Test 2 . dans le domaine
    print(is_mail("Pascal.Vigneaugmail@.@com")) # Test + de 1 @ dans l'email
    print(is_mail("Pascal.Vigneaugmail@.^com"))  # Test caractère spécial dans le domaine
    print(is_mail("Pascal.Vigneaugmail@.com"))  # Test mauvais placement du . dans domaine
    #Test présence du . dans le domaine
    print(is_mail("Pascal.Vigneaugmail@com"))  # Test présence du . dans le domaine
    #Test d'une bonne email
    print(is_mail("Pascal.Vigneau@gmail.com"))  # Test d'une bonne email










# Pascal, Python 3.10 | Développé le 14 Septembre 2022 sous l'IDE Pycharm

def ouvrante(car:str) -> bool:
    """
    La fonction ouvrante() permet de renvoyer un booléen indiquant si le caractère est ( [ ou {

    :param car(str): Représente le caractère passé en paramètre
    :return: La valeur de retour est un booléen indiquant si le car est bien ( [ ou {
    """

    return car == "(" or car == "[" or car == "{"

def fermante(car:str) -> bool:
    """
    La fonction fermante() permet de renvoyer un booléen indiquant si le caractère est ) ] ou }

    :param car(str): Représente le caractère passé en paramètre
    :return: La valeur de retour est un booléen indiquant si le car est bien ) ] ou }
    """

    return car == ")" or car == "]" or car == "}"

def reverse(car:str) -> str:
    """
    La fonction reverse() permet de retourner le caractère inverse à celui passé en paramètre

    :param car(str): Représente le caractère
    :return return_carac: La valeur de retour est un str qui sera l'inverse de celui passé en paramètre sous certaines
    conditions
    """

    return_carac = car

    if fermante(car):
        if car == ")":
            return_carac = "("
        elif car == "]":
            return_carac = "["
        else:
            return_carac = "{"

    return return_carac

def operateur(car:str) -> bool:
    """
    La fonction operateur() permet de vérifier que le car passé en paramètre est bien un opérateur

    :param car(str): Représente le caractère qui va être testé
    :return: La valeur de retour est un booléen indiquant si le caractère est un opérateur
    """
    return car == "*" or car == "+"

def nombre(car:str) -> bool:
    """
    La fonction nombre() permet de savoir si un caractère est un nombre grâce à isdigit()

    :param car(str): Représente le caractère
    :return: La valeur de retour est un booléen qui permet de savoir si le caractère est un nombre
    """

    return car.isdigit()

def caractere_valide(car:str) -> bool:
    """
    La fonction caractere_valide() permet de savoir si le car est un caractère valide

    :param car(str): Représente le caractère
    :return: La valeur de retour est un booléen indiquant si car est valide
    """

    return ouvrante(car) or fermante(car) or operateur(car) or nombre(car) or car == " "

def verif_parenthese(expression:str) -> bool:
    """
    La fonction verif_parenthese() permet de savoir si l'expression comporte que des caractères valides et les
    parenthèses sont bien mises.

    :param expression(str): Représente l'expression à vérifier
    :return est_correct(bool): La valeur de retour est un booléen qui signifie si l'expression est bien correcte.
    """

    est_correct = True
    limit = 0 # Compteur pour les différentes vérifications à faire
    stock_expression = [] # liste pour stocker l'expression et pouvoir travailler dessus
    
    # Vérification pour voir que tous les caractères de l'expression sont bons
    while est_correct and limit < len(expression) - 1:
        if not caractere_valide(expression[limit]):
            est_correct = False
        limit+=1

    for item in range(len(expression)):
        stock_expression.append(expression[item])

    if fermante(stock_expression[0]) or ouvrante(stock_expression[-1]):
        est_correct = False


    if est_correct:
        while est_correct and limit < len(stock_expression) - 1:
            f = 0
            if stock_expression[limit] == "(":
                stock_expression.pop(limit)
                if ")" in stock_expression:
                    while stock_expression[f] != ")" and f < len(stock_expression) - 1:
                        if stock_expression[f] == ")":
                            stock_expression.pop(f)
                        f +=1
                else:
                    est_correct = False

            if stock_expression[limit] == "[":
                stock_expression.pop(limit)
                if "]" in stock_expression:
                    while stock_expression[f] != "]" and f < len(stock_expression) - 1:
                        if stock_expression[f] == "]":
                            stock_expression.pop(f)
                        f +=1
                else:
                    est_correct = False

            if stock_expression[limit] == "{":
                stock_expression.pop(limit)
                if "}" in stock_expression:
                    while stock_expression[f] != "}" and f < len(stock_expression) - 1:
                        if stock_expression[f] == "}":
                            stock_expression.pop(f)
                        f += 1
                else:
                    est_correct = False
            limit+=1




    return est_correct

if __name__ == '__main__':
    #Test fonction ouvrante()
    print("----------------")
    print(ouvrante("("))
    #Test fonction fermante()
    print("----------------")
    print(fermante(")"))
    #Test fonction reverse()
    print("----------------")
    print(reverse(")"))
    #Test fonction operateur()
    print("----------------")
    print(operateur("+"))
    #Test fonction nombre()
    print("----------------")
    print(nombre("1"))
    #Test fonction caractere_valide()
    print("----------------")
    print(caractere_valide(" "))
    # Test fonction verif_parenthese()
    print("----------------")
    print(verif_parenthese("(2+2) + {2")) # Test dans le cas où { n'a pas sa fermeture
    print(verif_parenthese("(2+2) + 2")) # Test validé







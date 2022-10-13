import datetime


class Cmd:
    "Class Cmd qui contient les méthodes liées à des commandes"

    # Constructeur de Cmd
    def __init__(self):
        self.lst_cmd = ["LOWER", "UPPER", "DATENOW"]  # Liste des commandes

    @staticmethod
    def isCmd(CMD, data: bin) -> bool:
        """
        La fonction isCmd() permet de savoir si une donnée reçue contient une commande
        :param CMD: Représente un objet de type Cmd
        :param data: Représente la donnée
        :return: La valeur de retour est un booléen qui permet de savoir si une commande est présente dans la donnée
        """
        res = False
        data = str(data)[2:-1]
        if len(data) != 0:
            data = data.split(" ")
            if data[0] in CMD.lst_cmd:
                res = True
        return res

    @staticmethod
    def executeCmd(CMD, data: bin) -> str:
        """
        La fonction executeCmd() permet d'exécuter une commande
        :param CMD:  Représente un objet de type Cmd
        :param data:  Représente la donnée
        :return: La valeur de retour est un string
        """
        res = str(data)[2:-1]
        if CMD.isCmd(CMD, data):
            command = res.split(" ")[0]
            height = len(command)
            match command:
                case "LOWER":
                    res = res[height+1:].lower()
                case "UPPER":
                    res = res[height+1:].upper()
                case "DATENOW":
                    res = str(datetime.datetime.now())
        return res





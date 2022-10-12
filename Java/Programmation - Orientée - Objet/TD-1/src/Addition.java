public class Addition {

    /**
     * Fonction addition()
     * @param a Représente un entier
     * @param b Représente un entier
     * @return La valeur de retour est l'addition de a+b
     */
    public static int addition(int a, int b){
        return a+b;
    }

    /**
     * Fonction additionBis()
     * @param array Représente une liste d'entiers
     * @return La valeur de retour est l'addition de tous les éléments de la liste array
     */
    public static int additionBis(int[] array){

        int res = 0;

        if(array.length == 0){
            System.err.println("La liste est vide");
        }
        else{
            for (int j : array) {
                res = res + j;
            }
        }
        return res;
    }
}

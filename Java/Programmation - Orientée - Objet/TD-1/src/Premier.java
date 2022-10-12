public class Premier {
    /**
     * Fonction estPremier()
     * @param number Représente un entier
     * @return La valeur de retour est un booléen qui représente le fait qu'un nombre est entier ou non
     */
    public static boolean estPremier(int number){
        boolean res = true;
        int nbMultiple = 0;
        for(int i = 1; i <= number; i++){
            if(number % i == 0){
                nbMultiple++;
            }
        }
        if(nbMultiple > 2){
            res = false;
        }
        return res;
    }
}

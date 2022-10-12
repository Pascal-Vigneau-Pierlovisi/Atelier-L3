public class Moyenne {
    /**
     * Fonction moyenne()
     * @param lst Représente une liste de double
     * @return La valeur de retour est un double représentant la moyenne
     */
    public static double moyenne(double[] lst){
        double res = 0;
        if(lst.length == 0){
            System.err.println("La liste est vide");
        }
        else{
            for(double i : lst){
                res = res + i;
            }
            res = res / (lst.length);
        }
        return (double)res;
    }
}

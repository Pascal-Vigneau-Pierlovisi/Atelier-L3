public class Geometrie {

    /**
     * Fonction calculPerimetre()
     * @param r Représente le rayon du cercle
     * @return La valeur de retour est le périmètre
     */
    public static double calculPerimetre(double r){
        double res = 0;
        if(r <= 0){
            System.err.println("Le rayon ne peut pas être <= 0");
        }
        else{
            res = 2*Math.PI*r;
        }
        return res;
    }

    /**
     * Fonction calculAir()
     * @param r Représente le rayon du cercle
     * @return La valeur de retour est l'air du cercle
     */
    public static double calculAir(double r){
        double res = 0;
        if(r <= 0){
            System.err.println("Le rayon ne peut pas être <= 0");
        }
        else{
            res = (Math.PI) * (r*r);
        }
        return res;

    }
}

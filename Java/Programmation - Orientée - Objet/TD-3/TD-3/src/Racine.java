public class Racine {


    public static double calculer(double nombre) throws ValeurNegativeException{
        if(nombre <= 0){
            throw new ValeurNegativeException();
        }
        else{
            System.out.println(Math.sqrt(nombre));
            return Math.sqrt(nombre);
        }
    }

    /*public static void main(String[] args) throws ValeurNegativeException {
        Racine.calculer(-12);
    }*/
}

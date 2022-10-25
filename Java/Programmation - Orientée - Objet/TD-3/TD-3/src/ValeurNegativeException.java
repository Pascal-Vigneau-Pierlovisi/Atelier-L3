public class ValeurNegativeException extends Exception {

    public ValeurNegativeException(){
        System.err.println("Le nombre ne doit pas être négatif !");
    }
    public  ValeurNegativeException(String message){
        super(message);
        System.err.println(message);
    }

}


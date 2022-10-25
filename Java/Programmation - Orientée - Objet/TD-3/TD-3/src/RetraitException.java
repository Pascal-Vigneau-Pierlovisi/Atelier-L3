public class RetraitException extends Exception{
    public RetraitException(){
        System.err.println("Le solde est null");
    }
    public RetraitException(String mess){
        super(mess);
        System.err.println(mess);
    }

}

public class Banque {
    private int solde;

    public Banque(int solde){
        this.solde = solde;
    }
    public void retrait(int somme) throws RetraitException{
        if (solde - somme < 0){
            throw new RetraitException();
        }
        else {
            solde = solde - somme;
            System.out.println("Solde : " + solde);
        }
    }

    /*public static void main(String[] args) throws RetraitException {
        Banque monCompte = new Banque(1000);
        monCompte.retrait(50);
        monCompte.retrait(1000);
    }*/
}

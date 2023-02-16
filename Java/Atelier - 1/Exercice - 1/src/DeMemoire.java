import java.util.Random;

public class DeMemoire extends De{

    protected Integer lastChoice = 0;

    private static Random r = new Random();  // Création d'un objet du type Random

    /**
     * La fonction DeMemoire() est le constructeur de DePipes
     * @param nbFaces Représente le nombre de faces du Dé
     */
    public DeMemoire(int nbFaces){

        super(nbFaces);

    }

    /**
     * La fonction DeMemoire() est un constructeur de DePipes
     */
    public DeMemoire(){
        super();
    }

    /**
     * La fonction DeMemoire() est un constructeur de DePipes
     * @param name Représente le nom du Dé
     */
    public DeMemoire(String name){
        super(name);
    }

    /**
     * La fonction lancer() permet de faire un lancer et de ne jamais tomber sur la précédente valeur
     * @return La valeur de retour est un Integer
     */
    @Override
    protected Integer lancer(){
        int tirage = r.nextInt(nbFaces);
        while (tirage == lastChoice){
            tirage = r.nextInt(nbFaces);
        }
        lastChoice = tirage;
        return tirage;
    }
}

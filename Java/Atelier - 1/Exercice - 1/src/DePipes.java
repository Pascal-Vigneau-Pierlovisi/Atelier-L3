import java.util.Random;

public class DePipes extends De {

    private static Random r = new Random();  // Création d'un objet du type Random

    /**
     * La fonction DePipes() est le constructeur de DePipes
     * @param nbFaces Représente le nombre de faces du Dé
     */
    public DePipes(int nbFaces){

        super(nbFaces);

    }

    /**
     * La fonction DePipes() est un constructeur de DePipes
     */
    public DePipes(){
        super();
    }

    /**
     * La fonction DePipes() est un constructeur de DePipes
     * @param name Représente le nom du Dé
     */
    public DePipes(String name){
        super(name);
    }

    /**
     * La fonction lancer() permet de lancer le Dé et d'obtenir obligatoirement un nombre supérieur
     * @param nbStart Représente le nombre de à dépasser
     * @return La valeur de retour est un Integer qui doit être compris entre nbStart et nbFaces
     */
    protected Integer lancer(Integer nbStart){
        if(nbStart == nbFaces || nbStart > nbFaces){
            System.err.println("Merci de mettre un nombre différent");
        }

        return r.nextInt(nbStart, nbFaces);
    }

}

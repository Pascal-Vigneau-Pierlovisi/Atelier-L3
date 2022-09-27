import java.util.Random;

public class DePipes extends De{

    /**
     * Constructeur de DePipes
     * @param nom Représente le nom du DéPipes
     * @param nbFaces Représente le nombre de faces du DéPipes
     * @param min Représente la borne min du DéPipes
     */
    public DePipes(String nom, int nbFaces, int min){
        super(nom, nbFaces);
        if(min > LIMITE_INF && min < LIMITE_SUP){
            LIMITE_INF = min;
            setNbFaces(nbFaces);
        }
    }

    /**
     * Constructeur de DePipes
     * @param nbFaces Représente le nombre de faces du DéPipes
     * @param min Représente la borne min du DéPipes
     */
    public DePipes(int nbFaces, int min){
        super(nbFaces);
        if(min > LIMITE_INF && min < LIMITE_SUP){
            LIMITE_INF = min;
            setNbFaces(nbFaces);
        }
    }

    /**
     * Fonction lancer()
     * @return La valeur de retour est un entier représentant le tirage
     */
    @Override
    protected int lancer(){
        return new Random().nextInt(LIMITE_INF, getNbFaces() +1);
    }


}

import java.util.Random;

public class Tauren extends Personnage {  // Class représentant un Tauren qui est un Personnage

    private final int taille;  // Représente la taille du Tauren

    /**
     * Constructeur de Tauren
     * @param nom Représente le nom du Tauren
     * @param age Représente l'âge du Tauren
     * @param taille Représente la taille du Tauren
     */
    private Tauren(String nom, int age, int taille){
        super(nom, age);  // On instancie un Tauren qui aura les propriétés d'un personnage
        this.taille = taille;  // On déclare la taille du Tauren
    }

    /**
     * Fonction createTauren()
     * @param nom Représente le nom du Tauren
     * @param age Représente l'âge du Tauren
     * @param taille Représente la taille du Tauren
     * @return La valeur de retour est un objet de type Tauren
     */
    static Tauren createTauren(String nom, int age, int taille){
        if(taille <= 0){
            System.err.println("La taille d'un Tauren ne peut pas être négative");
            return null;
        }
        else{
            return new Tauren(nom, age, taille);
        }
    }

    /**
     * Fonction positionSouhaitee()
     * @return La valeur de retour est la position souhaitée par le Tauren
     */
    public int positionSouhaitee(){
        return getPosition() + new Random().nextInt(1, taille + 1);
    }

    /**
     * Fonction toString()
     * @return La valeur de retour est un message contenant
     */
    public String toString(){
        return ("Tauren " + getNom());
    }



}

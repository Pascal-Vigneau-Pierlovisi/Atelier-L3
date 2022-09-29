import java.util.ArrayList;

public abstract class Personnage {  // Class représentant un Personnage
    private final String nom;  // Représente le nom du personnage
    private final int age;  // Représente l'âge du personnage
    private int position;  // Représente la position du personnage
    private Joueur j = null;  // Représente le propriétaire du personnage de base sur null

    /**
     * Constructeur de Personnage()
     * @param nom Représente le nom du personnage
     * @param age Représente l'âge du personnage
     */
    public Personnage(String nom, int age){
        this.nom = nom;  // On attribue le nom d'un personnage
        this.age = age;  // On attribue l'âge à un personnage
    }

    /**
     * Accesseur
     * @return La valeur de retour est la position du personnage
     */
    public int getPosition() {
        return position;
    }

    /**
     * Accesseur
     * @return La valeur de retour est le nom du personnage
     */
    public String getNom() {
        return nom;
    }

    /**
     * Accesseur
     */
    public void setJ(Joueur j) {
        this.j = j;
    }

    /**
     * Accesseur
     * @return La valeur de retour est le Joueur j
     */
    public Joueur getJ() {
        return j;
    }

    /**
     * Accesseur
     * @param position Représente la position
     */
    public void setPosition(int position) {
        this.position = position;
    }

    /**
     * Fonction deplacer()
     * @param destination Représente la destination du personnage
     * @param gain Représente le nombre de points gagné ou perdu par le joueur
     */
    public void deplacer(int destination, int gain){
        position = destination;  // On met la position du personnage sur la destination
        j.modifierPoints(gain);  // On modifie le nombre de points du joueur
    }

    /**
     * Fonction penalite()
     * @param penalite Représente la valeur de la pénalité pour le joueur j
     */
    public void penalite(int penalite){
        if(penalite > 0){  // On vérifie que la pénalité ne soit pas positive
            System.err.println("Une pénalité ne peut pas être positive");  // Message d'erreur
        }
        else{  // Dans le cas où la pénalité est bien négative
            j.modifierPoints(penalite);  // On modifie le nombre de points du joueur
        }
    }

    /**
     * Fonction toString
     * @return La valeur de retour est un string contenant le nom du personnage
     */
    public String toString(){
        return ("Nom du personnage : " + nom);
    }

    /**
     * Fonction positionSouhaitee()
     * @return La valeur de retour est un int
     */
    public abstract int positionSouhaitee();

}

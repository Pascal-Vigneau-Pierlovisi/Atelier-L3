import java.util.ArrayList;

public class Joueur {  // Class Joueur représentant un joueur
    private final String nom;  // Représente le nom du joueur
    private final String code;  // Représente le code du joueur sous la forme J + numéro du joueur
    static int nbJoueurs = 1;  // Représente le nombre de joueurs qui jouent au jeu
    protected int nbPoints;  // Représente le nombre de points du joueur
    private ArrayList<Personnage> listePersos;  // Représente la liste des Personnages du joueur

    /**
     * Constructeur de Joueur
     * @param nom Représente le nom du joueur
     */
    public Joueur(String nom){
        code = "J" + nbJoueurs;  // Affectation du code du joueur à son instanciation
        this.nom = nom;  // Affectation du nom du joueur à son instanciation
        nbJoueurs++;  // Incrémentation du nombre de joueurs à chaque instanciation d'un joueur
        nbPoints = 0;  // Affectation du nombre de points du joueur à 0.
        listePersos = new ArrayList<Personnage>();  // Instanciation de la liste des Personnages

    }

    /**
     * Accesseur
     * @return La valeur de retour est le code du joueur
     */
    public String getCode() {
        return code;
    }

    /**
     * Accesseur
     * @return La valeur de retour est le nom du joueur
     */
    public String getNom() {
        return nom;
    }

    /**
     * Accesseur
     * @return La valeur de retour la liste des Personnages du joueur
     */
    public ArrayList<Personnage> getListePersos() {
        return listePersos;
    }

    /**
     * Fonction ajouterPersonnage
     * @param p Représente un Personnage
     */
    public void ajouterPersonnage(Personnage p){
        if(peutJouer()){  // Si la liste n'est pas vide
            if(!listePersos.contains(p)){  // Vérification de la présence du personnage dans la liste
                if(p.getJ() == null){  // On vérifie que le personnage n'est pas déjà utilisé
                    listePersos.add(p);  // Ajout du personnage dans la liste
                    p.setJ(this);  // On associe le joueur à son personnage
                }
                else{
                    System.err.println("Personnage déjà en possession d'un joueur");
                }

            }
            else{
                System.err.println("Personnage déjà en possession de " + code);  // Erreur qui s'affiche
            }
        }
        else{
            if(p.getJ() == null){  // On vérifie que le Personnage n'est pas déjà attribué
                listePersos.add(p);  // Dans le cas où la liste est vide on peut directement ajouter le personnage
                p.setJ(this);  // On associe le joueur à son personnage
            }
            else{
                System.err.println("Personnage déjà en possession d'un joueur");
            }
        }

    }

    /**
     * Fonction modifierPoints()
     * @param nb Représente le nombre de points à ajouter
     */
    public void modifierPoints(int nb){
        if(nb < 0){  // On vérifie que le nombre n'est pas négatif
            if((nbPoints - nb) < 0){  // On vérifie si la soustraction de ce nombre ne donne pas un nombre négatif
                nbPoints = 0;  // On met le nombre de points à 0.
                System.err.println("Le nombre de points ne peut pas être en dessous de 0");  // On affiche une erreur
            }
            else{
                nbPoints = nbPoints - nb;  // Dans le cas où la soustraction ne donne pas un nombre négatif
            }
        }
        else{  // Si nb est positif
            nbPoints = nbPoints + nb;  // On ajoute au nombre de points directement
        }
    }

    /**
     * Fonction peutJouer
     * @return La valeur de retour est un booléen qui permet de savoir si le joueur possède au moins 1 Personnage
     */
    public boolean peutJouer(){
        return !listePersos.isEmpty();
    }

    /**
     * Fonction toString()
     * @return La valeur de retour est un message d'information permettant d'identifier le joueur
     */
    public String toString(){
        String message = "";  // On définit la variable de retour
        if(!peutJouer()){  // Si le joueur n'a aucun personnage
            message = code + " " + nom + " (" + nbPoints + "  point) Aucun personnage";
        }
        else{  // Si le joueur a au moins 1 personnage
            message = code + " " + nom + " (" + nbPoints + "  points) avec " + listePersos.size() + " personnage";
        }

        return message;
    }


}

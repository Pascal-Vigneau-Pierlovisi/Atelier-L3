import java.util.Random;

public class De {

    private String nom = null;  // Nom du dé par défaut null
    private int nbFaces;  // Nombre de faces du dé
    protected final int LIMITE_SUP = 120;  // Limite du nombre de faces du dé
    protected int LIMITE_INF = 3;  // Limite inférieur du nombre de faces du dé
    private static int nbDe = 0;  // Nombre de Dé
    private static Random r = new Random();  // Tirage aléatoire du Dé

    /**
     * Constructeur de De
     */
    public De(){
        this(6);
    }

    /**
     * Constructeur de De
     * @param nom Représente le nom du Dé
     * @param nbFaces Représente le nombre de faces du Dé
     */
    public De(String nom, int nbFaces){
        this(nbFaces);
        if(!nom.equals("")){
            this.nom = nom;
        }
    }

    /**
     * Constructeur de De
     * @param nbFaces Représente le nombre de faces du dé
     */
    public De(int nbFaces){
        setNbFaces(nbFaces);
        if(nom == null){
            nom = "De" + nbDe;
        }
        nbDe++;
    }

    /**
     * Fonction lancer()
     * @return La valeur de retour est un nombre aléatoire compris entre 0 et le nombre de faces du dé
     */
    protected int lancer(){
        return r.nextInt(0, nbFaces + 1);
    }

    /**
     * Fonction lancer()
     * @param nbFois Représente le nombre de lancés du Dé
     * @return La valeur de retour est un entier représentant le tirage du Dé
     */
    protected int lancer(int nbFois){
        int res = 0;
        if(nbFois != 0){
            for(int i = 0; i < nbFois; i++){
                int r = new Random().nextInt(0, this.nbFaces+1);
                if(r > res){
                    res = r;
                }
            }
        }
        else{
            System.err.println(nbFois);
        }
        return res;
    }

    /**
     * La fonction toString() permet de retourner la définition de l'objet
     * @return La valeur de retour est un String qui permet de décrire l'objet
     */
    @Override
    public String toString(){
        return String.format("Nom du Dé : %s | Nombre de faces : %d", nom, nbFaces);
    }

    /**
     * Fonction equals()
     * @param De2 Représente un objet de type Object
     * @return La valeur de retour est un booléen qui signifie l'égalité ou non des valeurs
     */
    @Override
    public boolean equals(Object De2){
        boolean res = false;
        if(De2 instanceof De theDe){
            if(theDe.getNom().equals(nom) && nbFaces == theDe.getNbFaces()){
                res = true;
            }
        }
        return res;
    }

    /**
     * Accesseur de De
     * @param nom Représente le nom du Dé
     */
    public De(String nom){
        if(!nom.equals("")){
            this.nom = nom;
        }
        else{
            this.nom = "De" + nbDe;
        }
        nbDe++;
        setNbFaces(6);
    }

    /**
     * Accesseur
     * @return retourne le nombre de faces du dé
     */
    public int getNbFaces() {
        return nbFaces;
    }

    /**
     * Accesseur
     * @return retourne le nom du dé
     */
    public String getNom() {
        return nom;
    }

    /**
     * Accesseur permettant de set le nombre de faces du dé
     */
    public void setNbFaces(int nbFaces) {
        if(nbFaces >= LIMITE_INF && nbFaces <= LIMITE_SUP){
            this.nbFaces = nbFaces;
        }
        else{
            this.nbFaces = new Random().nextInt(LIMITE_INF, LIMITE_SUP +1);  // On assigne une valeur aléatoire
            System.err.println(nbFaces);
        }
    }


}

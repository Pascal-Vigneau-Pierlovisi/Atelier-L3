import java.util.GregorianCalendar;

public class Manager extends Employe {
    private Secretaire laSecretaire = null;  // Secrétaire du manager
    private final int anciennete;

    /**
     * Constructeur de la class Manager
     * @param leNom Le nom du Manager
     * @param lePrenom Le prénom du Manager
     * @param j Le jour de naissance
     * @param m Le mois de naissance
     * @param a L'année de naissance
     * @param numero Le numéro de rue
     * @param rue La rue
     * @param code_postal Le code postal
     * @param ville La ville
     * @param leSalaire Le salaire du Manager
     * @param jE Le jour d'embauche
     * @param mE Le mois d'embauche
     * @param aE L'année d'embauche
     */
    private Manager(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville,
                   double leSalaire, int jE, int mE, int aE){

        super(leNom, lePrenom, j, m, a, numero, rue, code_postal, ville, leSalaire, jE, mE, aE);
        anciennete = this.calculAnnuite();
        augmenterLeSalaire();
    }


    /**
     * Fonction createManager utilisée pour créer un Manager
     * @param leNom Le nom du manager
     * @param lePrenom Le prénom du manager
     * @param j Le jour de naissance
     * @param m Le mois de naissance
     * @param a L'année de naissance
     * @param numero Le numéro de rue
     * @param rue La rue
     * @param code_postal Le code postal
     * @param ville La ville
     * @param leSalaire Le salaire du manager
     * @param jE Le jour d'embauche
     * @param mE Le mois d'embauche
     * @param aE L'année d'embauche
     * @return La valeur de retour est soit un objet de type Manager, soit null
     */
    static Manager createManager(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville,
                                 double leSalaire, int jE, int mE, int aE){
        GregorianCalendar age = new GregorianCalendar(a, m, j);
        if(getAge(age) < 16 || getAge(age) > 65) return null;
        else{
            return new Manager(leNom, lePrenom, j, m, a, numero, rue, code_postal, ville, leSalaire, jE, mE, aE);
        }
    }

    /**
     * Fonction augmenterLeSalaire()
     */
    protected void augmenterLeSalaire(){
        if(anciennete != 0){
            for(int i = 0; i < anciennete; i++){
                this.augmenterLeSalaire(0.5);
            }
        }
    }

    /**
     * Fonction setSecretaire()
     * @param uneSecretaire Représente la secrétaire
     */
    protected void setSecretaire(Secretaire uneSecretaire){
        if(laSecretaire != uneSecretaire){
            if(uneSecretaire.setManager(this)){
                laSecretaire = uneSecretaire;
                System.out.println("Ajout de la secrétaire");
            }
        }
    }

    /**
     * Fonction deleteSecretaire()
     * @param uneSecretaire Représente un objet de la class Secretaire
     */
    protected void deleteSecretaire(Secretaire uneSecretaire){
        if(uneSecretaire.listeManager.contains(this)){
            laSecretaire = null;
            uneSecretaire.listeManager.remove(this);
        }
    }

    /**
     * Fonction afficheSecretaire
     * @return La valeur de retour est un message permettant d'identifier la secrétaire du manager
     */
    protected String afficheSecretaire(){
        String message = "La secrétaire n'est pas définie";
        if(laSecretaire != null){
            message = "La secrétaire de "+ getPrenom() +" est : " + laSecretaire.getPrenom() + " " + laSecretaire.getNom();
        }
        return message;
    }

    /**
     * Accesseur
     * @return La valeur de retour est la valeur d'ancienneté
     */
    public int getAnciennete() {
        return anciennete;
    }

    /**
     * Accesseur
     * @return La valeur de retour est la valeur de la variable laSecretaire
     */
    public Secretaire getLaSecretaire() {
        return laSecretaire;
    }

    /**
     * Accesseur
     * @param laSecretaire Représente un objet de class Secretaire
     */
    public void setLaSecretaire(Secretaire laSecretaire) {
        this.laSecretaire = laSecretaire;
    }
}

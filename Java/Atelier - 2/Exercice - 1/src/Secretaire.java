import java.util.ArrayList;
import java.util.GregorianCalendar;
import java.util.Objects;

public class Secretaire extends Employe{

    protected ArrayList<Manager> listeManager = new ArrayList<>();  // Liste des managers que gère la secrétaire

    /**
     * Constructeur de la class Secrétaire
     * @param leNom Le nom du Secrétaire
     * @param lePrenom Le prénom du Secrétaire
     * @param j Le jour de naissance
     * @param m Le mois de naissance
     * @param a L'année de naissance
     * @param numero Le numéro de rue
     * @param rue La rue
     * @param code_postal Le code postal
     * @param ville La ville
     * @param leSalaire Le salaire du Secrétaire
     * @param jE Le jour d'embauche
     * @param mE Le mois d'embauche
     * @param aE L'année d'embauche
     */
    private Secretaire(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville,
                    double leSalaire, int jE, int mE, int aE){

        super(leNom, lePrenom, j, m, a, numero, rue, code_postal, ville, leSalaire, jE, mE, aE);
    }

    /**
     * Fonction createSecrétaire utilisée pour créer un(e) Secrétaire
     * @param leNom Le nom du Secrétaire
     * @param lePrenom Le prénom du Secrétaire
     * @param j Le jour de naissance
     * @param m Le mois de naissance
     * @param a L'année de naissance
     * @param numero Le numéro de rue
     * @param rue La rue
     * @param code_postal Le code postal
     * @param ville La ville
     * @param leSalaire Le salaire du Secrétaire
     * @param jE Le jour d'embauche
     * @param mE Le mois d'embauche
     * @param aE L'année d'embauche
     * @return La valeur de retour est soit un objet de type Secretaire, soit null
     */
    static Secretaire createSecretaire(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville,
                                 double leSalaire, int jE, int mE, int aE){
        GregorianCalendar age = new GregorianCalendar(a, m, j);
        if(getAge(age) < 16 || getAge(age) > 65) return null;
        else{
            return new Secretaire(leNom, lePrenom, j, m, a, numero, rue, code_postal, ville, leSalaire, jE, mE, aE);
        }
    }

    /**
     * Fonction setManager()
     * @param leManager Représente le manager
     * @return La valeur de retour est un booléen indiquant si l'ajout s'est bien passé
     */
    protected boolean setManager(Manager leManager){
        boolean res = true;
        if(listeManager.contains(leManager) || listeManager.size() > 5){
            res = false;
        }
        else{
            listeManager.add(leManager);
            leManager.setLaSecretaire(this);
        }
        return res;
    }

    /**
     * Fonction afficheListManager()
     */
    protected void afficheListManager(){

        for(Manager manager:listeManager){
            System.out.println("Manager de " + getPrenom() + " : " + manager.getPrenom());
        }

    }

    /**
     * Fonction deleteManager()
     * @param leManager Représente un objet de la class Manager
     */
    protected void deleteManager(Manager leManager){
        if(listeManager.contains(leManager)){
            leManager.deleteSecretaire(this);
        }
    }

    /**
     * Fonction augmenterLeSalaire()
     */
    protected void augmenterLeSalaire(){
        if(listeManager.size() != 0){
            for(int i = 0; i < listeManager.size(); i++){
                this.augmenterLeSalaire(0.1);
            }
        }
    }

}

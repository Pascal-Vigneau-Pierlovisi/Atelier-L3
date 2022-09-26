import java.time.LocalDate;
import java.util.Calendar;
import java.util.GregorianCalendar;

public class Employe extends Personne{

    private double salaire;
    private final GregorianCalendar dateEmbauche;

    /**
     * Constructeur de la class Employe
     * @param leNom Le nom de l'employé
     * @param lePrenom Le prénom de l'employé
     * @param j Le jour de naissance
     * @param m Le mois de naissance
     * @param a L'année de naissance
     * @param numero Le numéro de rue
     * @param rue La rue
     * @param code_postal Le code postal
     * @param ville La ville
     * @param leSalaire Le salaire de l'employé
     * @param jE Le jour d'embauche
     * @param mE Le mois d'embauche
     * @param aE L'année d'embauche
     */
    protected Employe(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville,
                      double leSalaire, int jE, int mE, int aE){

        super(leNom, lePrenom, j, m, a, numero, rue, code_postal, ville);
        salaire = leSalaire;
        dateEmbauche = new GregorianCalendar(aE, mE, jE);
    }

    /**
     * Fonction createEmploye utilisée pour créer un employé
     * @param leNom Le nom de l'employé
     * @param lePrenom Le prénom de l'employé
     * @param j Le jour de naissance
     * @param m Le mois de naissance
     * @param a L'année de naissance
     * @param numero Le numéro de rue
     * @param rue La rue
     * @param code_postal Le code postal
     * @param ville La ville
     * @param leSalaire Le salaire de l'employé
     * @param jE Le jour d'embauche
     * @param mE Le mois d'embauche
     * @param aE L'année d'embauche
     * @return La valeur de retour est soit un objet de type Employe, soit null
     */
    static Employe createEmploye(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville,
                                 double leSalaire, int jE, int mE, int aE){
        GregorianCalendar age = new GregorianCalendar(a, m, j);
        if(getAge(age) < 16 || getAge(age) > 65){
            return null;
        }
        else{
            return new Employe(leNom, lePrenom, j, m, a, numero, rue, code_postal, ville, leSalaire, jE, mE, aE);
        }
    }

    /**
     * Accesseur
     * @return La valeur de retour est la valeur du salaire
     */
    public double getSalaire() {
        return salaire;
    }

    /**
     * Accesseur
     * @return La valeur de retour est la valeur du salaire
     */
    public GregorianCalendar getDateEmbauche() {
        return dateEmbauche;
    }

    /**
     * Accesseur
     * @return La valeur de retour est la valeur du salaire
     */
    public void setSalaire(double salaire) {
        this.salaire = salaire;
    }

    /**
     * Fonction calculAnnuite()
     * @return La valeur de retour est un entier représenant le nombre d'années d'ancienneté dans l'entreprise
     */
    protected int calculAnnuite(){
        int nb_anne = 0;

        Calendar maintenant = new GregorianCalendar();

        if(maintenant.get(Calendar.YEAR) >= dateEmbauche.get(Calendar.YEAR)){

            if(maintenant.get(Calendar.YEAR) == dateEmbauche.get(Calendar.YEAR) && maintenant.get(Calendar.MONTH) + 1 == dateEmbauche
                    .get(Calendar.MONTH)){
                nb_anne = 1;
            }
            else{


                int annee = maintenant.get(Calendar.YEAR) - dateEmbauche.get(Calendar.YEAR) ;
                int days = (maintenant.get(Calendar.DAY_OF_MONTH) + 1) - dateEmbauche.get(Calendar.DAY_OF_MONTH);

                if(annee == 0){
                    if(days > 0){
                        nb_anne = 1;
                    }
                }
                else if(annee >= 1){
                    if(days > 0){
                        nb_anne =  annee + 1;
                    }
                    else{
                        nb_anne = annee;
                    }
                }
            }
        }
        return nb_anne;
    }

    /**
     * Fonction augmenterSalaire()
     * @param pourcentage Représente le pourcentage qui va être augmenté sur le salaire
     */
    protected void augmenterLeSalaire(double pourcentage){
        if(pourcentage > 0){
            double augmentation = (salaire / 100) * pourcentage;
            salaire+=augmentation;
        }
    }













}

import java.util.*;

public class Personne{
    private static final Adresse ADRESSE_INCONNUE = null;
    private String nom;
    private String prenom;
    private final GregorianCalendar dateNaissance;
    private Adresse adresse=ADRESSE_INCONNUE;

	private static int nbPersonne = 0;
	
	/**
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le pr�nom de la personne
	 * @param laDate la date de naissance de la personne
	 * @param lAdresse l'adresse de la personne
	 */
	public Personne(String leNom,String lePrenom, GregorianCalendar laDate, Adresse lAdresse){
		nom = leNom.toUpperCase();
		prenom=lePrenom;
		dateNaissance=laDate;
		adresse=lAdresse;
	}
	
	/** 
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le pr�nom de la personne
	 * @param j le jour de naissance
	 * @param m le mois de naissance
	 * @param a l'ann�e de naissance
	 * @param numero le n� de la rue
	 * @param rue la rue
	 * @param code_postal le code postal de l'adresse
	 * @param ville la ville ou la personne habite
	 */
	public Personne(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville){
		this(leNom, lePrenom, new GregorianCalendar(a,m,j),new Adresse(numero,rue,code_postal,ville));
	}

	/**
	 * Accesseur
	 * @return retourne le nom
	 */
	public String getNom(){
		return nom;
	}

	/**
	 * Accesseur
	 * @return retourne le pr�nom
	 */
	public String getPrenom(){
		return prenom;
	}

	/**
	 * Accesseur
	 * @return retourne la date de naissance	 
	 */
	public GregorianCalendar getDateNaissance() {
		return dateNaissance;
	}

	/**
	 * Accesseur
	 * @return retourne l'adresse	 
	 */
	public Adresse getAdresse() {
		return adresse;
	}

	/**
	 * Accesseur
	 * @return retourne le nombre de personnes
	 */
	public static int getNbPersonne() {
		return nbPersonne;
	}

	/**
	 * Modificateur
	  retourne l'adresse
	 */
	public void setAdresse(Adresse a) {
		adresse=a;
	}

	/**
	 * Modificateur
	 modifie nbPersonne
	 */
	public static void setNbPersonne(int nbPersonne) {
		Personne.nbPersonne = nbPersonne;
	}

	/**
	 * Fonction PlusAgee()
	 * @param premierePersonne Représente la premiere personne
	 * @param deuxiemePersonne Représente la deuxième personne
	 * @return La valeur de retour est un booléen
	 */
	static boolean plusAgee(Personne premierePersonne ,Personne deuxiemePersonne){
		boolean result = false;
		if(premierePersonne.getDateNaissance().get(Calendar.YEAR ) == deuxiemePersonne.getDateNaissance().get(Calendar.YEAR )){
			if(premierePersonne.getDateNaissance().get(Calendar.MONTH) == deuxiemePersonne.getDateNaissance().get(Calendar.MONTH)){
				if(premierePersonne.getDateNaissance().get(Calendar.DAY_OF_MONTH) < deuxiemePersonne.getDateNaissance().get(Calendar.DAY_OF_MONTH)){
					result = true;
				}
			}
			else{
				if(premierePersonne.getDateNaissance().get(Calendar.MONTH) < deuxiemePersonne.getDateNaissance().get(Calendar.MONTH)){
					result = true;
				}
			}
		}
		else{
			if(premierePersonne.getDateNaissance().get(Calendar.YEAR) < deuxiemePersonne.getDateNaissance().get(Calendar.YEAR)){
				result = true;
			}
		}

		return result;
	}

	/**
	 * Fonction plusAgeeQue()
	 * @param deuxiemePersonne Représente la personne avec qui l'âge va être comparé
	 * @return La valeur de retour est un booléen
	 */
	public boolean plusAgeeQue(Personne deuxiemePersonne){
		boolean result = false;
		if(getDateNaissance().get(Calendar.YEAR ) == deuxiemePersonne.getDateNaissance().get(Calendar.YEAR )){
			if(getDateNaissance().get(Calendar.MONTH) == deuxiemePersonne.getDateNaissance().get(Calendar.MONTH)){
				if(getDateNaissance().get(Calendar.DAY_OF_MONTH) < deuxiemePersonne.getDateNaissance().get(Calendar.DAY_OF_MONTH)){
					result = true;
				}
			}
			else{
				if(getDateNaissance().get(Calendar.MONTH) < deuxiemePersonne.getDateNaissance().get(Calendar.MONTH)){
					result = true;
				}
			}
		}
		else{
			if(getDateNaissance().get(Calendar.YEAR) < deuxiemePersonne.getDateNaissance().get(Calendar.YEAR)){
				result = true;
			}
		}

		return result;
	}

	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	public String toString(){
		String result="\nNom : "+nom+"\n"
		+"Prénom : "+prenom+"\n"+
		"Né(e) le : "+dateNaissance.get(Calendar.DAY_OF_MONTH)+
		"-"+dateNaissance.get(Calendar.MONTH)+
		"-"+dateNaissance.get(Calendar.YEAR)+"\n"+
		"Adresse : "+
		adresse.toString();
		return result;
	}

	/* (non-Javadoc)
	 * @see java.lang.Object#equals()
	 */
	public boolean equals(Object unePersonne){
		boolean result = false;
		if(unePersonne instanceof Personne){
			if(((Personne) unePersonne).getDateNaissance().get(Calendar.YEAR) == getDateNaissance().get(Calendar.YEAR) &&
					((Personne) unePersonne).getDateNaissance().get(Calendar.MONTH) == getDateNaissance().get(Calendar.MONTH)
			&& ((Personne) unePersonne).getDateNaissance().get(Calendar.DAY_OF_MONTH) == getDateNaissance().get(Calendar.DAY_OF_MONTH) &&
					Objects.equals(((Personne) unePersonne).getNom(), nom) && Objects.equals(((Personne) unePersonne).getPrenom(), prenom)){
				result = true;

			}
		}
		return result;
	}

}

    
   
   
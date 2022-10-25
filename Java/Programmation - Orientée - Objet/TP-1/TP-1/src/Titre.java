import java.util.ArrayList;

public class Titre {
    private final int idTitre;  // Représente l'identifiant du titre
    private String nom;  // Représente le nom du titre
    private final int duree;  // Représente la durée du titre
    private final int tempo;  // Représente le tempo du titre
    private final String style;  // Représente le style
    private final boolean estReprise;  // Représente le fait qu'un titre soit oui ou non une reprise
    private boolean estPubliee;  // Représente le fait qu'un titre soit publié ou non
    private static int nbTitre = 0;  // Nombre de titres
    private ArrayList<Artiste> lstArtiste;

    /**
     * Constructeur()
     * @param nom Représente le nom du titre
     * @param duree Représente la durée du titre
     * @param tempo Représente le tempo du titre
     * @param style Représente le style du titre
     * @param estReprise Représente si le titre est une reprise ou non
     * @param estPubliee Représente le fait qu'un titre soit publié ou non
     */
    public Titre(String nom, int duree, int tempo, String style, boolean estReprise, boolean estPubliee){
        nbTitre++;  // On incrémente le nombre de titres
        this.idTitre = nbTitre;
        this.nom = nom;
        this.duree = duree;
        this.tempo = tempo;
        this.style = style;
        this.estReprise = estReprise;
        this.estPubliee = estPubliee;
        lstArtiste = new ArrayList<>();
    }

    /**
     * Accesseur
     * @return La valeur de retour est l'id du titre
     */
    public int getIdTitre() {
        return idTitre;
    }

    /**
     * Accesseur
     * @return La valeur de retour est le nom du titre
     */
    public String getNom() {
        return nom;
    }

    /**
     * Accesseur
     * @param nom Représente le nom du titre
     */
    public void setNom(String nom) {
        this.nom = nom;
    }

    /**
     * Accesseur
     * @return La valeur de retour est la durée d'un titre
     */
    public int getDuree() {
        return duree;
    }

    /**
     * Accesseur
     * @return La valeur de retour est le tempo du titre
     */
    public int getTempo() {
        return tempo;
    }

    /**
     * Accesseur
     * @return La valeur de retour est le tempo du titre
     */
    public String getStyle() {
        return style;
    }

    /**
     * Accesseur
     * @return La valeur de retour est un booléen qui signifie si le titre est une reprise
     */
    public boolean getEstReprise() {
        return estReprise;
    }

    /**
     * Accesseur
     * @return La valeur de retour est un booléen qui permet de savoir si la musique est publiée ou non
     */
    public boolean getEstPubliee() {
        return estPubliee;
    }

    /**
     * Accesseur
     * @param estPubliee Représente un booléen
     */
    public void setEstPubliee(boolean estPubliee) {
        this.estPubliee = estPubliee;
    }

    public ArrayList<Artiste> getLstArtiste() {
        return lstArtiste;
    }

    public void setLstArtiste(ArrayList<Artiste> lstArtiste) {
        this.lstArtiste = lstArtiste;
    }

    protected void addArtiste(Artiste artiste){
        if (!lstArtiste.contains(artiste)){
            lstArtiste.add(artiste);
        }
        if(!artiste.getLstTitre().contains(this)){
            artiste.addTitre(this);
        }
    }

}

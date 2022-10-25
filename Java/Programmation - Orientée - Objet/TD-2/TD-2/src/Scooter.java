public abstract class Scooter {

    private String modele;
    private String couleur;
    private int puissance;

    public Scooter(String modele, String couleur, int puissance){
        this.modele = modele;
        this.couleur = couleur;
        this.puissance = puissance;
    }

    public String getCouleur() {
        return couleur;
    }
    public int getPuissance() {
        return puissance;
    }
    public String getModele() {
        return modele;
    }

    public abstract void afficherCaracteristiques();

}

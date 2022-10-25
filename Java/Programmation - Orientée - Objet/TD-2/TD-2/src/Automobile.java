public abstract class Automobile {
    private String modele;
    private int puissance;
    private String couleur;
    private int espace;

    public Automobile(String modele, int puissance, String couleur, int espace){
        this.modele = modele;
        this.puissance = puissance;
        this.couleur = couleur;
        this.espace = espace;
    }

    public int getEspace() {
        return espace;
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

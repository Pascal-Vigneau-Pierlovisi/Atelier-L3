public class AutomobileEssence extends Automobile {

    private final int reservoir;

    public AutomobileEssence(String modele, int puissance, String couleur, int espace, int reservoir){
        super(modele, puissance, couleur, espace);
        this.reservoir = reservoir;
    }

    @Override
    public void afficherCaracteristiques()
        {
            System.out.println("Modèle : " + getModele() + " | Puissance : " + getPuissance() + " | Couleur : " + getCouleur() +
                    " | espace : " + getEspace() + "m3 | taille du réservoir : " + reservoir + " L");
        }

}


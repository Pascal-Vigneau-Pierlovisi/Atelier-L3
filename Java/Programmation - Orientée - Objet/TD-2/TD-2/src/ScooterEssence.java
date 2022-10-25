public class ScooterEssence extends Scooter {

    private final int reservoir;

    public ScooterEssence(String modele, String couleur, int puissance, int reservoir){
        super(modele, couleur, puissance);
        this.reservoir = reservoir;
    }

    @Override
    public void afficherCaracteristiques()
    {
        System.out.println("Modèle : " + getModele() + " | Puissance : " + getPuissance() + " | Couleur : " + getCouleur() +
                " | taille du réservoir : " + reservoir + " L");
    }


}

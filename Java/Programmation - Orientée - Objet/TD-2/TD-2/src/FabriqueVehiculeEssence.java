public class FabriqueVehiculeEssence implements FabriqueVehicule{

    private String modele;
    private int puissance;
    private String couleur;
    private int espace;
    private int reservoir;

    public FabriqueVehiculeEssence(String modele, int puissance, String couleur, int espace, int reservoir){
        this.modele = modele;
        this.puissance = puissance;
        this.couleur = couleur;
        this.espace = espace;
        this.reservoir = reservoir;
    }

    @Override
    public Automobile fabriquerAutomobile() {
        return new AutomobileEssence(modele, puissance, couleur, espace, reservoir);
    }

    @Override
    public Scooter fabriquerScooter() {
        return new ScooterEssence(modele, couleur, puissance, reservoir);
    }
}

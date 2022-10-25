public class FabriqueVehiculeElectricite implements FabriqueVehicule {

    private String modele;
    private int puissance;
    private String couleur;
    private int espace;
    private int temps_de_charge;

    public FabriqueVehiculeElectricite(String modele, int puissance, String couleur, int espace, int temps_de_charge){
        this.modele = modele;
        this.puissance = puissance;
        this.couleur = couleur;
        this.espace = espace;
        this.temps_de_charge = temps_de_charge;
    }
    @Override
    public Automobile fabriquerAutomobile() {
        return new AutomobileElectricite(modele, puissance, couleur, espace, temps_de_charge);
    }

    @Override
    public Scooter fabriquerScooter() {
        return new ScooterElectricite(modele, couleur, puissance, temps_de_charge);
    }
}

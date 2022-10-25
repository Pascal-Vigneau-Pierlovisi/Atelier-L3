public class ScooterElectricite extends Scooter{

    private final int temps_de_charge;

    public ScooterElectricite(String modele, String couleur, int puissance, int temps_de_charge){
        super(modele, couleur, puissance);
        this.temps_de_charge = temps_de_charge;
    }

    @Override
    public void afficherCaracteristiques()
    {
        System.out.println("Modèle : " + getModele() + " | Puissance : " + getPuissance() + " | Couleur : " + getCouleur() +
                " | temps de charge : " + temps_de_charge + " heure(s)");
    }

}

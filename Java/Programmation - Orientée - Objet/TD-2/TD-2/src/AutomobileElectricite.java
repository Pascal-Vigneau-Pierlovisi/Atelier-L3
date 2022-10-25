public class AutomobileElectricite extends Automobile {

    private final int temps_de_charge;

    public AutomobileElectricite(String modele, int puissance, String couleur, int espace, int temps_de_charge){
        super(modele, puissance, couleur, espace);
        this.temps_de_charge = temps_de_charge;
    }

    @Override
    public void afficherCaracteristiques() {
        {
            System.out.println("Modèle : " + getModele() + " | Puissance : " + getPuissance() + " | Couleur : " + getCouleur() +
                    " | espace : " + getEspace() + "m3 | temps de charge : " + temps_de_charge + " heure(s)");
        }

    }

}

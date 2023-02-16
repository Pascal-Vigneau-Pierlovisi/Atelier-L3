public class Humain extends Personnage{  // Class représentant un Humain qui est un Personnage
    private int nbDeplacements;  // Représente le nombre de déplacements fait par l'Humain
    private int niveau;  // Représente le niveau de l'Humain

    /**
     * Constructeur d'Humain
     * @param nom Représente le nom de l'humain
     * @param age Représente l'âge de l'humain
     */
    public Humain(String nom, int age){
        super(nom, age);  // On instancie un Humain qui aura les propriétés d'un personnage
        nbDeplacements = 1;  // On met le nombre de déplacements de l'humain sur 1
        niveau = 1;  // On met le niveau de l'humain à 1 quand on le crée
    }

    /**
     * Fonction deplacer()
     */
    @Override
    public void deplacer(int destination, int gain){
        super.deplacer(destination, gain);  // On fait appel à la méthode de Personnage
        nbDeplacements++;  // On incrémente le nombre de déplacements de l'humain
        if(nbDeplacements == 4){  // Si le nombre de déplacements de l'humain est >= 4 on le passe niveau 2
            niveau = 2;  // On met le niveau de l'humain sur 2
        }
        else if(nbDeplacements ==6){  // Si le nombre de déplacements de l'humain est >= 6 on le passe niveau 3
            niveau = 3;  // On met le niveau de l'humain sur 3
        }
    }

    /**
     * Fonction positionSouhaitee()
     * @return La valeur de retour est la position souhaitée par l'humain
     */
    public int positionSouhaitee(){return this.getPosition() + (niveau * nbDeplacements);}

    /**
     * Fonction toString()
     * @return La valeur de retour est le nom de l'humain
     */
    public String toString(){
        return ("Humain " + getNom());
    }
}

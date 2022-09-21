package Exercice1;

public class ManipRob {

    public static void main(String[] args) {

        Robot Toto = new Robot("Toto", 10, 20, 3);
        Robot Titi = new Robot("Titi");

        Toto.modifOrientation(2);
        Toto.modifPosition();

        Titi.modifPosition();

        //System.out.println(Toto.afficheToi());
        //System.out.println(Titi.afficheToi());
        System.out.println("Nom du robot : " + Toto.name + " | Référence : " + Toto.reference + " | " + "Position x, y :" +
                Toto.x + " " + Toto.y + " | Orientation : " + Toto.orientation);

        System.out.println("Nom du robot : " + Titi.name + " | Référence : " + Titi.reference + " | " + "Position x, y :" +
                Titi.x + " " + Titi.y + " | Orientation : " + Titi.orientation);

    }
}

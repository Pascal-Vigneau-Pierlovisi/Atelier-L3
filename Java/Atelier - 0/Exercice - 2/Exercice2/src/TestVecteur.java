public class TestVecteur {
    public static void main(String[] args) {

        Vecteur3D v1 = new Vecteur3D();
        Vecteur3D v2 = new Vecteur3D(3, 2, 5);

        System.out.println(v1.afficheVecteur());
        System.out.println(v1.norme());


        System.out.println(v2.afficheVecteur());
        System.out.println(v2.norme());

        System.out.println(v1.produitScalaire(v1, v2));
        System.out.println(v1.somme(v1, v2));

    }
}

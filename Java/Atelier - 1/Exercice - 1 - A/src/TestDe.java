public class TestDe {
    public static void main(String[] args) {
        De de1 = new De();  // Dé 0 par défaut sans aucuns paramètres
        De de2 = new De("Pascalito");  // Dé ayant pour nom Pascalito et pour nombre de faces 6
        De de3 = new De(120);  // Dé ayant uniquement le nombre de faces réglé sur 9
        De de4 = new De("Magic", 3);  // Dé ayant un nom et un nombre de faces
        De de5 = new De("Pascalito");

        System.out.println("-------------------");
        System.out.println(de1.getNom());  // Affichage des noms des différents Dé
        System.out.println(de2.getNom());
        System.out.println(de3.getNom());
        System.out.println(de4.getNom());

        System.out.println("-------------------");
        System.out.println(de1.getNbFaces());  // Affichage du nombre de faces des différents Dé
        System.out.println(de2.getNbFaces());
        System.out.println(de3.getNbFaces());
        System.out.println(de4.getNbFaces());

        System.out.println("-------------------");
        System.out.println(de1.lancer());  // Affichage des lancés pour les Dés
        System.out.println(de3.lancer(10));

        System.out.println("-------------------");
        System.out.println(de1.toString());  // Affichage avec la méthode toString()
        System.out.println(de3.toString());
        System.out.println(de2.toString());

        System.out.println("-------------------");
        System.out.println(de1.equals(de2));  // Test de l'égalité entre d1 et d2
        System.out.println(de2.equals(de5));

        System.out.println("-------------------");
        DePipes deP1 = new DePipes(10, 8);  // Instanciation d'un DéPipes
        System.out.println(deP1.lancer());  // Tirage d'un DéPipes



    }
}

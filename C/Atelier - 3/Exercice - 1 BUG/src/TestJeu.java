public class TestJeu {
    public static void main(String[] args) {
        Jeu jeu1 = new Jeu("AtelierPOO", 4, 10);
        Joueur J1 = new Joueur("Paul");
        Tauren taur1 = Tauren.createTauren("Hector", 15, 10);
        Humain hum1 = new Humain("Jean", 10);
        J1.ajouterPersonnage(taur1);
        J1.ajouterPersonnage(hum1);
        Joueur J2 = new Joueur("Lucien");
        Tauren taur2 = Tauren.createTauren("Hercule", 20, 5);
        Humain hum2 = new Humain("Marie", 10);
        J2.ajouterPersonnage(taur2);
        J2.ajouterPersonnage(hum2);
        jeu1.ajouterJoueur(J1);
        jeu1.ajouterJoueur(J2);
        jeu1.lancerJeu();

        Jeu jeu2 = new Jeu("AtelierPOO", 20, 10);
        jeu2.ajouterJoueur(J1);
        jeu2.ajouterJoueur(J2);
        jeu2.lancerJeu();



    }
}

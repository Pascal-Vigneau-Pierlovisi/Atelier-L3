import java.util.Calendar;

public class TestQ2 {
    public static void main(String[] args) {

        // --------- TEST EMPLOYE -------------------------
        Employe e1  = Employe.createEmploye("Vigneau", "Pascal", 29, 4, 2002, 1,
                "rue des potiers", "20250", "Corte", 2400, 26, 9, 2022);
        System.out.println(e1.toString());
        e1.augmenterLeSalaire(20);
        System.out.println(e1.getSalaire());
        System.out.println(e1.calculAnnuite() + " année(s) d'ancienneté");
        // ------------------------------------------------

        // --------- TEST MANAGER -------------------------
        Manager m1 = Manager.createManager("Pierlovisi", "Pascal", 29, 4, 2002, 1,
                "rue des potiers", "20250", "Corte", 1200, 22, 9, 2001);
        Manager m2 = Manager.createManager("Alpha", "Pascal", 29, 4, 2002, 1,
                "rue des potiers", "20250", "Corte", 1200, 22, 9, 2002);
        Manager m3 = Manager.createManager("Bravo", "Pascal", 29, 4, 2002, 1,
                "rue des potiers", "20250", "Corte", 1200, 22, 9, 2011);
        Manager m4 = Manager.createManager("Charli", "Pascal", 29, 4, 2002, 1,
                "rue des potiers", "20250", "Corte", 1200, 22, 9, 2020);
        Manager m5 = Manager.createManager("Delta", "Pascal", 29, 4, 2002, 1,
                "rue des potiers", "20250", "Corte", 1200, 22, 9, 2001);

        System.out.println(m1.toString());
        System.out.println(m1.getAnciennete() + " année(s) d'ancienneté");
        System.out.println("Salaire du manager : "+ m1.getSalaire());
        // ------------------------------------------------

        // --------- TEST SECRETAIRE -------------------------
        Secretaire s1 = Secretaire.createSecretaire("Karamani", "Laetitia", 17, 3, 1983, 1,
                "Résidence Élisa lieu dit U lagu", "20290", "Lucciana", 1200, 22, 9, 2020);
        System.out.println(s1.toString());
        m1.setSecretaire(s1);
        m2.setSecretaire(s1);
        m3.setSecretaire(s1);
        m4.setSecretaire(s1);
        m5.setSecretaire(s1);

        s1.afficheListManager();
        System.out.println(m1.afficheSecretaire());
        s1.augmenterLeSalaire();
        System.out.println("Salaire de " + s1.getNom() + " " + s1.getSalaire());
        s1.deleteManager(m1);
        // ------------------------------------------------

    }
}

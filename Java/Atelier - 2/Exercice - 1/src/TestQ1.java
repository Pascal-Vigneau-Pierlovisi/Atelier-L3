public class TestQ1 {

    public static void main(String[] args) {
        Personne p1 = new Personne("Vigneau", "Pascal", 29, 4, 2002, 1, "Rue des padawoines", "20290", "Ajaccio" );
        Personne p2 = new Personne("Vigneau", "Antoine", 29, 4, 2002, 1, "Rue des padawoines", "20290", "Ajaccio" );

        System.out.println(p1.toString());
        System.out.println(p1.plusAgeeQue(p2));
        System.out.println(Personne.plusAgee(p1, p2));
        System.out.println(p1.equals(p2));
    }
}

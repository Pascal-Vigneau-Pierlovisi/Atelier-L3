public class TestDe {

    /**
     * La fonction main() désigne le lieu d'execution du script Java
     */
    public static void main(String[] args) {

        De De1 = new De(6);

        De De2 = new De();

        De De3 = new De("Pascal");

        De De4 = new De("Pascal");

        DePipes DePipes1 = new DePipes();

        DeMemoire DeMemoire1 = new DeMemoire();

        //System.out.println(De1.lancer());
        //System.out.println(De1.lancer(8));
        //System.out.println(De1.toString());
        //System.out.println(De3.equals(De4));

        System.out.println(DePipes1.toString());

        System.out.println(DePipes1.lancer(3));

        System.out.println(DeMemoire1.lancer() + " Premier Tirage");
        System.out.println(DeMemoire1.lancer() + " deuxième Tirage");
        System.out.println(DeMemoire1.lancer() + " Troisième Tirage");

    }
}

public class TestNumber {

    public static void main(String[] args) {
        Entier entier1 = new Entier(1, 10);
        Entier entier2 = new Entier(1, 10);

        EntierFou entierFou1 = new EntierFou(1, 10, 2, 8);

        System.out.println(entier1.equals(entier2));

        System.out.println(entier1.toString());

        entier1.incremente(6);

        System.out.println(entier1.equals(entier2));


        System.out.println(entierFou1.incremente());

        System.out.println(entierFou1.toString());

    }
}

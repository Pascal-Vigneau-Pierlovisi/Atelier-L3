public class TestNumber {

    public static void main(String[] args) {
        ManipEntiers entier1 = new ManipEntiers(1, 10);
        ManipEntiers entier2 = new ManipEntiers(1, 10);

        EntierFou entierFou1 = new EntierFou(1, 10, 2, 8);

        System.out.println(entier1.equals(entier2));

        entier1.incremente(6);

        System.out.println(entier1.equals(entier2));

        System.out.println(entier1.toString());

        System.out.println(entierFou1.incremente());

        System.out.println(entierFou1.toString());

    }
}

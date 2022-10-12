public class Main {
    public static void main(String[] args) {

        System.out.println(Addition.addition(10, 12));  // Test de la fonction addition()
        System.out.println("--------------------------");
        int[] lst = {10, 20, 30};  // Déclaration d'une liste d'entiers
        System.out.println(Addition.additionBis(lst));  // Test de la fonction additionBis()
        System.out.println("--------------------------");
        Multiplication.afficherTable(5);  // Test de la fonction afficherTable()
        System.out.println("--------------------------");
        System.out.println(Geometrie.calculPerimetre(12));  // Test de la fonction calculPerimetre()
        System.out.println("--------------------------");
        System.out.println(Geometrie.calculAir(12));  // Test de la fonction calculAir()
        System.out.println("--------------------------");
        double[] lstDouble = {10, 20, 30};  // Déclaration d'une liste de double
        System.out.println(Moyenne.moyenne(lstDouble));  // Test de la fonction moyenne()
        System.out.println("--------------------------");
        System.out.println(Inverser.inverser("Hello"));  // Test de la fonction inverser()
        System.out.println("--------------------------");
        System.out.println(Ascii.valeurAscii('e'));  // Test de la fonction valeurAscii()
        System.out.println("--------------------------");
        System.out.println(Temperature.convertF(30));  // Test de la fonction convertF()
        System.out.println("--------------------------");
        System.out.println(Temperature.convertC(86));  // Test de la fonction convertC()
        System.out.println("--------------------------");
        for(int i = 1; i <= 100; i++){
            if(Premier.estPremier(i)){
                System.out.println(i + " est premier");
            }
            else{
                System.out.println(i + " n'est pas premier");
            }
        }  // Test pour avoir les nombres premiers de 1 à 100
        System.out.println("--------------------------");
        System.out.println(Palindrome.estPalindrome("Kayak"));  // Test de la fonction estPalindrome()
        System.out.println(Palindrome.estPalindrome("Arnaud"));  // Test de la fonction estPalindrome()

    }
}

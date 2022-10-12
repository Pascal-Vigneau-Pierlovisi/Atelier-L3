public class Palindrome {

    /**
     * Fonction estPalindrome()
     * @param word Représente le mot à tester
     * @return La valeur de retour est un booléen signifiant si un mot est palindrome
     */
    public static boolean estPalindrome(String word){
        return Inverser.inverser(word.toLowerCase()).equals(word.toLowerCase());
    }
}

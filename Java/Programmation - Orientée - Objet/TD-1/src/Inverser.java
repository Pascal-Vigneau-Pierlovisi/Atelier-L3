public class Inverser {
    /**
     * Fonction inverser()
     * @param chaine Représente une chaine de caractère
     * @return La valeur de retour est la chaine inversée
     */
    public static String inverser(String chaine){
        StringBuilder res = new StringBuilder();
        if(chaine.length() == 0){
            System.err.println("La chaine de caractère est vide");
        }
        else{
            for(int i = chaine.length() -1; i >= 0; i--){
                res.append(chaine.charAt(i));
            }
        }
        return res.toString();
    }
}

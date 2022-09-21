public class Entier {

    public Integer getNumber() {
        return number;
    }
    private Integer number;

    protected Integer min;

    protected Integer max;

    /**
     * La fonction ManipEntiers() est le constructeur par défault
     * @param min Représente la valeur minimum qui va être utilisée pour générer le nombre
     * @param max Représente la valeur maximale qui va être utilisée pour générer le nombre
     * @param number Représente la valeur que l'on souhaite affecter à number
     */
    public Entier(Integer min, Integer max, Integer number){
        if(min<number && number>max){
            this.number = min;
        }
        else{
            this.number = number;
        }

        this.min = min;
        this.max = max;

    }

    /**
     * La fonction ManipEntiers() est le constructeur
     * @param min Représente la valeur minimum qui va être utilisée pour générer le nombre
     * @param max Représente la valeur maximale qui va être utilisée pour générer le nombre
     */
    public Entier(Integer min, Integer max){
        this(min, max, min);
    }

    /**
     * La fonction setNumber() permet de régler la valeur de number
     * @param number Représente la valeur de number souhaitée
     */
    protected void setNumber(Integer number){
        if(number > min && number < max){
            this.number = number;
        }
    }

    /**
     * La fonction incremente() permet d'incrémenter number
     * @return La valeur de retour est la valeur de number
     */
    protected int incremente(){
        if(number +1 < max){
            number+=1;
        }
        return number;
    }

    /**
     * La fonction incremente() est une surcharge de la méthode déjà existante incremente
     * @param n Représente le pas qui va être utilisé pour l'incrementation de number
     * @return La valeur de retour est la valeur de number
     */
    protected int incremente(int n){
        if((this.number+n)<=max){
            number+=n;
        }
        return number;
    }

    /**
     * La fonction toString() est une redéfinition de la méthode toString() permettant de renvoyer
     * les informations d'un entier
     * @return La valeur de retour est un message contenant les informations liées à un objet ManipEntiers
     */
    public String toString(){
        return String.format("L'entier : %d | valeur min : %d | valeur max : %d", number, min, max);
    }

    /**
     * La fonction equals() est une redéfinition de la méthode déjà existante equals et permettant
     * la comparaison des attributs de 2 objets de class ManipEntiers
     * @param entierToCompare Objet qui va être comparé avec celui qui est utilisé dans l'appel de la méthode
     * @return La valeur de retour est un Booléen qui représente le fait de l'égalité des attributs des 2 objets
     */
    public boolean equals(Object entierToCompare){
        if(entierToCompare instanceof Entier){
            Entier autre = (Entier)entierToCompare;
            return(number == autre.number && min == autre.min && max == autre.max);
        }
        return false;

    }

}

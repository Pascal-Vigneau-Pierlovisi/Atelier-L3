import java.util.Random;

public class EntierFou extends ManipEntiers{

    private Random r = new Random();
    protected Integer niveauFolie;

    /**
     * La fonction EntierFou() est le constructeur de la class EntierFou
     * @param min Représente la valeur minimum qui va être utilisée pour générer le nombre
     * @param max Représente la valeur maximale qui va être utilisée pour générer le nombre
     * @param number Représente la valeur que l'on souhaite affecter à number
     * @param niveauFolie Représente le niveau de folie
     */
    public EntierFou(Integer min, Integer max, Integer number, Integer niveauFolie) {
        super(min, max, number);
        this.niveauFolie = niveauFolie;

    }

    /**
     * La fonction EntierFou() est le constructeur de la class EntierFou
     * @param min Représente la valeur minimum qui va être utilisée pour générer le nombre
     * @param max Représente la valeur maximale qui va être utilisée pour générer le nombre
     * @param niveauFolie Représente le niveau de folie
     */
    public EntierFou(Integer min, Integer max, Integer niveauFolie) {
        super(min, max);
        this.niveauFolie = niveauFolie;
    }

    /**
     * La fonction incremente() permet de générer un nombre aléatoirement entre 0 et niveauFolie
     * @return La valeur de retour est l'entier qui a été tiré.
     */
    protected int incremente(){

        int tirage = r.nextInt(0, niveauFolie);
        super.incremente(tirage);
        return tirage;
    }
}

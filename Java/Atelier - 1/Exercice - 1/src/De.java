import org.jetbrains.annotations.NotNull;

import java.util.*;
public class De {

    protected static Random r = new Random();  // Création d'un objet du type Random
    static Integer nbDe = 0;  // Nombre de Dé crées qui va s'incrémenté par la suite
    public String getName() {
        return name;
    }  // Access au nom du dé

    public void setName(String name) {
        this.name = name;
    }  // Permet de modifier le nom du Dé

    private String name;  // Nom du dé
    protected Integer nbFaces;  // Nombre de faces du dé entre 3 et 120

    /**
     * Constructeur de la class De qui ne prend aucun paramètre
     */
    public De(){
        this(6);
        this.name = "Dé" + nbDe;
    }

    /**
     * La fonction De() représente le constructeur par défaut de la classe De
     * @param nbFaces Représente le nombre de face du dé
     */
    public De(Integer nbFaces){

        this.name = "Dé" + nbDe;

        nbDe+=1;

        if(nbFaces > 120){
            System.err.println(nbFaces);
        }
        if(nbFaces < 3){
            System.err.println(nbFaces);
        }
        else{
            this.nbFaces = nbFaces;
        }

    }

    /**
     * Constructeur de la class De qui prend qu'un seul paramètre
     * @param name Représente le nom du Dé
     */
    public De(String name){
        this(6);
        this.name = name;
    }

    /**
     * La fonction getNbfaces() permet d'afficher le nombre de faces du dé
     * @return La valeur de retour est le nombre de faces du dé
     */
    protected Integer getNbFaces(){
        return this.nbFaces;
    }

    /**
     * La fonction setNbFaces() permet de régler le nombre de faces du dé
     * @param nbFaces Représente le nombre de face que veut l'utilisateur
     */
    protected void setNbFaces(Integer nbFaces){
        if(nbFaces > 120){
            System.err.println(nbFaces);
        }
        if(nbFaces < 3){
            System.err.println(nbFaces);
        }
        else{
            this.nbFaces = nbFaces;
        }
    }

    /**
     * La fonction lancer() permet de tirer un nombre au hasard entre 0 et 6
     * @return La valeur de retour est un entier entre 0 et 6
     */
    protected Integer lancer(){
        return r.nextInt(7);
    }

    /**
     * La fonction lancer() est une surcharge de lancer() et permet de rentrer un nombre de lancés
     * @param nbFois Représente le nombre de lancés qui vont être fait
     * @return La valeur de retour est un entier qui représente le nombre le plus grand tiré
     */
    protected Integer lancer(Integer nbFois){

        List<Integer> tableau = new ArrayList<Integer>();

        for(int i = 0; i<nbFois; i++){

            tableau.add(r.nextInt(7));

        }

        return Collections.max(tableau);



    }

    /**
     * La fonction toString() permet de retourner la définition de l'objet
     * @return La valeur de retour est un String qui permet de décrire l'objet
     */
    public String toString(){
        return String.format("Nom du Dé : %s | Nombre de faces : %d", this.name, this.nbFaces);
    }

    public boolean equals(Object De2){
        boolean res = false;
        if(De2 instanceof De){
            De theDe = (De)De2;
            if(theDe.getName().equals(name) && nbFaces == theDe.getNbFaces()){
                res = true;
            }
        }
        return res;
    }







}

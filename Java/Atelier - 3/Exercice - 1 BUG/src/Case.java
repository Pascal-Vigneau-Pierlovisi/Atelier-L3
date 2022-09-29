public class Case {
    protected int gain;  // Nombre de points à ajouter au joueur
    protected Personnage perso = null;  // Représente un Personnage qui est sur la case null si aucun Personnage
    protected Obstacle obs = null;  // Représente un Obstacle qui est sur la case null si aucun Obstacle

    /**
     * Constructeur de Case
     * @param obs Représente un obstacle
     * @param gain Représente le gain du joueur qui peut être positif ou négatif
     */
    public Case(Obstacle obs, int gain){
        this.obs = obs;  // On affecte un obstacle
        this.gain = gain;  // On affecte la valeur du gain
    }

    /**
     * Constructeur de Case
     * @param gain Représente le gain du joueur qui peut être positif ou négatif
     */
    public Case(int gain){
        this.gain = gain;  // On affecte la valeur du gain
    }

    /**
     * Fonction getPenalite()
     * @return La valeur de retour est la valeur de la pénalité
     */
    public int getPenalite(){
        int res = 0;  // On initialise la valeur de retour sur 0
        if(!sansObstacle()){  // Si un obstacle est présent dans la case
            res = obs.getObstacle();  // Le résultat prend la valeur de l'obstacle qui représente sa pénalité
        }
        if(!sansPerso()){  // Si un personnage est présent sur la case
            res = gain - (2*gain);  // La pénalité prend l'opposé de la valeur du gain
        }

        return res;  // On renvoie la valeur de la pénalité
    }

    /**
     * Fonction placerObstacle()
     * @param obstacle Représente l'obstacle à mettre sur la case
     */
    public void placerObstacle(Obstacle obstacle){
        if(obstacle != null){  // On vérifie que l'obstacle ne soit pas null
            obs = obstacle;  // On met l'obstacle sur la case
        }
        else{  // Si l'obstacle est null
            System.err.println("Impossible de mettre un obstacle null");  // On envoie un message d'erreur
        }
    }

    /**
     * Fonction placerPersonnage()
     * @param personnage Représente le personnage à mettre sur la case
     */
    public void placerPersonnage(Personnage personnage){
        if(personnage != null){  // On vérifie que le personnage ne soit pas null
            if(estLibre()){  // On vérifie si la case est libre
                perso = personnage;  // S'il n'est pas null on met le personnage sur la case
            }
            else{
                System.err.println("La case est déjà occupée");
            }

        }
        else{  // Si le personnage est null
            System.err.println("Le personnage est null cela n'est pas possible");  // On renvoie un message d'erreur
        }
    }

    /**
     * Fonction enleverPersonnage()
     */
    public void enleverPersonnage(){
        if(perso != null){  // On vérifie que le perso ne soit pas déjà null
            perso = null;  // Si le perso n'est pas null on le met sur null
        }
        else{  // Si le perso est null
            System.err.println("Aucun personnage n'est déjà présente sur la Case");  // On renvoie un message d'erreur
        }
    }

    /**
     * Fonction estLibre()
     * @return La valeur de retour est un booléen indiquant si la case est libre
     */
    public boolean estLibre(){
        return sansObstacle() && sansPerso();  // On retourne si la case est libre ou non
    }

    /**
     * Fonction sansObstacle()
     * @return La valeur de retour signifie la présence ou non d'un obstacle sur la case
     */
    public boolean sansObstacle(){
        boolean res = false;  // On initialise la valeur de retour sur faux
        if(obs == null){  // Si la case ne contient aucun obstacle
            res = true;  // On met la valeur de retour sur vraie
        }
        return res;  // On retourne la valeur de res qui signifie la présence ou non d'un obstacle
    }

    /**
     * Fonction sansPerso()
     * @return La valeur de retour représente la presence ou non d'un personnage sur la case
     */
    public boolean sansPerso(){
        boolean res = false;  // On initialise la valeur de retour sur faux
        if(perso == null){  // Si aucun personnage n'est présent sur la case
            res = true;  // La valeur de retour prend vraie
        }
        return res;  // On renvoie la valeur qui représente la présence ou non d'un personnage sur la case
    }

    /**
     * Fonction toString()
     * @return La valeur de retour est un message qui varie en fonction de plusieurs critères
     */
    public String toString(){
        String message = "";  // On initialise la valeur de retour sur une chaine de caractère
        if(estLibre()){  // Si la case est libre
            message = "Libre (gain = " + gain + ")";  // On met un message qui va être différent
        }
        if(!sansObstacle()){  // Si la case a un obstacle
            message = "Obstacle (pénalité = "+ getPenalite() + ")";  // On met un message qui va être différent
        }
        if(!sansPerso()){  // On vérifie si un personnage n'est pas déjà présent sur la case
            message = perso.toString() + "(pénalité = " + getPenalite() + ")";  // On met un message qui va être différent
        }
        else{  // Dans le cas où on rentre dans aucune des conditions une erreur est donc présente
            System.err.println("Une erreur est survenue");  // On affiche un message d'erreur
        }
        return message;  // On renvoie le message
    }


}

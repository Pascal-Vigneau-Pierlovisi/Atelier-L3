import java.util.ArrayList;
import java.util.Random;

public class Jeu {

    private String titre;  // Représente le titre du jeu
    private final int NB_JOUEUR_MAX = 6;  // Représente le nombre max de joueurs
    private final int NB_CASES = 50;  // Représente le nombre de cases
    private ArrayList<Joueur> listeJoueurs;  // Représente la liste des joueurs qui jouent au jeu
    private ArrayList<Case> cases;  // Représente les cases du jeu
    private final int nbEtapes;  // Représente le nombre de déplacements par Personnage
    private final int nbObstacles;  // Représente le nombre max d'obstacles dans le jeu

    private static int scoreMax = 0;  // Représente le score max atteint dans toutes les parties lancées

    /**
     * Constructeur de Jeu
     * @param titre Représente le titre du jeu
     * @param nbEtapes Représente le nombre d'étapes du jeu
     * @param nbObstacles Représente le nombre d'obstacles dans le jeu
     */
    public Jeu(String titre, int nbEtapes, int nbObstacles){
        this.titre = titre;  // On définit le titre de la partie
        this.nbEtapes = nbEtapes;  // On définit le nombre d'étapes du jeu
        this.nbObstacles = nbObstacles;  // On définit le nombre d'obstacles dans le jeu
        listeJoueurs = new ArrayList<>();  // On instancie la liste des joueurs de la partie
        cases = new ArrayList<>() ; // On instancie les cases du jeu
    }

    /**
     * Fonction ajouterJoueur()
     * @param j Représente un joueur à ajouter à la partie
     */
    public void ajouterJoueur(Joueur j){
        if(listeJoueurs.size() <= NB_JOUEUR_MAX){  // On vérifie que le nombre de joueurs max n'est pas atteint
            if(listeJoueurs.contains(j)){  // On vérifie que le joueur ne fait pas déjà partie du jeu
                System.err.println(j.getNom() + " est déjà dans la partie");  // On affiche un message d'erreur
            }
            else{  // Si le joueur n'est pas présent et que le nombre de joueurs max n'est pas atteint
                listeJoueurs.add(j);  // On ajoute le joueur dans la partie
            }
        }
        else{  // Si le nombre de joueurs max est déjà atteint
            System.err.println("La partie est déjà complète");  // On affiche un message d'erreur
        }
    }

    /**
     * Fonction tousLesPersos()
     * @return La valeur de retour est une liste contenant tous les personnages du jeu
     */
    public ArrayList<Personnage> tousLesPersos(){
        ArrayList<Personnage> listePersos = new ArrayList<>();  // On crée une variable de retour
        if(listeJoueurs.size() != 0){  // On vérifie que des joueurs soient bien présents dans la partie
            for(Joueur j : listeJoueurs){  // On parcourt la liste des joueurs de la partie
                listePersos.addAll(j.getListePersos());  // On ajoute tous les personnages
            }
        }
        else{  // Si aucuns joueurs dans la partie
            System.err.println("Aucun joueur dans la partie");  // On met un message d'erreur
        }
        return listePersos;  // On retourne la liste des personnages de la partie
    }

    /**
     * Fonction initialiserCases()
     */
    public void initialiserCases(){
        int limiteObs = 0;  // Compteur pour les obstacles
        for(int i = 0; i < NB_CASES + 1; i++){  // On va créer les cases du jeu
            int r = new Random().nextInt(0, 50);  // On prend un nombre aléatoire qui va nous servir
            Case newCase = new Case(r);  // On instancie une nouvelle case
            if(r % 5 == 0 && limiteObs < nbObstacles){  // Si les conditions sont respectées
                newCase.placerObstacle(new Obstacle(r*2));  // On ajoute un obstacle sur la case
                limiteObs ++;  // On incrémente le nombre d'obstacles du jeu
            }
            cases.add(newCase);  // On ajoute la case au dans le jeu
        }
    }

    /**
     * Fonction lancerJeu()
     */
    public void lancerJeu(){
        initialiserCases();
        for(Personnage p : tousLesPersos()){  // On parcourt les personnages qui sont dans le jeu
            boolean check = false;  // On fait une vérification si le personnage a été assigné à une case
            int nbCases = 0;  // On met en place un compteur
            while(!check && nbCases < cases.size() - 1){  // Tant que le personnage n'est pas assigné
                if(cases.get(nbCases).estLibre()){  // Si la case est libre
                    cases.get(nbCases).placerPersonnage(p);  // On ajoute le personnage à la case
                    p.setPosition(nbCases);  // On met la position du personnage sur l'index de la case
                    check = true;  // La vérification est donc vraie
                }
                else if(nbCases == cases.size() - 1){  // Si on atteint le nombre de cases max
                    System.err.println("Le personnage n'a pas pu être placé");  // On renvoie un message d'erreur
                }
                nbCases++;  // On incrémente le nombre de cases parcourut
            }
        }
        for(int i = 0; i < nbEtapes; i++){  // Lancement du jeu
            for(Personnage perso : tousLesPersos()){  // On parcourt pour tous les joueurs
                Case caseSouhaitee = cases.get(perso.positionSouhaitee() % NB_CASES - 1);  // On met la case désignée
                if(caseSouhaitee.estLibre()){  // Si la case est libre
                    caseSouhaitee.placerPersonnage(perso);  // On déplace le personnage sur cette case
                    perso.getJ().modifierPoints(caseSouhaitee.gain);  // Le joueur associé au personnage prend le gain
                }
                if(!caseSouhaitee.sansPerso()){  // Si un personnage est déjà présent sur la case
                    perso.getJ().modifierPoints(caseSouhaitee.getPenalite());  // Le joueur associé prend une pénalité
                } else if (!caseSouhaitee.sansObstacle()) {  // Si un obstacle est présent
                    perso.getJ().modifierPoints(caseSouhaitee.getPenalite());  // Le joueur associé prend une pénalité
                }
            }
            for(int a = 0; a < listeJoueurs.size() - 1; a++){  // On va régler le score max du jeu
                if(listeJoueurs.get(a).nbPoints > scoreMax){  // Si le score du joueur > scoreMax
                    scoreMax = listeJoueurs.get(a).nbPoints;  // le score max prend le score du joueur
                }
            }
            afficherCases();
        }
        afficherResultats();
    }

    /**
     * Fonction afficherCases()
     */
    public void afficherCases(){
        for(int i = 0; i < cases.size() -1; i++){
            System.out.println("-----------------------------\nCase " + i + " " + cases.get(i).toString());
        }
    }

    /**
     * Fonction afficherParticipants()
     */
    public void afficherParticipants(){
        System.out.println("LISTE DES JOUEURS");
        for(Joueur joueur : listeJoueurs){
            System.out.println("-------------------------\n" + joueur.getCode()+ " " + joueur.getNom() + "(" + joueur.nbPoints
            + " points) avec " + joueur.getListePersos().size() + " Personnage(s)");
        }
    }

    /**
     * Fonction afficherResultats()
     */
    public void afficherResultats(){
        afficherParticipants();
        System.out.println("***********************************************\n" + titre);
        Joueur gagnant = null;
        int score = 0;
        for(Joueur j : listeJoueurs){
            if(j.nbPoints > score){
                gagnant = j;
                score = j.nbPoints;
            }
        }
        System.out.println("RESULTATS");
        System.out.println("Le gagnant est " + gagnant.getNom()+ " avec " + gagnant.nbPoints+" points");
        System.out.println("Le record est de " + scoreMax);
    }
}

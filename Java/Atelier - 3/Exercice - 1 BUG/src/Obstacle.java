public class Obstacle {
    private final int obstacle;  // Représente un entier qui signifie le nombre de points de l'obstacle

    /**
     * Constructeur de Obstacle()
     * @param obstacle Représente la valeur que l'on souhaite attribuer à l'obstacle
     */
    public Obstacle(int obstacle){
        this.obstacle = obstacle;
    }

    /**
     * Accesseur
     * @return La valeur de retour est la valeur de l'obstacle
     */
    public int getObstacle() {
        return obstacle;
    }

}

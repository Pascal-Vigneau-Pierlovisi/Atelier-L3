import org.jetbrains.annotations.NotNull;

import java.lang.Math;

public class Vecteur3D {

    protected int x;
    protected int y;
    protected int z;

    public Vecteur3D(int x, int y, int z){

        this.x = x;
        this.y = y;
        this.z = z;
    }

    public Vecteur3D(){

        this.x = 0;
        this.y = 0;
        this.z = 0;

    }

    protected String afficheVecteur(){
        return String.format("x : %d | y : %d | z : %d", this.x, this.y, this.z);
    }

    protected double norme(){
        return Math.sqrt((x * x) +(y * y) +(z * z));
    }

    protected double produitScalaire(@NotNull Vecteur3D vecteur1, @NotNull Vecteur3D vecteur2){
        return ((vecteur1.x * vecteur2.x) + (vecteur1.y * vecteur2.y) + (vecteur1.z * vecteur2.z));
    }

    protected double somme(@NotNull Vecteur3D vecteur1, @NotNull Vecteur3D vecteur2){
        return ((vecteur1.x + vecteur2.x) + (vecteur1.y + vecteur2.y) + (vecteur1.z + vecteur2.z));
    }

    static double sommeStatic(@NotNull Vecteur3D vecteur1, @NotNull Vecteur3D vecteur2){
        return ((vecteur1.x + vecteur2.x) + (vecteur1.y + vecteur2.y) + (vecteur1.z + vecteur2.z));
    }

    static double produitScalaireStatic(@NotNull Vecteur3D vecteur1, @NotNull Vecteur3D vecteur2){
        return ((vecteur1.x * vecteur2.x) + (vecteur1.y * vecteur2.y) + (vecteur1.z * vecteur2.z));
    }

}

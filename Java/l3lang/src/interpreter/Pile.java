package interpreter;
import java.util.ArrayList;

public class Pile {

    public static ArrayList<Integer> MEM;   // Pile
    public static int SP = 0;   // Pointeur de Pile
    public static int PC = 0;   // Pointeur d'instruction

    public Pile(){}

    /**
     * La fonction Add() permet de faire l'addition des 2 derniers éléments de la pile.
     */
    public void Add(){
        if (MEM.size() > 1){
            int add = MEM.remove(-1) + MEM.remove(-2);
            MEM.add(add);
        }
        PC++;
    }

    /**
     * La fonction Sub() permet de faire la soustraction des 2 derniers éléments de la pile.
     */
    public void Sub(){
        if (MEM.size() > 1){
            int sub = MEM.remove(-1) - MEM.remove(-2);
            MEM.add(sub);
        }
        PC++;
    }

    /**
     * La fonction Mul() permet de faire la multiplication des 2 derniers éléments de la pile.
     */
    public void Mul(){
        if (MEM.size() > 1){
            int mul = MEM.remove(-1) * MEM.remove(-2);
            MEM.add(mul);
        }
        PC++;
    }

    /**
     * La fonction Div() permet de faire la division des 2 derniers éléments de la pile.
     */
    public void Div(){
        if (MEM.size() > 1){
            if(MEM.get(-1) > 0 && MEM.get(-2) > 0  ) {
                int div = Math.round(MEM.remove(-1) / MEM.remove(-2));
                MEM.add(div);
            }
        }
        PC++;
    }

    public void Eql()



}

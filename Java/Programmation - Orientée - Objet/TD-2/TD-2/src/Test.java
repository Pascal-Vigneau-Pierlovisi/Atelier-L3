import com.sun.source.tree.InstanceOfTree;

import java.lang.reflect.Type;

public class Test {
    public static void main(String[] args) {

        AutomobileElectricite tesla = new AutomobileElectricite("Tesla V8", 1000, "Vantablack", 3, 2);
        tesla.afficherCaracteristiques();

        AutomobileEssence megane3RS = new AutomobileEssence("Megane 3 RS Trophy", 400, "blanc", 3, 40);
        megane3RS.afficherCaracteristiques();

        ScooterEssence MBKRocket = new ScooterEssence("MBKRocket", "Rouge", 50, 5);
        MBKRocket.afficherCaracteristiques();

        ScooterElectricite Peugeot = new ScooterElectricite("Peugeot", "blanc", 10, 5);
        Peugeot.afficherCaracteristiques();

        Automobile honda = new FabriqueVehiculeEssence("Honda", 49, "bleu", 0, 5).fabriquerAutomobile();

        honda.afficherCaracteristiques();


    }
}

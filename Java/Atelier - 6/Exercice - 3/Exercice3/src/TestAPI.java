import java.lang.Math;
import java.util.Random;

public class TestAPI {



    public static void main(String[] args) {

        int x1 = 10;
        int x2 = 20;

        String n1 = "Pascal";
        String n2 = "Anthony";

        int whoIsFirst = n2.compareTo(n1);
        
        Random r = new Random();

        System.out.println(Math.PI);
        System.out.println(Math.random());
        System.out.println(r.nextInt(4));
        System.out.println(Math.max(x1, x2));
        System.out.println(n2.compareTo(n1));

        if(whoIsFirst < 0){
            System.out.println(n2);
        }


    }
}

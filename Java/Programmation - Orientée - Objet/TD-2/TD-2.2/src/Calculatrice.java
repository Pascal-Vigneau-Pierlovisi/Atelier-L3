public class Calculatrice extends Afficher implements Operation{

    @Override
    public Object addition(Object x, Object y) {
        return (float)x + (float)y;
    }

    @Override
    public Object soustraction(Object x, Object y) {
        return (float)x - (float)y;
    }

    @Override
    public Object multiplication(Object x, Object y) {
        return (float)x * (float)y;
    }

    @Override
    public Object division(Object x, Object y) {
        return (float)x / (float)y;
    }

    @Override
    public Object afficher() {
        return null;
    }
}

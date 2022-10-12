public class Temperature {
    /**
     * Fonction convertF()
     * @param celsius Représente la température en celsius
     * @return La valeur de retour est la température convertie en f𝑎𝑟𝑒𝑛h𝑒𝑖𝑡
     */
    public static double convertF(int celsius){
        return (celsius * 9/5) + 32;
    }

    /**
     * Fonction convertC()
     * @param farenheit Représente la température en farenheit
     * @return La valeur de retour est la conversion de la température en °Celsius
     */
    public static double convertC(double farenheit){
        return (farenheit - 32) * 5/9;
    }
}

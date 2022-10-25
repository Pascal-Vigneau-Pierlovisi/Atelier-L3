public class Generique<E>{
    private E contenu;
    public Generique(E contenu){
        this.contenu = contenu;
    }
    public E getContenu(){
        return contenu;
    }

    /*public static void main(String[] args) {
        Generique<String> gen = new Generique<>("Hello World");
        System.out.println(gen.getContenu());
    }*/
}


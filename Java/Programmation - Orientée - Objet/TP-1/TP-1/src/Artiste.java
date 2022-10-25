import java.util.ArrayList;

public class Artiste {
    private final int idArtiste;
    private String nomArtiste;
    private int nombreAbonne;

    private ArrayList<Titre> lstTitre;
    private static int nbArtiste = 0;

    public Artiste(String nomArtiste, int nombreAbonne){
        nbArtiste++;
        this.idArtiste = nbArtiste;
        this.nomArtiste = nomArtiste;
        this.nombreAbonne = nombreAbonne;
        lstTitre = new ArrayList<>();
    }

    public int getIdArtiste() {
        return idArtiste;
    }

    public String getNomArtiste() {
        return nomArtiste;
    }

    public void setNomArtiste(String nomArtiste) {
        this.nomArtiste = nomArtiste;
    }

    public void setNombreAbonne(int nombreAbonne) {
        this.nombreAbonne = nombreAbonne;
    }

    public ArrayList<Titre> getLstTitre() {
        return lstTitre;
    }

    protected void setLstTitre(ArrayList<Titre> lstTitre) {
        this.lstTitre = lstTitre;
    }

    protected void addTitre(Titre titre){
        if (!lstTitre.contains(titre)){
            lstTitre.add(titre);
        }
        if(!titre.getLstArtiste().contains(this)){
            titre.addArtiste(this);
        }

    }


}

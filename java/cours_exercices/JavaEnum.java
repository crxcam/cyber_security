package cours_exercices;

public class JavaEnum {

	enum Formation {
		ALGO("Algo",2),
		PYTHON("Python",5),
		JAVA("Java language",20),
		CYBER("Cyber securite ",4);

		private String nom;
		private int nbJour;

		Formation(String _nom, int _nbJour) {
			nom = _nom;
			nbJour = _nbJour;
		}

		int get_nb_jour(){
			return this.nbJour;
		}
		String get_nom(){
			return this.nom;
		}

	}

	public static void main(String[] args) {
		Formation maFormation =  Formation.ALGO;
		System.out.println("Enum Formation "+maFormation);
		System.out.println("Enum get_nb_jour "+maFormation.get_nb_jour());
		System.out.println("Enum get_nom "+maFormation.get_nom());




	}
}
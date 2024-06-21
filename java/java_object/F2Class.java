package java_object;

abstract class Humain {
	String nom;
	String prenom;

	Humain(String _nom, String _prenom) {
		nom = _nom;
		prenom = _prenom;
	}

	void dormir() {
		System.out.println("class Humain methode dormir");
	}

}

class Personne extends Humain {
	int position = 0;

	Personne(String nom, String prenom) {
		super(nom, prenom);
	}

	int getPosition() {
		return position;
	}

	void setPosition(int x) {
		if (position > 3000) {
			position = position - 3000 + x;
		}
		if (position == 0) {
			position = x;
		}
	}

	void seDeplacer(int d) {
		this.position = +d;
	}

	void afficher() {
		System.out.println("function afficher de la classe Personne");
		System.out.println("nom : " + nom);
		System.out.println("prenom : " + prenom);
	}

	void parler(String text) {
		System.out.println("function parler de la classe Personne");
		System.out.println("text : " + text);
	}
}

class Bebe extends Personne {
	Bebe(String nom, String prenom) {
		super(nom, prenom);
	}

	@Override
	void afficher() {
		System.out.println("overading methode afficher ");
	}

}

class F2Class {
	public static void main(String[] args) {
		System.out.println("Application START ");
		System.out.println("create clase Personne");
		Personne personne = new Personne("jules", "cesar");
		System.out.println("display clase Personne");
		personne.afficher();
		System.out.println("parler clase Personne");
		personne.parler("Appel de la function:personne.parler");
		System.out.println("create clase Bebe");
		Bebe bebe = new Bebe("mad", "max");
		System.out.println("display clase Bebe");
		bebe.afficher();
		System.out.println("speak clase Bebe");
		bebe.parler("bebe parle ");
		System.out.println("sleep clase Bebe");
		bebe.dormir();

	}
}
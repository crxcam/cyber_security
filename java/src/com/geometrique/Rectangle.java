package src.com.geometrique;

class Rectangle extends Form {
	int longeur;
	int largeur;

	Rectangle(Point p, int _longeur, int _largeur) {
		super(p);
		longeur = _longeur;
		largeur = _largeur;
	}

	@Override
	double calc_perimetre() {
		return (largeur + longeur) * 2;
	}

	@Override
	double calc_surface() {
		return largeur * longeur;
	}

	@Override
	void afficher() {
		System.out.println("###	Affichage de Rectangle	###");
		System.out.println(
				"longeur : " + longeur + " largeur : " + largeur + " surface : " + calc_surface() + " perimetre : "
						+ calc_surface());
		System.out.println("point origin Rectangle position x : " + point.x + " position y : " + point.y);
		System.out.println("distance entre les points : " + point.distance);
		System.out.println();

	}

}
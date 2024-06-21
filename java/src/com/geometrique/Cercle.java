package src.com.geometrique;

class Cercle extends Form {
	int rayon;

	Cercle(Point p, int _rayon) {
		super(p);
		rayon = _rayon;

	}

	@Override
	double calc_perimetre() {
		return (2 * 3.14) * rayon;
	}

	@Override
	double calc_surface() {
		return 3.14 * (2 * rayon);
	}

	@Override
	void afficher() {
		System.out.println("###	Affichage de Cercle	###");
		System.out.println("rayon : " + rayon + " surface : " + calc_surface() + " perimetre : "
				+ calc_surface());
		System.out.println("point origin Cercle position x : " + point.x + " position y : " + point.y);
		System.out.println("distance entre les points : " + point.distance);
		System.out.println();
	}

}
package src.com.geometrique;

abstract class Form {
	Point point;

	Form(Point p) {
		point = p;
	}

	void afficher(){

	}
	double calc_perimetre(){
		return 0;
	}
	double calc_surface(){
		return 0;
	}

}
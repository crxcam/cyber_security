package src.com.geometrique;

class Point {
	int x;
	int y;
	double distance ;

	Point(int _x, int _y) {
		x = _x;
		y = _y;
		distance = distance(_x,_y);
	}

	void afficher() {
		System.out.println("###	Affichage de Point	###");
		System.out.println("X = " + x);
		System.out.println("Y = " + y);
	}

	void seDeplacer(int _x, int _y) {
		x += _x;
		y += _y;
	}

	double distance(int x,int y){
		double r = Math.sqrt(Math.pow(x - x, 2) + Math.pow(y - y, 2));
		return r;
	}

}
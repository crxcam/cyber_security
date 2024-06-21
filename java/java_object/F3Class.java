package java_object;

class Point {
	int x;
	int y;
	int distance = 0;

	Point(int _x, int _y) {
		x = _x;
		y = _y;
	}

	void afficher() {
		System.out.println("X = " + x);
		System.out.println("Y = " + y);
		System.out.println("Distance = " + calcDistance());
	}

	void seDeplacer(int _x, int _y) {
		x += _x;
		y += _y;
	}

	int getDistance() {
		return calcDistance();
	}

	private int calcDistance() {
		if (x == y) {
			return 0;
		} else if (x > y) {
			return x - y;
		} else {
			return y - x;
		}
	}

}

class F3Class {
	public static void main(String[] args) {
		System.out.println("Creation object");
		Point point = new Point(4, 6);
		System.out.println("Afficher object");
		point.afficher();
		System.out.println("Deplacer object");
		point.seDeplacer(8, 2);
		System.out.println("Afficher object");
		point.afficher();

	}
}
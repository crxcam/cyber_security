package cours_exercices;

public class JavaMethodes_Exercice {
	static String log_prefix = "LOG ### => ";

	public static void main(String[] args) {
		// create points
		int[] first_point = build_array_point(10, 20);
		int[] two_point = build_array_point(15, 13);

		// move points
		int[] first_point_after_move = move_point(first_point);
		int[] two_point_after_move = move_point(two_point);
		// calc distance
		double first_distance = calc_distance(first_point[0], two_point[0], first_point[1], two_point[1]);
		double seconde_distance = calc_distance(first_point_after_move[0], two_point_after_move[0],
				first_point_after_move[1], two_point_after_move[1]);
		// display
		System.out.println(log_prefix + "two_point origin");
		display(first_point);
		System.out.println(log_prefix + "two_point origin");
		display(two_point);
		System.out.println(log_prefix + "first_point_after_move");
		display(first_point_after_move);
		System.out.println(log_prefix + "two_point_after_move");
		display(two_point_after_move);

		System.out.println(log_prefix + "distance before mouve :" + first_distance);
		System.out.println(log_prefix + "distance after mouve :" + seconde_distance);
	}

	static void display(int[] array) {
		for (int y = 0; y < array.length; y++) {
			System.out.println(log_prefix + "valeur de tableau " + array[y]);
		}
	}

	public static int[] build_array_point(int x, int y) {
		int[] tab_int = { x, y };
		return tab_int;
	}

	public static int[] move_point(int[] array) {
		int tab_int[] = new int[array.length];
		for (int y = 0; y < array.length; y++) {
			tab_int[y] = (array[y] + 2);
		}
		return tab_int;
	}

	static public double sqr(double a) {
		return a * a;
	}

	static public double calc_distance(double x1, double y1, double x2, double y2) {
		return Math.sqrt(sqr(y2 - y1) + sqr(x2 - x1));
	}

}
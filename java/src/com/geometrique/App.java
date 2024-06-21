package src.com.geometrique;


 class App {
	public static void main(String[] args) {
		System.out.println("###	Application start	###");
		System.out.println("#############################################");
		rectangle_manager();
		System.out.println("#############################################");
		cercle_manager();
	}


	private static void  rectangle_manager(){
		System.out.println("###	rectangle_manager start	###");
		Rectangle rectangle = new Rectangle(new Point(4, 8), 10, 5);
		rectangle.afficher();
		System.out.println("###	deplacement point origin	###");
		rectangle.point.seDeplacer(45,21);
		rectangle.afficher();
	}

	private static void  cercle_manager(){
		System.out.println("###	cercle_manager start	###");
		Cercle cercle = new Cercle(new Point(4, 8), 8);
		cercle.afficher();
		System.out.println("###	deplacement point origin	###");
		cercle.point.seDeplacer(45,21);
		cercle.afficher();
	}
}
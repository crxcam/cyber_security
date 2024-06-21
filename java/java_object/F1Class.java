package java_object;

class Test {
	int t = 12;
	void afficher(){
		System.out.println("les classe Test");
	}
}

class F1Class {
	int x = 2;

	public static void main(String[] args) {
		F1Class mc = new F1Class();
		Test te = new Test();
		te.afficher();
		System.out.println("les classe F1Class" + mc.x);
		System.out.println("les classe Test" + te.t);
	}
}
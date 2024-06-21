package cours_exercices;
public class JavaMethodes {

	public static void main(String[] args) {
		log(String.valueOf(add_int(10, 20)));
	}

	static void log(String msg) {
		String log_prefix = "LOG ### => ";
		System.out.println(log_prefix + msg);
	}

	static int add_int(int x,int y) {
		return (x+y);
	}

}
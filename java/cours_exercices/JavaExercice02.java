package cours_exercices;
/* switch */ 

public class JavaExercice02{
	
	public static void main(String[] args){
		
		String log_prefix = "### => ";
		System.out.println(log_prefix+"start process JavaExercice02 ");
		
	
		int age = 10;
		boolean is_poussin = (age >= 6 && age < 8);
		boolean is_pupille = (age >= 8 && age <= 9);
		boolean is_minime = (age >= 10 && age <= 11);
		boolean is_cadet = (age >= 12);
	
		System.out.println(log_prefix+"age saisie: " + age);
	
		if(is_poussin){
			System.out.println(log_prefix+"categorie poussin");
			return;
		}
		
		if(is_pupille){
			System.out.println(log_prefix+"categorie pupille");
			return;
		}
		
		if(is_minime){
			System.out.println(log_prefix+"categorie minime");
			return;
		}
		
		if(is_cadet){
			System.out.println(log_prefix+"categorie cadet");
			return;
		}
		else{
			System.out.println(log_prefix+"categorie inconnue");
		}
		
	}
	
	
}
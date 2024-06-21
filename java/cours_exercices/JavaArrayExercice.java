package cours_exercices;

public class JavaArrayExercice{
	
	public static void main(String[] args){
		String log_prefix = "### => ";
		System.out.println(log_prefix+"start process JavaArrayExercice ");
		
	int array_size = 10;
	int tab_int[] =  new int[array_size];
	System.out.println(log_prefix+"nombre des elements a afficher "+array_size);
	
	for (int y = 0; y < tab_int.length; y++){
		tab_int[y] = y;
		System.out.println(log_prefix+"passage boucle for "+tab_int[y]);
	}
	/*
	 * 	for (int entier : tableau ){
		System.out.println(log_prefix+"passage boucle for "+entier]);
	}
	 */

	
	}
	
	
}
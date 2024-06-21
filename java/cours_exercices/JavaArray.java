package cours_exercices;



public class JavaArray{
	
	public static void main(String[] args){
		String log_prefix = "### => ";
		System.out.println(log_prefix+"start process JavaArray ");



	
	int[] tab_int = {9,3,6,5,4};
	String[] tab_string = {"tortue","chien","vache","ourse"};
	System.out.println(log_prefix+"element du tableau "+tab_int[2]);
	tab_string[2] = "cochon";
	
	//int tab_int[] =  new int[10];
	
	for (int y = 0; y < tab_int.length; y++){
		System.out.println(log_prefix+"passage boucle for "+tab_int[y]);
	}
	
	
			
	}
	
	
}
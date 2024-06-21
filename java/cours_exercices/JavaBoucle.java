package cours_exercices;
/* boucles */

public class JavaBoucle{
	
	public static void main(String[] args){
		String log_prefix = "### => ";
		System.out.println(log_prefix+"start process JavaBoucle ");
	/* while 
	tan que la condition est vrai 
	
	*/
	
	int i = 0;
	while(i < 10){
		i ++;
		System.out.println(log_prefix+"passage boucle while "+i);
	}
	i = 0;
	
	do{
		i ++;
		System.out.println(log_prefix+"passage boucle do  while "+i);
	}
	while(i < 10);
	

	for (int y = 0; y < 20; y++){
		System.out.println(log_prefix+"passage boucle for "+y);
	}
	
	
			
	}
	
	
}

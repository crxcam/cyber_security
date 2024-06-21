package cours_exercices;

import java.util.ArrayList;
import java.util.HashMap;

public class JavaCollection {

	public static void main(String[] args) {
		ArrayList<String> animals = new ArrayList<>();
		animals.add("chat");
		animals.add("chien");

		for (int i = 0; i < animals.size(); i++) {
			System.out.println("JavaCollection ArrayList display " + animals.get(i));
		}

		System.out.println("JavaCollection ArrayList  " + animals);
		System.out.println("JavaCollection ArrayList hashCode " + animals.hashCode());


		HashMap <String,String> dictionnaire = new HashMap<String,String>();
		dictionnaire.put("cle1","value1");
		dictionnaire.put("cle2","value2");
		dictionnaire.put("cle3","value3");
		dictionnaire.get("cle1");
		dictionnaire.forEach((k,v) -> System.out.println("key: "+k+" value:"+v));

	}
}
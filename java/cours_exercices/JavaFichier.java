package cours_exercices;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;

public class JavaFichier {
	static String file_name = "mon_fichier.txt";
	static File my_file;

	public static void main(String[] args) {
		System.out.println("### => Creation de fichier : " + file_name);
		create_file(file_name);
		System.out.println("### => Ecriture dans de fichier : " + file_name);
		write_file(file_name);
		System.out.println("### => Lecture dans de fichier : " + file_name);
		read_file(file_name);
	}

	public static void create_file(String file_name) {
		try {
			my_file = new File(file_name);
			my_file.createNewFile();
		} catch (IOException e) {

		}
	}

	public static void write_file(String file_name) {
		try {
			FileWriter fileWriter = new FileWriter(file_name);
			PrintWriter printWriter = new PrintWriter(fileWriter);
			printWriter.print("Ecriture premiere ligne ");
			printWriter.printf("\n");
			printWriter.print("Ecriture deuxieme ligne ");
			printWriter.close();
		} catch (IOException e) {
		}
	}

	public static void read_file(String file_name) {
		int cpt_line = 0;
		try (FileReader fileReader = new FileReader(file_name);
				BufferedReader bufferedReader = new BufferedReader(fileReader)) {
			String line;
			while ((line = bufferedReader.readLine()) != null) {
				cpt_line++;
				System.out.println("Ligne n : " + cpt_line + " : " + line);
			}
			fileReader.close();
		} catch (IOException e) {
			System.out.println("Error reading file: " + e.getMessage());
		}
	}

}
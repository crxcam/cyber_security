package cours_exercices;
import java.util.Random;
import java.util.Scanner;

public class JavaChifumi {
	static int player_score = 0;
	static int computer_score = 0;
	static String[] choices = { "Pierre", "Feuille", "Ciseaux" };
	static String current_choice_player = "";
	static String current_choice_computer = "";

	static String[] text_start = { "Bonjour et bienvenue dans le chifumi",
			"Vous jouez contre ordinateur",
			"Vous avez 3 choix [Pierre(touche 1),Feuille(touche 2),Ciseaux(touche 3)]",
			"Le jeux se termine lorsque un joueur (ordinateur où vous a emporter 3 points)",
	};

	public static void main(String[] args) {
		init();
		while (go_next_game()) {
			start_game();
		}
		System.out.println("Partie est terminer.");
	}

	public static void start_game() {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Saisir votre choix: ");
		compare_inputs_values(scanner.nextInt());
		scanner.close();
	}

	static void init() {
		player_score = 0;
		computer_score = 0;
		display_array_msg(text_start);
	}

	static void display_array_msg(String[] array_text) {
		for (int y = 0; y < array_text.length; y++) {
			System.out.println(array_text[y]);
		}
	}

	static int get_random_value() {
		Random rand = new Random();
		return rand.nextInt(3) + 1;
	}

	static void compare_inputs_values(int player_input) {
		if (player_input > 3) {
			System.out.print("Error votre choix est superieur a 3 ");
			return;
		}
		int computer_input = get_random_value();
		// [Pierre(touche 1),Feuille(touche 2),Ciseaux(touche 3)]
		current_choice_player = choices[player_input - 1];
		current_choice_computer = choices[computer_input - 1];

		if (player_input == computer_input) {
			display_score_and_choice();
			return;
		}
		switch (player_input) {
			case 1:
				switch (computer_input) {
					case 2:
						computer_score++;
						break;
					case 3:
						player_score++;
						break;
				}
				break;
			case 2:
				switch (computer_input) {
					case 1:
						player_score++;
						break;
					case 3:
						computer_score++;
						break;
				}
				break;
			case 3:
				switch (computer_input) {
					case 1:
						player_score++;
						break;
					case 2:
						player_score++;
						break;
				}
				break;
			default:
				System.out.println(" Combinaison non trouvé");
		}
		display_score_and_choice();
	}

	static void display_score_and_choice() {
		System.out.println("Joueur a saisie : " + current_choice_player);
		System.out.println("Ordinateur a saisie : " + current_choice_computer);
		System.out.println("Score de joueur : " + player_score);
		System.out.println("Score de l'ordinateur : " + computer_score);
	}

	static boolean go_next_game() {
		return player_score > 2 || computer_score > 2 ? false : true;
	}

}
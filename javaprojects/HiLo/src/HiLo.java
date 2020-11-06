
import java.util.Scanner;

public class HiLo {

	public static void main(String[] args) {
		// get ready for the player to use the keyboard
		Scanner scan = new Scanner(System.in);
		
		//play again string
		String playAgain="";
		
		
		// game loop
		do {
			// counting trials
			int trials=0;
			// create a new random number from 1-100
			int theNumber = (int)(Math.random()*100 + 1);
			
			int guess = 0;
			
			while(guess != theNumber) {
				System.out.println("Guess a number between 1 and 100");
				
				// get the user's guess
				guess = scan.nextInt();
				trials ++;
				if (guess < theNumber) {
					System.out.println(guess + " is too low. Try again!");
				}
				else if(guess > theNumber) {
					System.out.println(guess + " is too high. Try again!");
				}
				else {
					System.out.println(guess + " is correct!. You win! with " + trials + " trials");
				}
			} // end of while loop for guessing
			
			// ask for 'y' to play again
			System.out.println("Would you like to play again? (y/n)?");
			playAgain = scan.next();
			
		} while (playAgain.equalsIgnoreCase("y")); // end of do loop
		//thank you for playing
		System.out.println("Thank you for playing!, Goodbye.");
	} // end of public static void

}// end of public class

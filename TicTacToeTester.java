import java.util.Scanner;


public class TicTacToeTester {

	/**
	 * @param args
	 */
	public static void main(String[] args) 
	{
		TicTacToeClass TTT = new TicTacToeClass();
		
		TTT.length();
		
		//Scanner sc = new Scanner;
		
		TTT.playMove('X', 0, 0);
		TTT.playMove('O', 1, 0);
		TTT.playMove('X', 1, 2);
		TTT.playMove('X', 0, 1);
		TTT.playMove('X', 0, 2);
		TTT.playMove('X', 2, 0);
		TTT.playMove('X', 2, 1);
		TTT.playMove('X', 2, 2);
		TTT.playMove('X', 1, 1);
		
		System.out.println(TTT.playerAt(1, 0));
		System.out.println(TTT.playerAt(2, 0));
		
		System.out.println(TTT.numTurns());
		
		TTT.displayBoard();
	
		System.out.println(TTT.isWinner('X'));
		
	}

}

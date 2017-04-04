/**
* Name: rxu17 
* Date: 01/15/17
* Tic Tac Toe Class returns a tic tac toe board game and has the player input in moves to play with the computer
**/
public class TicTacToeClass 
{
	private char[][] board;
	private int turns;
	
	/**
	* Initializes the tic tac toe board
	**/
	public TicTacToeClass()
	{
		board = new char[3][3];
		for(int i = 0; i < board[0].length; i++)
		{
			for(int j = 0; j < board.length; j++)
			{
				board[i][j] = ' ';
			}
		}
		turns = 0;
	}
	
	/**
	* Returns length of the board
	**/
	public int length()
	{
		return board.length;
	}
	
	/**
	* Check to see if the move played by either player results in a win 
	**/
	public boolean isWinner(char p)
	{
		if(board[0][0] == p && board[1][1] == p && board[2][2] == p)
		{
			return true;
		}
		else if(board[0][0] == p && board[1][0] == p && board[2][0] == p)
		{
			return true;
		}
		else if(board[0][0] == p && board[0][1] == p && board[0][2] == p)
		{
			return true;
		}
		else if(board[1][0] == p && board[1][1] == p && board[1][2] == p)
		{
			return true;
		}
		else if(board[2][0] == p && board[2][1] == p && board[2][2] == p)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	
	/**
	* Checks to see if all the slots in the board has a char or not 
	**/
	public boolean isFull()
	{
		if(turns == 9)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	
	/**
	* Checks to see if it is a draw
	**/
	public boolean isCat()
	{
		if(isFull() && !isWinner('X') || turns == 9 && !isWinner('O'))
		{
			return true; 
		}
		else
		{
			return false;
		}
	}
	
	/**
	* Checks to see if the move played is valid
	**/
	public boolean isValid(int r, int c)
	{
		if(board[r][c] == ' ')
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	
	/**
	* Returns the number of turns taken total in the game
	**/
	public int numTurns()
	{
		return turns;
	}
	
	/**
	* Method for checking the character at a certain coordinate on the board
	**/
	public char playerAt(int r, int c)
	{
		if(board[r][c] == ' ')
		{
			return ' ';
		}
		else if(board[r][c] == 'X')
		{
			return 'X';
		}
		else
		{
			return 'O';
		}
	}
	/**
	* Draws out the tic tac toe board
	**/
	public void displayBoard()
	{
		for(int i = 0; i < board[0].length; i++)
		{
			for(int j = 0; j < board.length; j++)
			{
				System.out.print("|" + board[i][j] + "|");
			}
			System.out.println();
		}
	}
	
	/**
	* Puts the character 'X' or 'O' in the requested coordinate in the board
	**/
	public void playMove(char p, int r, int c)
	{
		if(isValid(r, c))
		{
			board[r][c] = p;
			turns++;
		}
		else
		{
			System.out.println("Can't play that spot");
		}
		if(isCat())
		{
			System.out.println("It's a tie!");
		}
	}
}

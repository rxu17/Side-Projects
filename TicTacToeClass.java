
public class TicTacToeClass 
{
	private char[][] board;
	private int turns;
	
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
	
	public int length()
	{
		return board.length;
	}
	
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
	
	public int numTurns()
	{
		return turns;
	}
	
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

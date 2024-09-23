# TODO: Student writes their name at the top of the file (delete this TODO line when completed) (0.5 pt.)
# Steven Bui             <Date> 11/27/2022
# Assignment #6 Naval Battle
 
# TODO: Ensure that the assignment is turned in by the due date AND Ensure that the files that gets submitted are called
# 'navalBattle.py', 'gameBoard.py', 'gameInput.py', 'gamePlay.py', 'targetBoard.txt', 'board1.txt', and 'board2.txt'.
# These files should be included in a .zip file called 'navalBattle.zip' (1 pt.)
 
# NOTE: All of the 'TODO' statements are contained in navalBattle.py, gamePlay.py and gameInput.py.
 
import gameBoard
import gamePlay
 
def main():
    """This is the main function of the game. It controls the flow/ execution of the entire script.
    """
    gameOver = False
 
    gameboardChoice = 0
    humanGameBoard = None
    targetBoard = None
    computerGameBoard = None
   
    numHumanTargets = 0
    numComputerTargets = 0
   
    print("Welcome to Naval Battle!")
    print()
   
    # TODO: Have student print their name/ section when the script runs (0.5 pt.)
    print("By: Steven Bui")
    print("[COM S 127 <section D>]")
    print()
 
    while gameOver == False:
        choice = input("[p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p":
            # TODO: Fill out the data structures necessary to play the game by calling the methods referenced below. (1 pt.)
 
            # Choose which gameboard to use for the HUMAN player with the chooseHumanGameBoard method in the gameBoard module.
            # Assign this to choice to the gameboardChoice variable.
            gameboardChoice = gameBoard.chooseHumanGameBoard()
           
 
 
            # Load the gameboard for the HUMAN player with the loadGameBoard method in the gameBoard module.
            # Assign the output of this method to the humanGameBoard and numHumanTargets variables.
            humanGameBoard, numHumanTargets = gameBoard.loadGameBoard(gameboardChoice)
         
 
            # Choose which gameboard to use for the COMPUTER player with the chooseComputerGameBoard method in the gameBoard module.
            # Assign this to choice to the gameboardChoice variable.
            gameboardChoice = gameBoard.chooseComputerGameBoard()
 
            # Load the gameboard for the COMPUTER player with the loadGameBoard method in the gameBoard module.
            # Assign the output of this method to the computerGameBoard and numComputerTargets variables.
            computerGameBoard, numComputerTargets = gameBoard.loadGameBoard(gameboardChoice)
            # Load the 'target board' for the HUMAN player to use with the loadTargetBoard method in the gameBoard module.
            # Assign this to choice to the targetBoard variable.
            targetBoard = gameBoard.loadTargetBoard()
 
            # Run the game by passing in the relevant data to the runGame method of the gamePlay module.
            gamePlay.runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets)
        elif choice == "i":
            # TODO: Print out the instructions for the game (1 pt.)
            print("Naval Battle similar to Battle Ship\nPlayers take turns using coordinates guessing the location of ships\nThe game is over when all ships are sunk on oneside")
        elif choice == "q":
            gameOver = True
            # TODO: set gameOver to be True and print a 'goodbye' message to the player (1 pt.)
            print('goodbye')
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()
 
if __name__ == "__main__":
    main()
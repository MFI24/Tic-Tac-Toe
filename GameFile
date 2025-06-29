#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    position = int(position)
    if board[position] == ' ':
        board[position] = mark
            

# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard():
    newBoard = {
        1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6',
        7: '7', 8: '8', 9: '9'
    }
    
    for k, v in board.items():
        if v != ' ':
            newBoard[k] = v

    print('\n {} | {} | {}'.format(newBoard[1], newBoard[2], newBoard[3]))
    print(' ---------')
    print(' {} | {} | {}'.format(newBoard[4], newBoard[5], newBoard[6]))
    print(' ---------')
    print(' {} | {} | {}\n'.format(newBoard[7], newBoard[8], newBoard[9]))


# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or
# position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    if (type(position) == str):
        if position.isdigit() == True:
          position = int(position)
        else:
          print("Input is not a number!")
          return False
        
    if position not in range(1, 10): #out of bound
        print("Position out of bounds!")
        return False
    elif board[position] != ' ': #occupied position
        print("Position is occupied!")
        return False            
    elif position in range(1, 10): #correct input
        return True

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3], #1
    [4, 5, 6], #2
    [7, 8, 9], #3
    [1, 4, 7], #4
    [2, 5, 8], #5
    [3, 6, 9], #6
    [1, 5, 9], #7
    [3, 5, 7] #8
]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    for combo in winCombinations:
        if board[1]  == player and board[2]  == player and board[3]  == player:
          return True
        elif board[4]  == player and board[5]  == player and board[6]  == player:
          return True
        elif board[7]  == player and board[8]  == player and board[9]  == player:
          return True
        elif board[1]  == player and board[4]  == player and board[7]  == player:
          return True
        elif board[2]  == player and board[5]  == player and board[8]  == player:
          return True
        elif board[3]  == player and board[6]  == player and board[9]  == player:
          return True
        elif board[1]  == player and board[5]  == player and board[9]  == player:
          return True
        elif board[3]  == player and board[5]  == player and board[7]  == player:
          return True
    return False


# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
   for v in board.values():
    if v == ' ':
      return False
   return True

#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User

while True:  #loop for restarting the game
  while not gameEnded:
    move = input(currentTurnPlayer + "'s turn, input: ")
    if validateMove(move) == True:
      markBoard(move, currentTurnPlayer)
      printBoard()
    else: #logic to stay on the same turn if validateMove == False
      if currentTurnPlayer == 'X':
        currentTurnPlayer = 'O'
      elif currentTurnPlayer == 'O':
        currentTurnPlayer = 'X'
      printBoard()

    if checkWin(currentTurnPlayer) == True:
      gameEnded = True
      print("Player " + currentTurnPlayer + " has won!\n")
      break
    elif checkFull() ==  True:
      gameEnded = True
      print("It's a tie!")
      break
      
    if currentTurnPlayer == 'X': #switch players
      currentTurnPlayer = 'O'
    else:
      currentTurnPlayer = 'X'

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over

  restart = input("Would you like to have a rematch? ( Y / N ) : ") #logic to restart game
  if (restart.isdigit() == True) or (restart.isnumeric() == True):
    print("Please input 'Y' to continue, or 'N' to stop.\n")
    continue
  elif (restart == "N") or (restart == "n"):
    print("\nThank you for playing!\n")
    break  
  elif (restart == "Y") or (restart == "y"):
    for k in board: #reset board
      board[k] = ' '
    gameEnded = False
  else:
    print("Please input 'Y' to continue, or 'N' to stop.\n")
    continue

  print('\n-+-+-+-+-+-\n\n' +
    'New game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')
  continue

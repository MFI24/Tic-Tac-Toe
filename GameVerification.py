#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# import libraries
import unittest

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



# Main Program, a Tester for your functions
# It does not cover the printBoard() function.

tc = unittest.TestCase()

# Test validateMove()
tc.assertEqual(validateMove(0), False, "validateMove() didn't work as expected with input : 0")
tc.assertEqual(validateMove(10), False, "validateMove() didn't work as expected with input : 10")
tc.assertEqual(validateMove('1'), True, "validateMove() didn't work as expected with input : 1")
tc.assertEqual(validateMove('5'), True, "validateMove() didn't work as expected with input : 5")
tc.assertEqual(validateMove('9'), True, "validateMove() didn't work as expected with input : 9")

testBoard = {
    1: 'X', 2: 'O', 3: 'X',
    4: 'O', 5: 'X', 6: 'O',
    7: ' ', 8: ' ', 9: ' '
}

# Test markBoard()
markBoard(1, 'X')
markBoard(2, 'O')
markBoard(3, 'X')
markBoard(4, 'O')
markBoard(5, 'X')
markBoard(6, 'O')

tc.assertDictEqual(board, testBoard, "markBoard() didn't work as expected")

tc.assertEqual(validateMove('1'), False, "validateMove() didn't work as expected with duplicated input : 1")

# Test checkWin()
tc.assertEqual(checkWin('X'), False, "checkWin() didn't work as expected with input : 'X'")
testBoard[7] = 'X'
markBoard(7, 'X')
tc.assertDictEqual(board, testBoard, "markBoard() didn't work as expected with input (7, 'X')")
tc.assertEqual(checkWin('X'), True, "checkWin() didn't work as expected with input : 'X'")


board = {
    1: 'X', 2: ' ', 3: ' ',
    4: 'O', 5: 'X', 6: ' ',
    7: 'O', 8: ' ', 9: 'X'
}
tc.assertEqual(checkWin('X'), True, "checkWin() didn't work as expected with input : 'X'")
tc.assertEqual(checkWin('O'), False, "checkWin() didn't work as expected with input : 'O'")

board = {
    1: 'O', 2: ' ', 3: ' ',
    4: 'X', 5: 'O', 6: ' ',
    7: 'X', 8: 'X', 9: 'O'
}
tc.assertEqual(checkWin('O'), True, "checkWin() didn't work as expected with input : 'O'")
tc.assertEqual(checkWin('X'), False, "checkWin() didn't work as expected with input : 'X'")

board = {
    1: 'X', 2: 'O', 3: 'O',
    4: 'X', 5: ' ', 6: ' ',
    7: 'X', 8: ' ', 9: ' '
}
tc.assertEqual(checkWin('X'), True, "checkWin() didn't work as expected with input : 'X'")
tc.assertEqual(checkWin('O'), False, "checkWin() didn't work as expected with input : 'O'")

board = {
    1: 'X', 2: 'O', 3: 'X',
    4: 'X', 5: 'O', 6: ' ',
    7: ' ', 8: 'O', 9: ' '
}
tc.assertEqual(checkWin('O'), True, "checkWin() didn't work as expected with input : 'O'")
tc.assertEqual(checkWin('X'), False, "checkWin() didn't work as expected with input : 'X'")

board = {
    1: 'X', 2: 'X', 3: 'X',
    4: 'O', 5: 'O', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}
tc.assertEqual(checkWin('X'), True, "checkWin() didn't work as expected with input : 'X'")
tc.assertEqual(checkWin('O'), False, "checkWin() didn't work as expected with input : 'O'")

board = {
    1: 'X', 2: 'X', 3: ' ',
    4: 'O', 5: 'O', 6: 'O',
    7: 'X', 8: ' ', 9: ' '
}
tc.assertEqual(checkWin('O'), True, "checkWin() didn't work as expected with input : 'O'")
tc.assertEqual(checkWin('X'), False, "checkWin() didn't work as expected with input : 'X'")


# Test checkFull()
tc.assertEqual(checkFull(), False, "checkFull() didn't work as expected")
board = {
    1: 'O', 2: 'X', 3: 'O',
    4: 'O', 5: 'X', 6: 'X',
    7: 'X', 8: 'O', 9: 'X'
}
tc.assertEqual(checkFull(), True, "checkFull() didn't work as expected")

print("All tests passed! Congratulations!")

import random


class Computer:
    size = []
    board = []

    playerLetter = 'O'

    def ComputerMove(self, board, computerLetter):

        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        for i in range(0, 9):
            copy = self.getBoardCopy(board)
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, computerLetter, i)
                if self.isWinner(copy, computerLetter):
                    return i

        # Check if the player could win on his next move, and block them.
        for i in range(0, 9):
            copy = self.getBoardCopy(board)
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, playerLetter, i)
                if self.isWinner(copy, playerLetter):
                    return i


        # Try to take one of the corners, if they are free.
        move = self.chooseRandomMoveFromList(board, [0, 2, 6, 8])
        if move != None:
            return move

        if self.isSpaceFree(board, 4):
            return 4

        # Move on one of the sides.
        return self.chooseRandomMoveFromList(board, [1, 3, 5, 7])

    def makeMove(self, board, letter, move):
        board[move] = letter

    def chooseRandomMoveFromList(self, board, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def isSpaceFree(self, board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def getBoardCopy(self, board):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard


    def isWinner(self ,bo, le):
        return ((bo[6] == le and bo[7] == le and bo[8] == le) or
                (bo[3] == le and bo[4] == le and bo[5] == le) or
                (bo[0] == le and bo[1] == le and bo[2] == le) or
                (bo[6] == le and bo[3] == le and bo[0] == le) or
                (bo[7] == le and bo[4] == le and bo[1] == le) or
                (bo[8] == le and bo[5] == le and bo[2] == le) or
                (bo[6] == le and bo[4] == le and bo[2] == le) or
                (bo[8] == le and bo[4] == le and bo[0] == le))
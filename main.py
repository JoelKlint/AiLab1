from game import GameState
from move import Move
from minimax import AI
import copy
import sys

print ("")
print('Welcome to Reversi Human!')
print('It is you, against me.')
print('For how long would you like me to think?')
print('1: Not very long')
print('2: Average long')
print('3: Chuck norris long')
depth = input('Well? ')
depth = int(depth)*2


game = GameState()
game.initialize()
while (True):
    if (len(game.validMoves()) == 0):
        if (game.stateValue() > 0):
            print ('Human Won!!')
        elif(game.stateValue() < 0):
            print ('Computer Won!!')
        else:
            print ('Its a draw!')
        sys.exit()
        
    
    coordinates = [1]
    while(len(coordinates) != 2):
        print ("")
        if (game.getPlayerOneTurn()):
            game.printGameState()
            coordinates = input('Where do you want to place your brick? (row, col): \n').split(' ')
            while len(coordinates) is not 2:
                print("Input two values")
                coordinates = input('Where do you want to place your brick? (row, col): \n').split(' ')
            x = int(coordinates[0]) - 1
            y = int(coordinates[1]) - 1
            while not game.placeDisk(Move(x, y)):
                print("Invalid input, try again")
                coordinates = input('Where do you want to place your brick? (row, col): \n').split(' ')
                x = int(coordinates[0]) - 1
                y = int(coordinates[1]) - 1
        else:
            print("I am using my superbrain now...")
            ai = AI()
            aiGame = copy.deepcopy(game)
            action = ai.minimax(aiGame, depth)
            game.placeDisk(action['move'])

            print ('I placed in: ' + str(action['move'].getX() + 1) + ' ' + str(action['move'].getY() + 1))






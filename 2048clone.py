import random
from time import sleep

#VARIABLES

user = ''
end_num = 64
firstLoop = True
boardSize = 4
gameBoard = [[0 for i in range(boardSize)] for i in range(boardSize)]
endMessage = ''

#GAME FUNCTIONS

def addNum():
	num = random.randint(0, 1)
	emptySpot = False
	row = random.randint(0, boardSize - 1)
	col = random.randint(0, boardSize - 1)
	if num == 1:
		num = 4
	else:
		num = 2
	if boardFull() == False:
		while emptySpot == False:
			if gameBoard[row][col] == 0:
				gameBoard[row][col] = num
				emptySpot = True
			else:
				row = random.randint(0, boardSize - 1)
				col = random.randint(0, boardSize - 1)

def checkForEnd():
	noMoves = True
	if boardFull() == True:
		for row in range(0, boardSize - 1):
			for col in range(0, boardSize - 1):
				if gameBoard[row][col] == gameBoard[row+1][col]:
					noMoves = False
				if gameBoard[row][col] == gameBoard[row][col+1]:
					noMoves = False
		return noMoves
	else:
		return False

def getWinStatus():
	global endMessage
	win = False
	for row in range(0, boardSize):
		for col in range(0, boardSize):
			if gameBoard[row][col] == end_num:
				win = True
	if win == True:
		endMessage = 'Congratulations, you win!\n'
	else:
		endMessage = 'Sorry, no more moves are available. Try again!\n'
	return win

def boardFull():
	Empty = False
	for list in gameBoard:
		for i in list:
			if i == 0:
				Empty = True
				return False
	if Empty == False:
		return True

def shiftUp():
	tileMoved = False
	for col in range(0, boardSize):
		topMerged = False
		midMerged = False
		botMerged = False
		for i in range(0, boardSize - 1):
			for row in range(1, boardSize):
				if gameBoard[row-1][col] == 0:
					gameBoard[row-1][col] = gameBoard[row][col]
					if gameBoard[row][col] != 0:
						tileMoved = True
						gameBoard[row][col] = 0
				elif gameBoard[row-1][col] == gameBoard[row][col]:
					if row == 1:
						if not topMerged and not midMerged:
							gameBoard[row-1][col] = gameBoard[row-1][col] + gameBoard[row][col]
							gameBoard[row][col] = 0
							tileMoved = True
							topMerged = True
					elif row == 2:
						if not midMerged and not botMerged:
							gameBoard[row-1][col] = gameBoard[row-1][col] + gameBoard[row][col]
							gameBoard[row][col] = 0
							tileMoved = True
							midMerged = True
					elif row == 3:
						if not botMerged:		
							gameBoard[row-1][col] = gameBoard[row-1][col] + gameBoard[row][col]
							gameBoard[row][col] = 0
							tileMoved = True
							topMerged = True
	return tileMoved

def shiftLeft():
	tileMoved = False
	for row in range(0, boardSize):
		leftMerged = False
		midMerged = False
		rightMerged = False
		for i in range(0, boardSize - 1):
			for col in range(1, boardSize):
				if gameBoard[row][col-1] == 0:
					gameBoard[row][col-1] = gameBoard[row][col]
					if gameBoard[row][col] != 0:
						tileMoved = True
						gameBoard[row][col] = 0
				elif gameBoard[row][col-1] == gameBoard[row][col]:
					if (col == 1):
						if not leftMerged and not midMerged:
							gameBoard[row][col-1] = gameBoard[row][col-1] + gameBoard[row][col]
							gameBoard[row][col] = 0
							tileMoved = True
							leftMerged = True
					elif col == 2:
						if not midMerged and not rightMerged:
							gameBoard[row][col-1] = gameBoard[row][col-1] + gameBoard[row][col]
							gameBoard[row][col] = 0
							tileMoved = True
							midMerged = True
					elif col == 3:
						if not rightMerged:		
							gameBoard[row][col-1] = gameBoard[row][col-1] + gameBoard[row][col]
							gameBoard[row][col] = 0
							tileMoved = True
							rightMerged = True
	return tileMoved

def shiftDown():
	tileMoved = False
	for col in range(0, boardSize):
		topMerged = False
		midMerged = False
		botMerged = False
		for i in range(0, boardSize - 1):
			for row in range(2, -1, -1):
				if gameBoard[row+1][col] == 0:
					gameBoard[row+1][col] = gameBoard[row][col]
					if (gameBoard[row][col] != 0):
						tileMoved = True
						gameBoard[row][col] = 0
				elif gameBoard[row+1][col] == gameBoard[row][col]:
					if row == 2:
						if not botMerged and not midMerged:
							gameBoard[row+1][col] = gameBoard[row+1][col] + gameBoard[row][col]
							gameBoard[row][col] = 0
							tileMoved = True
							botMerged = True
					elif row == 1:
						if not midMerged and not topMerged:
							gameBoard[row+1][col] = gameBoard[row+1][col] + gameBoard[row][col]
							gameBoard[row][col] = 0
							tileMoved = True
							midMerged = True
					elif row == 0:
						if not topMerged:		
							gameBoard[row+1][col] = gameBoard[row+1][col] + gameBoard[row][col]
							gameBoard[row][col] = 0
							tileMoved = True
							topMerged = True
	return tileMoved

def shiftRight():
	tileMoved = False
	for row in range(0, boardSize):
		leftMerged = False
		midMerged = False
		rightMerged = False
		for i in range(0, boardSize - 1):
			for col in range(2, -1, -1):
				if gameBoard[row][col+1] == 0:
					gameBoard[row][col+1] = gameBoard[row][col]
					if gameBoard[row][col] != 0:
						tileMoved = True
						gameBoard[row][col] = 0
				elif gameBoard[row][col+1] == gameBoard[row][col]:
					if col == 2:
						if not rightMerged and not midMerged:
							gameBoard[row][col+1] = gameBoard[row][col+1] + gameBoard[row][col]
							gameBoard[row][col] = 0
							tileMoved = True
							rightMerged = True
					elif col == 1:
						if not midMerged and not leftMerged:
							gameBoard[row][col+1] = gameBoard[row][col+1] + gameBoard[row][col]
							gameBoard[row][col] = 0
							tileMoved = True
							midMerged = True
					elif col == 0:
						if not leftMerged:		
							gameBoard[row][col+1] = gameBoard[row][col+1] + gameBoard[row][col]
							gameBoard[row][col] = 0
							tileMoved = True
							leftMerged = True
	return tileMoved

def processInput():
    successful = False
    if user == 'w': # Up
        successful = shiftUp()
        successful == True
        addNum()
    elif user == 'a': # Left
        successful = shiftLeft()
        if successful == True:
            addNum()
    elif user == 's': # Down
        successful = shiftDown()
        if successful == True:
            addNum()
    elif user == 'd': # Right
        successful = shiftRight()
        if successful == True:
            addNum()
    elif user == 'q':
        print('Exiting...')
        sleep(0.5)

def printBoard():
    print('\033[H\033[J')
    print('\nPlaying until:',str(end_num))
    print('-----------------')
    
    for rowValue in gameBoard:
        for i in rowValue:
            if i == 0:
                print('|\u001b[0;30m',str(i),end=' \u001b[0m')
            elif i == 2:
                print('|\u001b[0;33m',str(i),end=' \u001b[0m')
            elif i == 4:
                print('|\u001b[0;35m',str(i),end=' \u001b[0m')
            elif i == 8:
                print('|\u001b[0;36m',str(i),end=' \u001b[0m')
            elif i == 16:
                print('|\u001b[1;34m',str(i),end='\u001b[0m')
            elif i == 32:
                print('|\u001b[1;36m',str(i),end='\u001b[0m')
            elif i == 64:
                print('|\u001b[1;33m\033[1m',str(i),end='\u001b[0m')
        print('|')
        print('-----------------')

#GAME INTERFACE

print('\033[H\033[J')
print('Welcome to 2048!')
print('---------------')
print('Press \'q\' to quit')
user = input('Press any key to start: ')

while user != 'q':
    if user != 'q':
        if firstLoop == True:
            addNum()
            addNum()
            firstLoop = False

        if getWinStatus() == False and checkForEnd() == False:
            printBoard()
            user = input('Enter a move: ').lower().replace(' ','')
            processInput()

        else:
            printBoard()
            print(endMessage)
            user = 'q'
    elif user == 'q':
        processInput()
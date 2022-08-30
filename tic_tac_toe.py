import random

board=["-", "-", "-",
       "-", "-", "-",
       "-", "-", "-"]
jugador_actual = 'X'

ganador = None

juego_en_ejecucion = True

#Mostrar el tablero
def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])

    print(board[3] + '|' + board[4] + '|' + board[5])

    print(board[6] + '|' + board[7] + '|' + board[8])


def playerInput(board):
    entrada = int(input(' Ingresa un número 1-9: '))
    if entrada > 0 and entrada < 10 and board[entrada-1] == '-':
        board[entrada-1] = jugador_actual
    else:
        print('¡Opps ese lugar ya ha sido marcado!')


def verifyHorizontal(board):
    global ganador
    if board[0] == board[1] ==board[2] and board[0] != "-":
        ganador = board[0]
        return True
    elif board[3] == board[4] ==board[5] and board[3] != "-":
        ganador = board[3]
        return True
    elif board[6] == board[7] ==board[8] and board[6] != "-":
        ganador = board[6]
        return True

def verifyVertical(board):
    if board[0] == board[3] ==board[6] and board[0] != "-":
        ganador = board[0]
        return True
    elif board[1] == board[4] ==board[7] and board[1] != "-":
        ganador = board[1]
        return True
    elif board[2] == board[5] ==board[8] and board[2] != "-":
        ganador = board[2]
        return True

def verifyDiagonal(board):
    if board[0] == board[4] ==board[8] and board[0] != "-":
        ganador = board[0]
        return True
    elif board[2] == board[4] ==board[6] and board[2] != "-":
        ganador = board[2]
        return True

def checkEmpate(board):
    global juego_en_ejecucion
    if '-' not in board:
        printBoard(board)
        print('¡Es un empate!')
        juego_en_ejecucion = False

def checkGanador():
    if verifyDiagonal(board) or verifyVertical(board) or verifyHorizontal(board):
        print(f'El ganador es {ganador}')
        juego_en_ejecucion = False

def changePlayer():
    global jugador_actual
    if jugador_actual == 'X':
        jugador_actual = 'O'
    else:
        jugador_actual = 'X'

#Computer
def computer(board):
    while jugador_actual == 'O':
        position = random.randint(0, 8)
        if board[position] == '-':
            board[position] = 'O'
            changePlayer()

while juego_en_ejecucion:
    printBoard(board)
    playerInput(board)

    changePlayer()

    computer(board)
    checkGanador()
    checkEmpate(board)
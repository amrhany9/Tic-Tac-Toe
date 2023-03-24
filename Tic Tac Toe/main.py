board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

current_player = 'X'
winner = None
RunningGame = True

# printing the board
def print_board():
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

# take input from player 
def player_input():
    inp = int(input("Enter Number Player " + current_player + "from 1-9:"))
    if inp <= 9 and inp >= 1 and board[inp-1] == '-':
        board[inp-1] = current_player
    else:
        print("Oops , another player put in this place!")

# check for win or tie 
def checkHorizontle():
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow():
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def checkDiag():
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True

def checkIfWin():
    global RunningGame
    if checkHorizontle():
        print_board()
        print(f"The winner is {winner}!")
        RunningGame = False

    elif checkRow():
        print_board()
        print(f"The winner is {winner}!")
        RunningGame = False

    elif checkDiag():
        print_board()
        print(f"The winner is {winner}!")
        RunningGame = False


def checkIfTie():
    global RunningGame
    if "-" not in board:
        print_board()
        print("It is a tie!")
        RunningGame = False

#switch the player 
def switch():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


while RunningGame:
    print_board()
    player_input()
    checkIfWin()
    checkIfTie()
    switch()
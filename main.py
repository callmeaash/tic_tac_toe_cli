import random

board = ['-', '-', '-','-','-','-','-','-','-']
current_player = 'X'
winner = None
game_running = True
print("\n")

def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def player_input(board):

    while(True):
        try:
            response = int(input("Enter a number 1 to 9: "))
        except ValueError:
            print("Provide valid number")
            continue
        if response > 0 and response <= 9 and board[response-1] == "-":
            board[response-1] = current_player
            break
        else:
            print("Invalid Response")

def check_horizontal(board):
    if board[0] == board[1] == board[2] and board[2] != '-':
        print(f"The winner is {board[0]}")
        return False

    elif board[3] == board[4] == board[5] and board[4] != '-':
        print(f"The winner is {board[3]}")
        return False

    elif board[6] == board[7] == board[8] and board[7] != '-':
        print(f"The winner is {board[7]}")
        return False
    else:
        return True

def check_vertical(board):
    if board[0] == board[3] == board[6] and board[3] != '-':
        print(f"The winner is {board[0]}")
        return False

    elif board[1] == board[4] == board[7] and board[4] != '-':
        print(f"The winner is {board[1]}")
        return False

    elif board[2] == board[5] == board[8] and board[2] != '-':
        print(f"The winner is {board[5]}")
        return False
    
    else:
        return True

def check_diagonal(board):
    if board[0] == board[4] == board[8] and board[4] != '-':
        print(f"The winner is {board[0]}")
        return False

    elif board[6] == board[4] == board[2] and board[4] != '-':
        print(f"The winner is {board[6]}")
        return False
    
    else:
        return True
    
def check_tie(board):
    for spot in board:
        if spot == "-":
            return False
    return True

def ai_input(board):
    while True:
        choice = random.randint(0,8)
        if board[choice] != '-':
            continue
        else:
            board[choice] = 'O'
            break

while game_running:
    display_board(board)
    player_input(board)
    game_running = check_horizontal(board) and game_running
    game_running = check_vertical(board) and game_running
    game_running = check_diagonal(board) and game_running
    if game_running:
        ai_input(board)
        game_running = check_horizontal(board) and game_running
        game_running = check_vertical(board) and game_running
        game_running = check_diagonal(board) and game_running

    if check_tie(board):
        print("It's a tie")
        break

display_board(board)
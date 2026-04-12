board = [' ' for i in range(9)]

def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def check_winner(player):
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True
    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def play_game():
    current_player = 'BAT'

    for turn in range(9):
        print_board()
        print(current_player + " turn")

        try:
            move = int(input("Enter position (1-9): ")) - 1
        except:
            print("Enter number only")
            continue

        if move < 0 or move > 8 or board[move] != ' ':
            print("Invalid move")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(current_player + " wins")
            return

        if current_player == 'BAT':
            current_player = 'BALL'
        else:
            current_player = 'BAT'

    print_board()
    print("Match draw")

print("Cricket Tic Tac Toe")
play_game()

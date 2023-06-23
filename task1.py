# Tic-Tac-Toe

# Create the game board
board = [' ' for _ in range(9)]

# Function to print the game board
def print_board():
    print('---------')
    for i in range(3):
        print('|', board[i * 3], '|', board[i * 3 + 1], '|', board[i * 3 + 2], '|')
        print('---------')

# Function to check if there's a winner
def check_winner():
    # Check rows
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != ' ':
            return board[i * 3]
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    return None

# Function to play the game
def play_game():
    current_player = 'X'
    while True:
        print_board()
        print("It's", current_player, "'s turn.")
        position = int(input('Enter the position (1-9): ')) - 1
        if board[position] == ' ':
            board[position] = current_player
            winner = check_winner()
            if winner:
                print_board()
                print('Congratulations!', winner, 'wins!')
                break
            if ' ' not in board:
                print_board()
                print("It's a tie!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Invalid move. Try again.')

# Start the game
play_game()

             
# 😊😊😊 .:: STEP 1 ::.
def show_board():
    global game_board
    print(f"{game_board[0]}|{game_board[1]}|{game_board[2]}")
    print(f"{game_board[3]}|{game_board[4]}|{game_board[5]}")
    print(f"{game_board[6]}|{game_board[7]}|{game_board[8]}")


# 💀💀💀 .:: STEP 3 ::.
def choose_symbols():
    while True:
        symbol = input("Player 1, choose your symbol (X/O): ").upper()
        if symbol == 'X' or symbol == 'O':
            player1 = symbol
            player2 = 'O' if player1 == 'X' else 'X'
            global current_player
            current_player = player1
            print(f"Player 1 is '{player1}', Player 2 is '{player2}'.")
            return player1, player2, current_player
        else:
            print("Invalid input. Please enter only 'X' or 'O'.")

def turn(current_player):
    print(f"It's {current_player}'s turn now.")


# 😵‍💫😵‍💫😵‍💫 .:: STEP 4 ::.          #assume:player1 X  / player2 O 
def start_play(current_player):
    global game_board
    while True:
        number=int(input(f"player {current_player} choose a number between 1-9 : "))
        index=number-1
        if game_board[index]=='-':
            game_board[index]=current_player
            break
        else:
            print('this position is already taken choose another one ')
        


# .:: STEP 5 ::.
def check_win(current_player):
    global game_board
    if game_board[0:3]==[current_player]*3 or game_board[3:6]==[current_player]*3 or game_board[6:9]==[current_player]*3:
        return f"player {current_player} won"
    elif game_board[0:7:3]==[current_player]*3 or game_board[1:8:3]==[current_player]*3 or game_board[2:9:3]==[current_player]*3:
        return f"player {current_player} won"
    elif game_board[0:9:4]==[current_player]*3 or game_board[2:8:2]==[current_player]*3:
        return f"player {current_player} won"
    elif '-' not in game_board:
        return'Tie'
    else:
        return'the game should go on'



# .:: Step 6 ::.
def switch(current_player):
    if current_player=='X':
        return 'O'
    else:
        return 'X'


#.::Step 7 ::.
if __name__ == "__main__":
    print("Welcome to the Tic Tac Toe game!")
    game_board=['-','-','-','-','-','-','-','-','-']
    show_board()
    player1, player2, current_player =  choose_symbols()
    while True:
        turn(current_player)
        start_play(current_player)
        show_board()
        result = check_win(current_player)
        if result != 'the game should go on':
            print(result)
            break
        current_player = switch(current_player)

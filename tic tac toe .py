print("Welcome to Tic Tac Toe!")
player = input("Player 1: would you like to be X or O? ")
if player != "X" or "O":
    print("Choose X or O!")
    player = input("Would you like to be X or O? ")

player1 = input("Player 2: and would you like to be X or O? ")
if player == player1:
    print("You can't choose the same character!")
    player1 = input("So would you like to be X or O? ")
elif player1 != "X" or "O":
    print("Choose X or O!")
    player1 = input("Would you like to be X or O? ")

current_player = player
player_choice = {'X' : "", 'O' : ""}
print(f"[1] [2] [3]\n[4] [5] [6]\n[7] [8] [9]")
XO = [" "," ", " ", " ", " ", " ", " ", " ", " ", " "]
element = int(input(f"Which place would you like to place {player}? "))

if current_player == player:
    current_player = player1
else:
    current_player = player

if player == "X" or "O":
    print(f"[1] [2] [3]\n[4] [5] [6]\n[7] [8] [9]")
else:
    print("Not X or O! Choose X or O")

while element >= 1 and element <= 9:
    XO[element - 1] = player
    print(f"[{XO[0]}] [{XO[1]}] [{XO[2]}]\n[{XO[3]}] [{XO[4]}] [{XO[5]}]\n[{XO[6]}] [{XO[7]}] [{XO[8]}]")
    element = int(input(f"Which place would you like to place {player}? "))

if player == "X":
    player_choice["X"] = current_player
    if current_player == player:
        player_choice["O"] = player1
    else:
        player_choice["O"] = player
elif player == "O":
    player_choice["O"] = current_player
    if current_player == player:
        player_choice["X"] = player1
    else:
        player_choice["X"] = player

def check_winner(current_player):
    win_comb = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]



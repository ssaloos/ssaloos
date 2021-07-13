import random
import string
print("Welcome to Tic Tac Toe!")
XO = [" "," ", " ", " ", " ", " ", " ", " ", " ", " "]
player_choice = {'X' : "", 'O' : ""}
def print_tic_tac_toe():
    print(" ")
def check_empty():
    empty_index = []
    for index in range(9):
        if XO[index] == " ":
            empty_index.append(index)
    return empty_index
def check_draw():
    count = 0
    for element in XO:
        if element == " ":
            count = count + 1
    return count
print(check_draw())
def check_winner():
    win_comb = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    if player_choice("X") == win_comb:
        print("X wins!")
    elif player_choice("O") == win_comb:
        print("O wins!")
# print(check_winner())
    # winner = xo_game(options[choice-1])
player = input("Player 1: would you like to be X or O? ")
cur_player = player
player1 = (" ")
if cur_player == "X":
    player1 = "O"
elif cur_player == "O":
    player1 = "X"
print(f"Player 2 (Computer) is : {player1}")
print(f"[1] [2] [3]\n[4] [5] [6]\n[7] [8] [9]")
element = int(input(f"Which place would you like to place {player}? "))
def xo_game(cur_player):
    values = [" " for x in range(9)]
    player_pos = {"X":[ ], "O":[ ]}
    while True:
        print(f"[1] [2] [3]\n[4] [5] [6]\n[7] [8] [9]")
        player = input("Player 1: would you like to be X or O? ")
        cur_player = player
        player1 = (" ")
        if cur_player == "X":
            player1 = "O"
        elif cur_player == "O":
            player1 = "X"
        print(f"Player 2 (Computer) is : {player1}")
        XO = [" "," ", " ", " ", " ", " ", " ", " ", " ", " "]
        element = int(input(f"Which place would you like to place {player}? "))
        if element < 1 or element > 9:
            print("Choose a number from 1-9!")
            continue
        if values[element-1] != " ":
            print("Place already filled. Try again!")
            continue
        values[element-1] = cur_player
        player_pos[cur_player].append(element)
        if values[element-1] != ' ':
            print("Place filled. Try again!")
            continue
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!")
            return cur_player
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            return check_draw
        if cur_player == player:
            cur_player == player1
        else:
            cur_player == player
while element >= 1 and element <= 9:
    XO[element - 1] = player
    print(f"[{XO[0]}] [{XO[1]}] [{XO[2]}]\n[{XO[3]}] [{XO[4]}] [{XO[5]}]\n[{XO[6]}] [{XO[7]}] [{XO[8]}]")
    player1_choice = random.choice(check_empty())
    print(player1_choice)
    random.randint(1,9)
    element = player1_choice
    XO[element - 1] = player1
    print(f"[{XO[0]}] [{XO[1]}] [{XO[2]}]\n[{XO[3]}] [{XO[4]}] [{XO[5]}]\n[{XO[6]}] [{XO[7]}] [{XO[8]}]")
    element = int(input(f"Which place would you like to place {player}? "))
    player_choice = random.choice(check_empty())
    element1 = player_choice
    XO[element1 - 1] = player
    print(f"[{XO[0]}] [{XO[1]}] [{XO[2]}]\n[{XO[3]}] [{XO[4]}] [{XO[5]}]\n[{XO[6]}] [{XO[7]}] [{XO[8]}]")





import random
print("Welcome to Tic Tac Toe!")
def check_empty():
    empty_index = []
    for index in range(9):
        if XO[index] == " ":
            empty_index.append(index)

    return empty_index
player_choice = {'X' : "", 'O' : ""}
player = input("Player 1: would you like to be X or O? ")
current_player = player
player1 = (" ")
if current_player == "X":
    player1 = "O"
elif current_player == "O":
    player1 = "X"
print(f"Player 2 is : {player1}")
print(f"[1] [2] [3]\n[4] [5] [6]\n[7] [8] [9]")
XO = [" "," ", " ", " ", " ", " ", " ", " ", " ", " "]
element = int(input(f"Which place would you like to place {player}? "))

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
    player1_choice = random.choice(check_empty())
    print(player1_choice)
    random.randint(1,9)
    element = player1_choice
    XO[element - 1] = player1
    print(f"[{XO[0]}] [{XO[1]}] [{XO[2]}]\n[{XO[3]}] [{XO[4]}] [{XO[5]}]\n[{XO[6]}] [{XO[7]}] [{XO[8]}]")
    element = int(input(f"Which place would you like to place {player}? "))
    XO[element - 1] = player
    print(f"[{XO[0]}] [{XO[1]}] [{XO[2]}]\n[{XO[3]}] [{XO[4]}] [{XO[5]}]\n[{XO[6]}] [{XO[7]}] [{XO[8]}]")
def check_winner(current_player):
    win_comb = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]



import random
import time
print("Welcome to Tic Tac Toe!")
XO = [" "," ", " ", " ", " ", " ", " ", " ", " ", " "]
empty_list = []
def check_empty():
    empty_index = []
    for index in range(9):
        if XO[index] == " ":
            empty_index.append(index)
    return empty_index
def check_winner():
    if XO[0] == "X" and XO[1] == "X" and XO[2] == "X":
        print ("X won!")
        return True
    elif XO[0] == "O" and XO[1] == "O" and XO[2] == "O":
        print ("O won!")
        return True
    elif XO[0] == "X" and XO[3] == "X" and XO[6] == "X":
        print ("X won!")
        return True
    elif XO[0] == "O" and XO[3] == "O" and XO[6] == "O":
        print ("O won!")
        return True
    elif XO[3] == "X" and XO[4] == "X" and XO[5] == "X":
        print ("X won!")
        return True
    elif XO[3] == "O" and XO[4] == "O" and XO[5] == "O":
        print ("O won!")
        return True
    elif XO[6] == "X" and XO[7] == "X" and XO[8] == "X":
        print ("X won!")
        return True
    elif XO[6] == "O" and XO[7] == "O" and XO[8] == "O":
        print ("O won!")
        return True
    elif XO[1] == "X" and XO[4] == "X" and XO[7] == "X":
        print ("X won!")
        return True
    elif XO[1] == "O" and XO[4] == "O" and XO[7] == "O":
        print ("O won!")
        return True
    elif XO[2] == "X" and XO[5] == "X" and XO[8] == "X":
        print ("X won!")
        return True
    elif XO[2] == "O" and XO[5] == "O" and XO[8] == "O":
        print ("O won!")
        return True
    elif XO[0] == "X" and XO[4] == "X" and XO[8] == "X":
        print ("X won!")
        return True
    elif XO[0] == "O" and XO[4] == "O" and XO[8] == "O":
        print ("O won!")
        return True
    elif XO[2] == "X" and XO[4] == "X" and XO[6] == "X":
        print ("X won!")
        return True
    elif XO[2] == "O" and XO[4] == "O" and XO[6] == "O":
        print ("O won!")
        return True
    return False
def check_draw():
    count = 0
    for element in XO:
        if element != " ":
            count = count + 1
    return count
check_draw()
check_winner()
name = input("Player 1, what's your name? ")
player = input(f"Hi, {name}! Would you like to be X or O? ")
if player == "X":
    player1 = "O"
elif player == "O":
    player1 = "X"
print(f"Player 2 (Computer) is : {player1}")
print(f"[1] [2] [3]\n[4] [5] [6]\n[7] [8] [9]")
element = int(input(f"{name}, which place would you like to place {player}? "))
XO[element - 1] = player
print(f"[{XO[0]}] [{XO[1]}] [{XO[2]}]\n[{XO[3]}] [{XO[4]}] [{XO[5]}]\n[{XO[6]}] [{XO[7]}] [{XO[8]}]")
while element >= 1 and element <= 9:
    empty_list.append(element)
    player1_choice = random.choice(check_empty())
    print("Computer is choosing...")
    time.sleep(0.6)
    element1 = player1_choice
    XO[element1] = player1
    print(f"[{XO[0]}] [{XO[1]}] [{XO[2]}]\n[{XO[3]}] [{XO[4]}] [{XO[5]}]\n[{XO[6]}] [{XO[7]}] [{XO[8]}]")
    if check_winner():
        break
    element = int(input(f"{name}, which place would you like to place {player}? "))
    XO[element - 1] = player
    print(f"[{XO[0]}] [{XO[1]}] [{XO[2]}]\n[{XO[3]}] [{XO[4]}] [{XO[5]}]\n[{XO[6]}] [{XO[7]}] [{XO[8]}]")
    element1 = player1_choice
    XO[element1] = player1
    print(f"[{XO[0]}] [{XO[1]}] [{XO[2]}]\n[{XO[3]}] [{XO[4]}] [{XO[5]}]\n[{XO[6]}] [{XO[7]}] [{XO[8]}]")
    player1_choice = random.choice(check_empty())
    check_draw()
    if check_winner():
        break

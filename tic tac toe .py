print("Welcome to Tic Tac Toe!")
character = input("Would you like to be X or O? ")
print(f"[1] [2] [3]\n[4] [5] [6]\n[7] [8] [9]")
XO = [" "," ", " ", " ", " ", " ", " ", " ", " ", " "]

element = int(input(f"Which place would you like to place {character}? "))

if element >= 1 and element <= 9:
    XO[element - 1] = character

print(f"[{XO[0]}] [{XO[1]}] [{XO[2]}]\n[{XO[3]}] [{XO[4]}] [{XO[5]}]\n[{XO[6]}] [{XO[7]}] [{XO[8]}]")

element = input(f"Which place would you like to place {character}? ")


print(f"[{XO[0]}] [{XO[1]}] [{XO[2]}]\n[{XO[3]}] [{XO[4]}] [{XO[5]}]\n[{XO[6]}] [{XO[7]}] [{XO[8]}]")


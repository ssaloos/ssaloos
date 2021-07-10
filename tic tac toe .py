print("Welcome to Tic Tac Toe!")
character = input("Would you like to be X or O? ")
options = ['X', 'O']
print(f"[1] [2] [3]\n[4] [5] [6]\n[7] [8] [9]")
XO = ["O, O, O, O, O, O, O, O, O"]

element = input(f"Which place would you like to place {character}? ")

# if element == "1":
#     print(f"[{character}] [] []\n[] [] []\n[] [] []")
# elif element == "2":
#     print(f"[] [{character}] []\n[] [] []\n[] [] []")
# elif element == "3":
#     print(f"[] [] [{character}]\n[] [] []\n[] [] []")
# elif element == "4":
#     print(f"[] [] []\n[{character}] [] []\n[] [] []")
# elif element == "5":
#     print(f"[] [] []\n[] [{character}] []\n[] [] []")
# elif element == "6":
#     print(f"[] [] []\n[] [] [{character}]\n[] [] []")
# elif element == "7":
#     print(f"[] [] []\n[] [] []\n[{character}] [] []")
# elif element == "8":
#     print(f"[] [] []\n[] [] []\n[] [{character}] []")
# elif element == "9":
#     print(f"[] [] []\n[] [] []\n[] [] [{character}]")

for element in range (9):
    print(f"[] [] []\n[] [] []\n[] [] []")
    break
element = input(f"Which place would you like to place {character}: ")




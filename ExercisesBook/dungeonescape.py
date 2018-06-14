from random import randint, sample

game_map = []

for i in range(16):
    game_map.append("-")

player_position, key_position, gate_position = sample(range(16), 3)

game_map[player_position] ="P"
game_map[key_position] = "K"
game_map[gate_position] = "E"

for i in range(len(game_map)):
    print(game_map[i], end=' ')
    if (i % 4 == 3):
        print("\n")
    
playing= True
got_key = False
while playing:
    move = input("Your move? ")
    if move == "D":
        if player_position % 4 == 3:
            print("Invalid move!!")
        elif game_map[player_position+1] == "-":
            game_map[player_position] = "-"
            game_map[player_position+1] = "P"
            player_position += 1
            for i in range(len(game_map)):
                print(game_map[i], end=' ')
                if (i % 4 == 3):
                    print("\n")
        elif game_map[player_position+1] == "K":
            got_key = True
            print("You have just pick a key")
            game_map[player_position] = "-"
            game_map[player_position+1] = "P"
            player_position += 1
            for i in range(len(game_map)):
                print(game_map[i], end=' ')
                if (i % 4 == 3):
                    print("\n")
        elif game_map[player_position+1] == "E":
            if got_key == False:
                for i in range(len(game_map)):
                    print(game_map[i], end=' ')
                    if (i % 4 == 3):
                        print("\n")
                print("You can not exit, please acquire the key first")
            else:
                game_map[player_position] = "-"
                game_map[player_position+1] = "P"
                player_position += 1
                for i in range(len(game_map)):
                    print(game_map[i], end=' ')
                    if (i % 4 == 3):
                        print("\n")
                print("Congrats, you have just escaped the dungeon!")
                playing = False

    elif move == "A":
        if player_position % 4 == 0:
            print("Invalid move!!")
        elif game_map[player_position-1] == "-":
            game_map[player_position] = "-"
            game_map[player_position-1] = "P"
            player_position -= 1
            for i in range(len(game_map)):
                print(game_map[i], end=' ')
                if (i % 4 == 3):
                    print("\n")
        elif game_map[player_position-1] == "K":
            got_key = True
            game_map[player_position] = "-"
            game_map[player_position-1] = "P"
            player_position -= 1
            for i in range(len(game_map)):
                print(game_map[i], end=' ')
                if (i % 4 == 3):
                    print("\n")
            print("You have just pick a key")
        elif game_map[player_position-1] == "E":
            if got_key == False:
                for i in range(len(game_map)):
                    print(game_map[i], end=' ')
                    if (i % 4 == 3):
                        print("\n")
                print("You can not exit, please acquire the key first")
            else:
                game_map[player_position] = "-"
                game_map[player_position-1] = "P"
                player_position -= 1
                for i in range(len(game_map)):
                    print(game_map[i], end=' ')
                    if (i % 4 == 3):
                        print("\n")
                print("Congrats, you have just escaped the dungeon!")
                playing = False

    elif move == "W":
        if 0 <= player_position <= 3:
            print("Invalid move!!")
        elif game_map[player_position-4] == "-":
            game_map[player_position] = "-"
            game_map[player_position-4] = "P"
            player_position -= 4
            for i in range(len(game_map)):
                print(game_map[i], end=' ')
                if (i % 4 == 3):
                    print("\n")
        elif game_map[player_position-4] == "K":
            got_key = True
            game_map[player_position] = "-"
            game_map[player_position-4] = "P"
            player_position -= 4
            for i in range(len(game_map)):
                print(game_map[i], end=' ')
                if (i % 4 == 3):
                    print("\n")
            print("You have just pick a key")
        elif game_map[player_position-4] == "E":
            if got_key == False:
                for i in range(len(game_map)):
                    print(game_map[i], end=' ')
                    if (i % 4 == 3):
                        print("\n")
                print("You can not exit, please acquire the key first")
            else:
                game_map[player_position] = "-"
                game_map[player_position-4] = "P"
                player_position -= 4
                for i in range(len(game_map)):
                    print(game_map[i], end=' ')
                    if (i % 4 == 3):
                        print("\n")
                print("Congrats, you have just escaped the dungeon!")
                playing = False
    elif move == "S":
        if 12 <= player_position <= 15:
            print("Invalid move!!")
        elif game_map[player_position+4] == "-":
            game_map[player_position] = "-"
            game_map[player_position+4] = "P"
            player_position += 4
            for i in range(len(game_map)):
                print(game_map[i], end=' ')
                if (i % 4 == 3):
                    print("\n")
        elif game_map[player_position+4] == "K":
            got_key = True
            game_map[player_position] = "-"
            game_map[player_position+4] = "P"
            player_position += 4
            for i in range(len(game_map)):
                print(game_map[i], end=' ')
                if (i % 4 == 3):
                    print("\n")
            print("You have just pick a key")
        elif game_map[player_position+4] == "E":
            if got_key == False:
                for i in range(len(game_map)):
                    print(game_map[i], end=' ')
                    if (i % 4 == 3):
                        print("\n")
                print("You can not exit, please acquire the key first")
            else:
                game_map[player_position] = "-"
                game_map[player_position+4] = "P"
                player_position += 4
                for i in range(len(game_map)):
                    print(game_map[i], end=' ')
                    if (i % 4 == 3):
                        print("\n")
                print("Congrats, you have just escaped the dungeon!")
                playing = False
    else:
        print("Invalid move!!!")

    








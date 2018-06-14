map_sokoban = {
    "size_x" : 5,
    "size_y" : 5
}
player = {
    "x" : 4,
    "y" : 0
}

boxes = [
    {"x": 1, "y" : 1},
    {"x": 2, "y" : 2},
    {"x": 3, "y" : 3},
]
destinations = [
    {"x": 2, "y" : 1},
    {"x": 3, "y" : 2},
    {"x": 4, "y" : 3},
]

playing = True
while playing:
    for y in range(map_sokoban["size_y"]):
        for x in range(map_sokoban["size_x"]):

            box_is_here = False
            for box in boxes:
                if box["x"] == x and box["y"] == y:
                    box_is_here = True

            destination_is_here = False
            for destination in destinations:
                if destination['x'] == x and destination['y'] == y:
                    destination_is_here = True


            player_is_here = False
            if x == player["x"] and y == player["y"]:
                player_is_here = True


            if player_is_here:
                print("P ",end='')
            elif box_is_here:
                print("B ",end='')
            elif destination_is_here:
                print("D ",end='')
            else:
                print("- ",end='')
                    
        print()
    ### Check win

    win = True 
    for box in boxes:
        if box not in destinations:
            win = False
    if win:
        print("You win")
        break

        #### end of print map

    move = input("Your move: ").upper()

    dx = 0
    dy = 0

    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    else:
        playing = False


    if 0 <= player['x'] + dx < map_sokoban['size_x'] \
       and 0 <= player['y'] + dy < map_sokoban['size_y']:
       player['x'] += dx
       player['y'] += dy

    for box in boxes:
        if box['x'] == player['x'] and box['y'] == player['y']:
            consecutive_boxes = False
            if {'x' : box['x'] + dx, 'y' : box['y'] + dy} in boxes:
                consecutive_boxes = True  
            
            if consecutive_boxes:
                player['x'] -= dx
                player['y'] -= dy
            elif 0 <= box['x'] + dx < map_sokoban['size_x'] and 0 <= box['y'] + dy < map_sokoban['size_y']: 
                box['x'] += dx
                box['y'] += dy
            else:
                player['x'] -= dx
                player['y'] -= dy
            










        # elif box_is_here is False:
            #     # is_box = False
            #     # for v in range(len(boxes)):
            #     #      if x == boxes[v]["x"] and y == boxes[v]["y"]:
            #     #         print("B ",end='')
            #     #         is_box = True 
            #     # if is_box == False:
            #     print("- ",end='')

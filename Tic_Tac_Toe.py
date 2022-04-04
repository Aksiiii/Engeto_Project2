from textwrap import dedent


def ttt_map():
    border_line = "+---+---+---+"
    play_line = "| "

    for seq in game_data:
        print(border_line)
        for i in seq:
            if i == 1:
                play_line += "X"
            elif i == 2:
                play_line += "O"
            else:
                play_line += "-"
            play_line += " | "
        else:
            print(play_line)
            play_line = "| "
    else:
        print(border_line)
    return 0


def translator(choice):
    # translates user input from 1-9 to corresponding index in game_data
    result = [
        [2, 0],
        [2, 1],
        [2, 2],
        [1, 0],
        [1, 1],
        [1, 2],
        [0, 0],
        [0, 1],
        [0, 2],
    ]
    return result[choice - 1]


def win_con(grid):
    # diagonal
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:
        return False
    elif grid[2][0] == grid[1][1] == grid[0][2] != 0:
        return False
    # horizontal
    for seq in grid:
        if seq.count(1) == 3 or seq.count(2) == 3:
            return False
    # vertical
    if grid[0][0] == grid[1][0] == grid[2][0] != 0:
        return False
    elif grid[0][1] == grid[1][1] == grid[2][1] != 0:
        return False
    elif grid[0][2] == grid[1][2] == grid[2][2] != 0:
        return False
    return True


def verify(choice):
    if choice.isnumeric() and int(choice) in range(1, 10):
        choice = int(choice)
        if not game_data[translator(choice)[0]][translator(choice)[1]] != 0:
            return True
        else:
            print(SEP_ONE,
                  "The Chosen space is already occupied",
                  "Please pick a different space",
                  sep="\n")
            return False
    else:
        print(SEP_ONE,
              "You must pick a number between 1 - 9, please try again",
              sep="\n")
        return False


def player(t):
    result = int(t) + 1
    return result


turn = True
max_turn = 9
SEP_ONE = "--------------------------------------------"
SEP_TWO = "============================================"
game_data = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

print(dedent(f"""\
    Welcome to Tic Tac Toe"
    {SEP_TWO}
    GAME RULES:
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their
    marks in a:
    * horizontal
    * vertical or
    * diagonal row
    {SEP_ONE}
    USE NUMPAD FOR ORIENTATION
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    {SEP_ONE}"""))
input("Press ENTER to continue ")
print(SEP_TWO,
      "Let's start the game", sep="\n")

# main game loop that doesnt end until win_con returns False
# or max_turn reaches 0
while win_con(game_data) and max_turn > 0:
    print(SEP_ONE)
    trigger = ttt_map()
    print(SEP_TWO)

    max_turn -= 1
    turn = not turn

    while True:
        cell = input(f"Player {player(turn)} |"
                     f" Please enter your move number: ")
        if verify(cell):
            cell = int(cell)
            break
    # Updates game data using user put trough translator function
    game_data[translator(cell)[0]][translator(cell)[1]] += player(turn)

else:
    print(SEP_ONE)
    trigger = ttt_map()
    print(SEP_TWO)

    if not win_con(game_data):
        print(f"Congratulations, Player {player(turn)} Wins!")
    else:
        print("It's a Draw!")
    print(SEP_TWO)

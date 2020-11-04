def startup(game_state):
    permitted_chars = ["X", "O", "_"]
    for char in game_state:
        if char not in permitted_chars:
            print("Enter valid character")
    return game_state


def print_table(game_state):
    i, ii, iii = game_state[:3], game_state[3:6], game_state[6:]
    print("---------")
    print(f"| {i[0]} {i[1]} {i[2]} |")
    print(f"| {ii[0]} {ii[1]} {ii[2]} |")
    print(f"| {iii[0]} {iii[1]} {iii[2]} |")
    print("---------")


def player_move(game_state):
    coord = [int(move) for move in input('Enter the coordinates: ').split(' ')]
    field = [i for i in game_state]
    new_field = []

    return


def check_for_win(game_state):
    winning_states = [(0, 9, 4), (2, 7, 2), (0, 7, 3), (1, 8, 3), (2, 9, 3),
                      (0, 3), (3, 6), (6, 9)]
    x_wins = False
    o_wins = False
    for ind in winning_states:
        test_slice = slice(*ind)
        if "XXX" == game_state[test_slice]:
            x_wins = True
        if "OOO" == game_state[test_slice]:
            o_wins = True
    if abs(game_state.count("X") - game_state.count("O")) >= 2:
        print("Impossible")
    elif not x_wins and not o_wins and "_" in game_state:
        print("Game not finished")
    elif x_wins and o_wins:
        print("Impossible")
    elif x_wins:
        print("X wins")
    elif o_wins:
        print("O wins")
    else:
        print("Draw")


# while True:
def main():
    game_state = startup(input("Enter cells: "))
    print_table(game_state)
    player_move(game_state)
    # check_for_win(game_state)


main()

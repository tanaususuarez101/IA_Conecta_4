
infinity = 1.0e400


def opponent(player):
    return 'X' if player == 'O' else 'O'


def h0(state, player):

    if state.utility != 0:
        if player == 'X':
            return state.utility * infinity
        else:
            return -state.utility * infinity

    f1, f2 = 0, 0

    for move in legal_moves(state):
        for displacement in [(0, 1), (1, 0), (1, -1), (1, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]:

            f1 += heuristic_function(state, move, displacement, player)
            f2 += heuristic_function(state, move, displacement, opponent(player))

    return f1-f2


def heuristic_function(state, move, displacement, player):
    h_temp = 0

    x, y = move
    x_displ, y_displ = displacement
    adversary = opponent(player)

    for count in range(3):
        x, y = x + x_displ, y + y_displ
        if x > 7 or x <= 0 or y > 6 or y <= 0:
            break

        if state.board.get(x, y) == adversary:
            return -50

        if state.board.get((x, y)) == player:
            h_temp += 100
        else:
            h_temp += 50

    return h_temp


def legal_moves(state):
    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y-1) in state.board]

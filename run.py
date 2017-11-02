# CODING = UTF-8

import os
import games
import heuristic


d_glb = 4
player_glb = 'X'


def get_difficulty():
    return d_glb


def get_player():
    return player_glb


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def start_game(d, player):

    game = games.ConnectFour(player=player)
    state = game.initial

    while True:
        clear()
        print "Difficulty level:", d if d == 1 else d/2
        if game.to_move(state) == 'X':
            print "Player to move: CPU"
        else:
            print "Player to move: Human"

        game.display(state)

        if player == 'O':
            col_str = raw_input("\n--> Movement: ")

            while int(col_str) < 1 or int(col_str) > 7:
                col_str = raw_input("--> Movement: ")

            coor = int(str(col_str).strip())
            x = coor
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]

            state = game.make_move((x, y), state)
            player = 'X'
        else:
            print "\nThinking..."

            move = games.alphabeta_search(state, game, d, eval_fn=heuristic.h0)

            state = game.make_move(move, state)
            player = 'O'
        print "-------------"
        if game.terminal_test(state):
            clear()
            game.display(state)
            print "\nEND OF THE GAME. Press any key to back main menu."
            raw_input()
            break


def set_difficulty():
    clear()

    print ".: Settings: difficulty level :.\n"
    print " 1) Amateur\n 2) Intermediate\n 3) Professional\n "

    option = int(raw_input("--> Select difficulty level: "))

    while option < 1 or option > 3:
        option = int(raw_input("--> Entry a correct option please: "))

    global d_glb
    if option == 1:
        d_glb = 1
    else:
        d_glb = option*2


def set_initial_player():
    clear()

    print ".: Initial player :.\n"
    print " 1) Human\n 2) CPU\n"

    option = int(raw_input("--> Select initial player: "))

    while option != 1 and option != 2:
        option = int(raw_input("--> Entry a correct option please: "))

    global player_glb
    if option == 1:
        player_glb = 'O'
    else:
        player_glb = 'X'

    start_game(get_difficulty(), get_player())


def main_menu():
    while True:
        clear()

        print "#####################################"
        print "## CONECTA-4: Crushing the machine ##"
        print "#####################################\n"

        print "1) Start game."
        print "2) Set difficulty."
        print "3) Exit.\n"

        option = int(raw_input("--> "))

        while option < 1 or option > 3:
            option = int(raw_input("--> "))

        if option == 3:
            break

        if option == 1:
            set_initial_player()
        else:
            set_difficulty()


main_menu()

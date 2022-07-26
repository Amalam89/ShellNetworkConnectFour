# connectfour_console.py
#
# ICS 32 Winter 2020
# Project #2: Send Me On My Way
# Ali Malam


import connectfour

import connectfour_functions


def play_game()-> None:
    """
    Function which is called when console is main. The function handles all the
    Gameplay of a two player game of connect four.
    """

    current_game = connectfour.new_game()
    
    while(True):

        connectfour_functions.display_board(current_game.board)
        print()
        print()
        player_move = connectfour_functions.user_prompt(current_game.turn)   
        try:
            current_game, a = connectfour_functions.receive_move(current_game, current_game.turn, player_move)
        except:            
            continue
        
        if connectfour.winner(current_game) == connectfour.RED:
            print("WINNER_RED")
            break
        elif connectfour.winner(current_game) == connectfour.YELLOW:
            print("WINNER_YELLOW")
            break


if __name__ == '__main__':

    play_game()

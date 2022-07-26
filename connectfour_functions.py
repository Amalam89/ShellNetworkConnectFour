# connectfour_functions.py
#
# ICS 32 Winter 2020
# Project #2: Send Me On My Way
# Ali Malam



import connectfour

def display_board(board: [[int]]) -> None:
    '''
    Displays the state of the board throughout gameplay
    '''

    for num in range(1, connectfour.BOARD_COLUMNS + 1):
        print(num, end=" ")
        
    for row in range(connectfour.BOARD_ROWS):
        print()

        for col in range(connectfour.BOARD_COLUMNS):

            if board[col][row] == connectfour.RED:
                print("R",  end=" ")
            elif board[col][row] == connectfour.YELLOW:
                print("Y", end=" ")
            else:
                print(".", end=" ")



def user_prompt(turn: int) -> str:
    '''
    Gives players prompts to make moves throughout gameplay. When move is selected, the respective
    move is applied to the gameplay
    '''
    player_move = input("Player {},\nEnter Drop if you would like to drop a piece in a column\n"
                        "Enter Pop if you would like to pop a piece from the bottom of a column\n"
                        "Follow the command with the number of column you would like to Drop or Pop\n"
                        "Example... DROP 5\n\n".format(turn))
        
    return player_move
        

def receive_move(game_state: 'GameState', turn: int, player_move: str):
    '''
    '''

    while(True):

        move_in_string = player_move        

        temporary_list = player_move.split()
        
        if len(temporary_list) != 2:
            print("That is not a valid Entry\n")
            
            break

        player_move, num = temporary_list

        try:

            num = int(num)

        except ValueError:
            print("That is not a valid Entry\n")
            break

        if (player_move != "DROP") and (player_move != "POP"):
            print("That is not a valid Entry\n")
            break

        elif (num < 1) or (num > connectfour.BOARD_COLUMNS):
            print("That is not a valid column entry\n")
            break

        else:

            if player_move == "DROP":

                try:
                    game_change = connectfour.drop(game_state, (num-1))

                    return game_change, move_in_string

                except connectfour.InvalidMoveError:

                    print("That is not a valid Entry\n")
                    break

            else:

                try:
                    game_change = connectfour.pop(game_state, (num - 1))

                    return game_change, move_in_string

                except connectfour.InvalidMoveError:

                    print("That is not a valid Entry\n")
                    break













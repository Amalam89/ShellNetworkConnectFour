#connectfour_network.py
#
# ICS 32 Winter 2020
# Project #2: Send Me On My Way
# Ali Malam



import cn_socket
import connectfour
import connectfour_functions


def _run_user_interface() -> None:
    '''
    Runs the Network user interface from start to finish.
    '''
    
    host = read_host()
    port = read_port()
    connection = cn_socket.connect(host, port)

    try:
        while True:
            
            username = _ask_for_username()

            cn_socket.initial_connect(connection, username)
            
            break

        
        while _handle_command(connection):
            
            pass

    finally:
        
        cn_socket.close(connection)

def read_host() -> str:
    '''
    Asks the user to specify what host they'd like to connect to,
    continuing to ask until a valid answer is given.  An answer is
    considered valid when it consists of something other than just
    spaces.
    '''

    while True:
        host = input('Host: ').strip()

        if host == '':
            print('Please specify a host: ')
        else:
            return host



def read_port() -> int:
    '''
    Asks the user to specify what port they'd like to connect to,
    continuing to ask until a valid answer is given.  A port must be an
    integer between 0 and 65535.
    '''

    while True:
        try:
            port = int(input('Port: ').strip())

            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port

        except ValueError:
            print('Ports must be an integer between 0 and 65535')


def _handle_command(connection: cn_socket.GameConnection) -> bool:
    '''
    After initial connection, this function handles the rest of
    game play between user and server.
    '''

    current_game = connectfour.new_game()    

    while(True):

        connectfour_functions.display_board(current_game.board)        

        print()
        print()

        if current_game.turn == 1:
            move = connectfour_functions.user_prompt(current_game.turn)
            try:
                current_game, a = connectfour_functions.receive_move(current_game, current_game.turn, move)
            except:            
                continue

            ai_move = cn_socket.send_move(connection, move)

            if ai_move == 'WINNER_RED':
                print('WINNER_RED')
                return False
        
            elif ai_move == 'WINNER_YELLOW':                       
                print('WINNER_YELLOW')
                return False
            
        elif current_game.turn == 2:
            
            current_game, move = connectfour_functions.receive_move(current_game, current_game.turn, ai_move)           
        

def _ask_for_username() -> str:
    '''
    Asks the user to enter a username and returns it as a string.  Continues
    asking repeatedly until the user enters a username that is non-empty, as
    the Polling server requires.
    '''
    while True:
        username = input('Username: ').strip()

        if len(username) > 0 and ' ' not in username:
            return username
        else:
            print('That is not a valid username; please try again')


if __name__ == '__main__':
    _run_user_interface()

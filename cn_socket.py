# cn_socket.py
#
# ICS 32 Winter 2020
# Project #2: Send Me On My Way
# Ali Malam


from collections import namedtuple
import socket
import sys


GameConnection = namedtuple('GameConnection',['socket', 'input', 'output'])

PLAY = 0

_SHOW_DEBUG_TRACE = False

def game_protocol_error()-> None:
    '''
    Ends game in case of incorrect input for protocol.
    '''
    print('UNEXPECTED INPUT!')    
    sys.exit()

def connect(host: str, port: int) -> GameConnection:
    '''
    Connects to a I32CFSP server running on the given host and listening
    on the given port, returning a GameConnection object describing
    that connection if successful, or raising an exception if the attempt
    to connect fails.
    '''

    connect_socket = socket.socket()
    
    connect_socket.connect((host, port))

    connect_input = connect_socket.makefile('r')
    connect_output = connect_socket.makefile('w')

    return GameConnection(
        socket = connect_socket,
        input = connect_input,
        output = connect_output)



def initial_connect(connection: GameConnection, username: str) -> PLAY:
    '''
    Runs and verifies the initial I32CFSP connection protocol between client
    and server. If the server sends back a response that does not conform to
    the Polling protocol, an exception is raised.
    '''
    
    _write_line(connection, 'I32CFSP_HELLO ' + username)

    response = _read_line(connection)    

    if response == 'WELCOME '+ username:

        _write_line(connection, 'AI_GAME')

        response = _read_line(connection)        

        if response == 'READY':

            return PLAY

    else:

        raise game_protocol_error()


def send_move(connection: GameConnection, player_input: str) -> str:
    '''
    Sends a valid move from the player to server, expecting a valid response
    with either a move or declaration of a winner. Raises exception
    and closes connection with server if unexpected response is received.
    '''
    _write_line(connection, player_input)
      
    response = _read_line(connection)
    
    if response == 'WINNER_RED':

        return response

    elif response == 'OKAY':        

        ai_move = _read_line(connection)

        response = _read_line(connection)

        if response == 'WINNER_YELLOW':

            return response
        
        elif response == 'READY':
            
            return ai_move

        else:

            raise game_protocol_error()
            
    else:
        
        raise game_protocol_error()    
    


def close(connection: GameConnection) -> None:
    'Closes the connection to the I32CFSP server'    
    connection.input.close()
    connection.output.close()
    connection.socket.close()



def _read_line(connection: GameConnection) -> str:
    '''
    Reads a line of text sent from the server and returns it without
    a newline on the end of it
    '''
   
    line = connection.input.readline()[:-1]

    if _SHOW_DEBUG_TRACE:
        print('RCVD: ' + line)

    return line



def _write_line(connection: GameConnection, line: str) -> None:
    '''
    Writes a line of text to the server, including the appropriate
    newline sequence, and ensures that it is sent immediately.
    '''
    connection.output.write(line + '\r\n')
    connection.output.flush()

    if _SHOW_DEBUG_TRACE:
        print('SENT: ' + line)

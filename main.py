import os
import chess

# Sets up initial variables
game_started = False
game_board = None


# Generates a board based of the FEN or a new game.
def setup_game():
    global game_started
    while True:
        menu1 = str(input("Enter starting FEN\nType 'None' to use a starting board\n>"))
        menu1.lower()

        # Asks for FEN. If none given, generates starting board.
        if menu1 == "none":
            game_board_f = chess.Board()
            if game_board_f.is_valid():
                break
            else:
                print("Game board not valid.")
        else:
            game_board_f = chess.Board(fen=menu1)
            if game_board_f.is_valid():
                break
            else:
                print("Gameboard not valid.")

    print("Game generated successfully!")
    game_started = True

    return game_board_f


# Writes a clear function to keep the screen clean and tidy :)
def clear():
    os.system("clear")


# Push pieces around the board until the user exits the "program"
def make_move(game_board_f):
    while True:
        print(game_board_f)
        # If there is an end of game outcome, print the result and exit the "program".
        if game_board_f.is_checkmate():
            print("Checkmate!")
            input()
            break
        elif game_board_f.is_stalemate():
            print("Stalemate!")
            input()
            break
        elif game_board_f.is_insufficient_material():
            print("Draw through insufficient material!")
            input()
            break
        elif game_board_f.is_seventyfive_moves():
            print("Draw through seventy five move rule!")
            input()
            break
        elif game_board_f.is_fivefold_repetition():
            print("Draw through fivefold repetition!")
            input()
            break

        if bool(game_board_f.turn):
            print("White to play.")
        else:
            print("Black to play.")
        # Allows the user to enter a move. Going to be changed to a proper console later.
        move = str(input(">"))
        if move == "close":
            print("Closing move program")
            break
        else:
            try:
                game_board_f.push_san(move)  # Makes the move, or returns a value error
            except ValueError:  # Adds exception for a value error
                print("Value Error! Check your move and try again.")
    clear()


# Main console function
def console():
    global game_board
    while True:
        console_menu = str(input(">"))
        console_menu.lower()
        # ----------------------------------------------------------------------------------------------------------------------
        if console_menu == "move":
            make_move(game_board)
        elif console_menu == "board":
            print(game_board)
        elif console_menu == "clear":
            clear()
        elif console_menu == "newgame":
            game_board = setup_game()
        elif console_menu == "help":
            print("""            newgame - Generates a new game with the default setup or a generated FEN
            move - Makes a move in the game
            board - Displays the active board
            clear - Clears the terminal
            shutdown - Closes the program
            help - Displays all available commands
            """)
        elif console_menu == "shutdown":
            quit()
        elif console_menu == "hello":
            print("Hi!")
        else:
            print("Command not recognised, please try again.")


def main():
    console()


main()

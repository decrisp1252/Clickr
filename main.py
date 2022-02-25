import os
import chess
import chess.svg

# Sets up initial variables
game_started = False
game_board = None
chess_svg = False


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
                print("Game-board not valid.")
    if chess_svg:
        game_board_svg = chess.svg.board(game_board_f)
        svg = open("board.svg", "w")
        svg.write(game_board_svg)
        svg.close()

    print("Game generated successfully!")
    game_started = True

    return game_board_f


# Writes a clear function to keep the screen clean and tidy :)
def clear():
    os.system("clear")


# Push pieces around the board until the user exits the "program"
def make_move(game_board_f):
    if chess_svg:
        svg = open("board.svg", "w")
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
            if chess_svg:
                svg.close()
            break
        else:
            try:
                game_board_f.push_san(move)  # Makes the move, or returns a value
                if chess_svg:
                    game_board_svg = chess.svg.board(game_board_f)
                    svg.write(game_board_svg)
            except ValueError:  # Adds exception for a value error
                print("Value Error! Check your move and try again.")
    clear()


def svg_mode(game_board_f, chess_svg_f):
    if not chess_svg_f:
        if game_started:
            game_board_svg = chess.svg.board(game_board_f)
            svg = open("board.svg", "w")
            svg.write(game_board_svg)
            svg.close()
            print("Game found, board generated.")

        chess_svg_f = True
        print("SVG mode activated")
    else:
        chess_svg_f = False
        print("SVG mode deactivated")
    return chess_svg_f


def shutdown():
    os.remove("board.svg")
    quit()

# Main console function
def console():
    global game_board, chess_svg
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
        elif console_menu == "svg":
            svg_mode(game_board, chess_svg)
        elif console_menu == "help":
            print("""newgame - Generates a new game with the default setup or a generated FEN
move - Makes a move in the game
board - Displays the active board
svg - activates svg mode
clear - Clears the terminal
shutdown - Closes the program
help - Displays all available commands
""")
        elif console_menu == "shutdown":
            shutdown()
        elif console_menu == "hello":
            print("Hi!")
        else:
            print("Command not recognised, please try again.")


def main():
    console()


main()

from blessed import Terminal

from library import Board

term = Terminal()
board = Board()

with term.fullscreen(), term.cbreak(), term.hidden_cursor():
    board.draw_board(term)

    while (val := term.inkey()) != "q":
        if val in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            continue

#!/usr/bin/env python

import sys

from board import Board, BoardView
from utils import clear, getch


def main():
    board = Board(19, 19)
    view = BoardView(board)
    err = None

    def move():
        board.move(*view.cursor)
        view.redraw()

    def exit():
        sys.exit(0)

    KEYS = {
        'w': view.cursor_up,
        'r': view.cursor_down,
        'a': view.cursor_left,
        's': view.cursor_right,
        'x': move,
        '\x1b': exit,
    }

    while True:
        # Print board
        clear()
        sys.stdout.write('{0}\n'.format(view))
        sys.stdout.write('Black: {black} <===> White: {white}\n'.format(**board.score))
        sys.stdout.write('{0}\'s move... '.format(board.turn))

        if err:
            sys.stdout.write(err + '\n')
            err = None

        # Get action
        c = getch()

        try:
            # Execute selected action
            KEYS[c]()
        except Board.BoardError as be:
            # Board error (move on top of other piece, suicidal move, etc.)
            err = be.message
        except KeyError:
            # Action not found, do nothing
            pass


if __name__ == '__main__':
    main()
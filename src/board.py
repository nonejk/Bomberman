""" this module contains the board functions and elements
"""

from __future__ import print_function
from elements import *


class Board():
    """ this is the board class
    """

    rows = 42
    columns = 92
    board = [[elements() for x in range(92)] for y in range(42)]
    bmbr = (2, 4)
    enem = []
    bmb = ()
    brks = []
    enm_cnt = 0
    bmb_cnt = 0
    expl = []

    def __init__(self):
        pass

    def disp(self):
        """ displays the board on the screen
        """
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.board[i][j].symb, end='')
            print()

    def reset_brd(self):
        """ resets position of suggest to change it inton
        """
        for i in range(self.columns):
            self.board[0][i].def_element(1, 0, i)
            self.board[1][i].def_element(1, 1, i)
            self.board[self.rows - 1][i].def_element(1, (self.rows - 1), i)
            self.board[self.rows - 2][i].def_element(1, (self.rows - 2), i)
        for i in range(2, self.rows):
            self.board[i][0].def_element(1, i, 0)
            self.board[i][1].def_element(1, i, 1)
            self.board[i][2].def_element(1, i, 2)
            self.board[i][3].def_element(1, i, 3)
            self.board[i][88].def_element(1, i, 88)
            self.board[i][89].def_element(1, i, 89)
            self.board[i][90].def_element(1, i, 90)
            self.board[i][91].def_element(1, i, 91)
        for i in range(2, self.rows - 2, 2):
            for j in range(4, self.columns - 4, 4):
                if ((i / 2) % 2 == 1) or (((i / 2) % 2 == 0) and ((j / 4) % 2 == 1)):
                    self.board[i][j].def_element(0, i, j)
                    self.board[i + 1][j].def_element(0, i + 1, j)
                    self.board[i][j + 1].def_element(0, i, j + 1)
                    self.board[i + 1][j + 1].def_element(0, i + 1, j + 1)
                    self.board[i][j + 2].def_element(0, i, j + 2)
                    self.board[i + 1][j + 2].def_element(0, i + 1, j + 2)
                    self.board[i][j + 3].def_element(0, i, j + 3)
                    self.board[i + 1][j + 3].def_element(0, i + 1, j + 3)

                else:
                    self.board[i][j].def_element(1, i, j)
                    self.board[i + 1][j].def_element(1, i + 1, j)
                    self.board[i][j + 1].def_element(1, i, j + 1)
                    self.board[i + 1][j + 1].def_element(1, i + 1, j + 1)
                    self.board[i][j + 2].def_element(1, i, j + 2)
                    self.board[i + 1][j + 2].def_element(1, i + 1, j + 2)
                    self.board[i][j + 3].def_element(1, i, j + 3)
                    self.board[i + 1][j + 3].def_element(1, i + 1, j + 3)

    def rt_elem(self, row, column):
        """ returns the right element type
        """
        return self.board[row][column + 4].tyype

    def lft_elem(self, row, column):
        """ returns the right element type
        """
        return self.board[row][column - 4].tyype

    def tp_elem(self, row, column):
        """ returns the right element type
        """
        return self.board[row - 2][column].tyype

    def btm_elem(self, row, column):
        """ returns the right element type
        """
        return self.board[row + 2][column].tyype

    def set_bmbr(self, row, column):
        """ returns the right element type
        """
        self.bmbr = (row, column)

    def bmb_pos(self):
        """returns postion of the planted bomb
        """
        return self.bmb

    def dfn_oct(self, typ, row, column):
        """ sets the type of all 8 blocks around it to be of a particular type
        """
        self.board[row + 0][column + 0].def_element(typ, row + 0, column + 0)
        self.board[row + 0][column + 1].def_element(typ, row + 0, column + 1)
        self.board[row + 0][column + 2].def_element(typ, row + 0, column + 2)
        self.board[row + 0][column + 3].def_element(typ, row + 0, column + 3)
        self.board[row + 1][column + 0].def_element(typ, row + 1, column + 0)
        self.board[row + 1][column + 1].def_element(typ, row + 1, column + 1)
        self.board[row + 1][column + 2].def_element(typ, row + 1, column + 2)
        self.board[row + 1][column + 3].def_element(typ, row + 1, column + 3)

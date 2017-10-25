""" has functions required to play the game such as move, explosion, etc
"""
from __future__ import print_function
import os
import random
from board import *


def clear():
    os.system('clear')


class gameplay(Board):
    """ contains all the functions. inherits the Board class
    """
    level = 1
    score = 0
    lvs_lft = 3

    def bmbr_mv_lft(self, row, column):
        """ checks for any enemy on right. If so, decreases lives, returns 0.
        """
        # if there is wall or brick, no movement
        elem = self.lft_elem(row, column)
        if not (elem == 1 or elem == 2):
            self.bmbr = (row, column - 4)
            flag = 0
            for i in range(len(self.enem)):
                if(self.bmbr == self.enem[i]):
                    flag = 1
                    break
            if flag:
                self.lvs_lft -= 1
                self.rst_bmbr()
                self.dfn_oct(0, row, column)
                return 0
            self.dfn_oct(5, row, column - 4)
            self.dfn_oct(0, row, column)
            return 1
        return 1

    def bmbr_mv_rt(self, row, column):
        """ checks for any enemy on left. If so, decreases lives, returns 0.
        """
        # if there is wall or brick, no movement
        elem = self.rt_elem(row, column)
        if elem == 1 or elem == 2:
            return 1
        if not (elem == 1 or elem == 2):
            self.bmbr = (row, column + 4)
            flag = 0
            for i in range(len(self.enem)):
                if self.bmbr == self.enem[i]:
                    flag = 1
                    break
            if flag:
                self.lvs_lft -= 1
                self.rst_bmbr()
                self.dfn_oct(0, row, column)
                return 0
            self.dfn_oct(5, row, column + 4)
            self.dfn_oct(0, row, column)
            return 1

    def bmbr_mv_up(self, row, column):
        """ checks for any enemy on up. If so, decreases lives, returns 0.
        """
        # if there is wall or brick, no movement
        elem = self.tp_elem(row, column)
        if not (elem == 1 or elem == 2):
            self.bmbr = (row - 2, column)
            flag = 0
            for i in range(len(self.enem)):
                if self.bmbr == self.enem[i]:
                    flag = 1
                    break
            if flag:
                self.lvs_lft -= 1
                self.rst_bmbr()
                self.dfn_oct(0, row, column)
                return 0
            self.dfn_oct(5, row - 2, column)
            self.dfn_oct(0, row, column)
            return 1
        return 1

    def bmbr_mv_dwn(self, row, column):
        """ checks for any enemy on bottom. If so, decreases lives, returns 0.
        """
        # if there is wall or brick, no movement
        l = self.btm_elem(row, column)
        if not (l == 1 or l == 2):
            self.bmbr = (row + 2, column)
            flag = 0
            for i in range(len(self.enem)):
                if self.bmbr == self.enem[i]:
                    flag = 1
                    break
            if flag:
                self.lvs_lft -= 1
                self.rst_bmbr()
                self.dfn_oct(0, row, column)
                return 0
            self.dfn_oct(5, row + 2, column)
            self.dfn_oct(0, row, column)
            return 1
        return 1

    def explosion(self):
        """ explooooosiooooon
        """
        row = self.bmb[0]
        column = self.bmb[1]
        right = self.rt_elem(row, column)
        left = self.lft_elem(row, column)
        above = self.tp_elem(row, column)
        down = self.btm_elem(row, column)

        self.dfn_oct(4, row, column)

        if right == 0 or right == 2 or right == 3 or right == 5:
            self.dfn_oct(4, row, column + 4)
        if left == 0 or left == 2 or left == 3 or left == 5:
            self.dfn_oct(4, row, column - 4)
        if above == 0 or above == 2 or above == 3 or above == 5:
            self.dfn_oct(4, row - 2, column)
        if down == 0 or down == 2 or down == 3 or down == 5:
            self.dfn_oct(4, row + 2, column)

    def bfr_expl_scr_updt(self):
        """ score updation function
        """
        row = self.bmb[0]
        column = self.bmb[1]
        right = self.rt_elem(row, column)
        left = self.lft_elem(row, column)
        above = self.tp_elem(row, column)
        down = self.btm_elem(row, column)

        enemyDead = 0
        bricks = 0

        if left == 2 or right == 2 or above == 2 or down == 2:
            bricks += (int)(left == 2) + (int)(right == 2) + \
                (int)(above == 2) + (int)(down == 2)
        if left == 3 or right == 3 or above == 3 or down == 3:
            enemyDead += (int)(left == 3) + (int)(right == 3) + \
                (int)(above == 3) + (int)(down == 3)

        self.score += (bricks * 20 + enemyDead * 100)

    def chck_dth_n_updt_lvs(self):
        """ to check if the bomber is in 4 blocks around the bomb
        """
        row = self.bmb[0]
        column = self.bmb[1]
        # getting types of elements around the bomb
        right = self.rt_elem(row, column)
        left = self.lft_elem(row, column)
        above = self.tp_elem(row, column)
        down = self.btm_elem(row, column)
        # check if they are bomberman type
        if right == 5 or left == 5 or above == 5 or down == 5 or self.bmbr == self.bmb:
            self.lvs_lft -= 1
            return 1
        return self.chck_enm_tch_dth()

    def enem_upd_expl(self):
        """ remove the enemies who died in the blast
        """
        row = self.bmb[0]
        column = self.bmb[1]
        # getting types of elements around the bomb
        right = self.rt_elem(row, column)
        left = self.lft_elem(row, column)
        above = self.tp_elem(row, column)
        down = self.btm_elem(row, column)
        # to check they are enemy type
        if right == 3:
            self.enem.remove((row, column + 4))
            self.enm_cnt -= 1
        if left == 3:
            self.enem.remove((row, column - 4))
            self.enm_cnt -= 1
        if above == 3:
            self.enem.remove((row - 2, column))
            self.enm_cnt -= 1
        if down == 3:
            self.enem.remove((row + 2, column))
            self.enm_cnt -= 1

    def chck_enm_tch_dth(self):
        """ to check for bomberman's death by enemy touches
        """
        for i in range(len(self.enem)):
            if self.bmbr == self.enem[i]:
                self.lvs_lft -= 1
                return 1
        return 0

    def clr_expl(self):
        """ to clear the bomb explosion area of the elements '^'
        """
        row = self.bmb[0]
        column = self.bmb[1]
        # getting the type of elements around the centre of explosion
        right = self.rt_elem(row, column)
        left = self.lft_elem(row, column)
        above = self.tp_elem(row, column)
        down = self.btm_elem(row, column)
        # making bomb location blank
        self.dfn_oct(0, row, column)
        # to check if a destroyable elements was in radius, and if so, replace
        # it with blank space
        if right == 0 or right == 2 or right == 3 or right == 5 or right == 4:
            self.dfn_oct(0, row, column + 4)
        if left == 0 or left == 2 or left == 3 or left == 5 or left == 4:
            self.dfn_oct(0, row, column - 4)
        if above == 0 or above == 2 or above == 3 or above == 5 or above == 4:
            self.dfn_oct(0, row - 2, column)
        if down == 0 or down == 2 or down == 3 or down == 5 or down == 4:
            self.dfn_oct(0, row + 2, column)
        # reset bomb params
        self.bmb = ()
        self.bmb_cnt = 0

    def set_bmb(self, a, b):
        """ placing the bomb on the board
        """
        # check if a bomb is already on the board. If not, place it
        if(self.bmb == ()):
            self.bmb_cnt = 1
            self.bmb = (a, b)
            self.dfn_oct(6, a, b)
            return 1
        return 0

    def set_bmb_typ(self, t):
        """ with respect to time left for explosion, set to required type
        """
        a = self.bmb[0]
        b = self.bmb[1]
        self.dfn_oct(t, a, b)

    def set_brk(self):
        """ placing a brick on the map randomly
        """
        psr = random.randint(1, 19) * 2
        psc = random.randint(2, 20) * 4

        tipe = self.board[psr][psc].tyype

        while(tipe == 1 or tipe == 3):
            psr = random.randint(1, 19) * 2
            psc = random.randint(2, 20) * 4
            tipe = self.board[psr][psc].tyype

        self.brks.append((psr, psc))
        self.dfn_oct(2, psr, psc)

    def set_enem(self):
        """ position enemies randomly
        """
        psr = random.randint(1, 19) * 2
        psc = random.randint(2, 21) * 4
        tipe = self.board[psr][psc].element_type()

        while(tipe == 1):
            psr = random.randint(1, 19) * 2
            psc = random.randint(2, 21) * 4
            tipe = self.board[psr][psc].tyype

        self.enem.append((psr, psc))
        self.dfn_oct(3, psr, psc)
        self.enm_cnt += 1

    def rst_bmbr(self):
        """ resets bomber position
        """
        self.bmbr = (2, 4)
        self.dfn_oct(5, 2, 4)

    def rst_params(self):
        """resets all parameters
        """
        self.enem = []
        self.enm_cnt = 0
        self.bmb_cnt = 0
        self.brks = []
        self.bmb = ()

    def gm_ovr(self):
        """ prints required information when game gets over
        """
        clear()
        print("\t\t\t\t\tBOMBERMAN\n\t\t\t\t\tLEVEL", self.level)
        print(
            "\n\t\t\t\t\tGAME OVER\n\n\t\t\t\t     Final Score:",
            self.score, "\n\t\t\t\t\tLives left:", self.lvs_lft)
        self.disp()
        print("\n\t\t\t\t\t   END")
        self.rst_params()
        self.reset_brd()

    def enm_chk_tp(self, ind):
        """ check enemy's top position
        """
        row = self.enem[ind][0]
        column = self.enem[ind][1]
        above = self.tp_elem(row, column)
        if(above == 1 or above == 2 or above == 3):
            return 0
        return 1

    def enm_chk_lft(self, ind):
        """ check enemy's left
        """
        row = self.enem[ind][0]
        column = self.enem[ind][1]
        left = self.lft_elem(row, column)
        if(left == 1 or left == 2 or left == 3):
            return 0
        return 1

    def enm_chk_rt(self, ind):
        """ check enemy's right
        """
        row = self.enem[ind][0]
        column = self.enem[ind][1]
        right = self.rt_elem(row, column)
        if(right == 1 or right == 2 or right == 3):
            return 0
        return 1

    def enm_chk_btm(self, ind):
        """ check enemy's bottom
        """
        row = self.enem[ind][0]
        column = self.enem[ind][1]
        down = self.btm_elem(row, column)
        if(down == 1 or down == 2 or down == 3):
            return 0
        return 1

    def enm_mv(self, ind, a, b):
        """ move enemy to required position
        """
        row = self.enem[ind][0]
        column = self.enem[ind][1]
        self.dfn_oct(0, row, column)
        row += a
        column += b
        self.enem[ind] = (row, column)
        self.dfn_oct(3, row, column)

    def enm_move_itr(self):
        """ move all enemies to random location [changed with respect to the old function]
        """
        length = len(self.enem)
        for i in range(length):
            rn = random.randint(1, 4)
            if rn == 1:
                if self.enm_chk_tp(i):
                    self.enm_mv(i, -2, 0)
                elif self.enm_chk_lft(i):
                    self.enm_mv(i, 0, -4)
                elif self.enm_chk_rt(i):
                    self.enm_mv(i, 0, 4)
                elif self.enm_chk_btm(i):
                    self.enm_mv(i, 2, 0)

            if rn == 2:
                if self.enm_chk_lft(i):
                    self.enm_mv(i, 0, -4)
                elif self.enm_chk_rt(i):
                    self.enm_mv(i, 0, 4)
                elif self.enm_chk_btm(i):
                    self.enm_mv(i, 2, 0)
                elif self.enm_chk_tp(i):
                    self.enm_mv(i, -2, 0)

            if rn == 3:
                if self.enm_chk_rt(i):
                    self.enm_mv(i, 0, 4)
                elif self.enm_chk_btm(i):
                    self.enm_mv(i, 2, 0)
                elif self.enm_chk_tp(i):
                    self.enm_mv(i, -2, 0)
                elif self.enm_chk_lft(i):
                    self.enm_mv(i, 0, -4)

            if rn == 4:
                if self.enm_chk_btm(i):
                    self.enm_mv(i, 2, 0)
                elif self.enm_chk_tp(i):
                    self.enm_mv(i, -2, 0)
                elif self.enm_chk_lft(i):
                    self.enm_mv(i, 0, -4)
                elif self.enm_chk_rt(i):
                    self.enm_mv(i, 0, 4)

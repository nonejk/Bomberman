# this is the main file to run to play the game
from __future__ import print_function
import time
import math
# importing other required files
from getchara import *
from menu import *
from gameplay import *


def main():
    # displaying menu first
    inp = menu()
    game = gameplay()
    # """ if 'q' is entered in the beginnging at menu, stage -> exit from game"""
    if inp == -1:
        clear()
        print("\t\t\t\t\tBOMBERMAN")
        print("\n\n\t\t\t\t\tYou quit")
        print("\n\n\t\t\t\t\t   END")
        return 0

    # if 's' is pressed at menu, we go further

    # game running flag
    gm_flg = 1
    game.level = 1
    for counter in range(3):
        print("Starts in", 3-counter, "seconds...")
        time.sleep(1)
    # game starts here
    while gm_flg:
        max_enm = 2 * game.level
        # reset board and its parameters
        game.reset_brd()
        game.rst_params()
        # place enemies(number determined by current level) on board
        itrtr = 0
        while itrtr < max_enm:
            game.set_enem()
            itrtr += 1
        # place a random number of brick on board
        itrtr = 0
        while itrtr < max_enm:
            game.set_brk()
            itrtr += 1

        # placing bomber on board in the first position
        game.rst_bmbr()
        # initialising parameters and flags required
        lvl_flg = 1
        bmb_plcd_flg = 0
        time_1 = 0
        time_2 = 0
        death = 0
        expl_flg = 0
        ip_tm_flg = 1
        itrns = 0
        bitr = 0
        # start of each level
        while lvl_flg:
            clear()
            print("\t\t\t\t\tBOMBERMAN\n\t\t\t\t\tLEVEL", game.level)
            print(
                "\nScore:",
                game.score,
                "\t\t\t\t\t\t\t\t\tLives left:",
                game.lvs_lft)

            # to check for a death in prev iteration and print appropriate
            # message
            if game.lvs_lft == 0:
                print("\t\t\tYou have no more lives left!!")
                game.gm_ovr()
                gm_flg = 0
                break
            if death and expl_flg:
                print("You died...Game Resumes")
                game.clr_expl()
                expl_flg = 0
                bmb_plcd_flg = 0
                game.bmb = ()
                game.bmb_cnt = 0
                game.rst_bmbr()
                death = 0
            elif death:
                print("You died...Game Resumes")
                expl_flg = 0
                bmb_plcd_flg = 0
                game.bmb = ()
                game.bmb_cnt = 0
                game.rst_bmbr()
                death = 0
            else:
                print()

            # to tell player that bomb has been placed
            if bmb_plcd_flg:
                print("Bomb has been planted! Explodes in 3 seconds...")
            else:
                print()

            game.disp()

            # moving all the enemies on map
            game.enm_move_itr()

            # to clear the board of explosion elements, if there was one in
            # prev iteration
            if expl_flg:
                game.clr_expl()
                expl_flg = 0

            # storing bomber man's position on map at any iteration
            bmbr_r = game.bmbr[0]
            bmbr_c = game.bmbr[1]

            # get input action for next move
            time_2 = time.time()
            inp = ""
            inp = nonBlockingCharInput()()
            if (time.time() - time_2) < 1:
                ip_tm_flg = 1

            # mapping inputs with required action
            if inp == 'q':
                game.gm_ovr()
                lvl_flg = 0
                gm_flg = 0
                break
            elif inp == 'w':
                death = (int)(not game.bmbr_mv_up(bmbr_r, bmbr_c))
            elif inp == 's':
                death = (int)(not game.bmbr_mv_dwn(bmbr_r, bmbr_c))
            elif inp == 'a':
                death = (int)(not game.bmbr_mv_lft(bmbr_r, bmbr_c))
            elif inp == 'd':
                death = (int)(not game.bmbr_mv_rt(bmbr_r, bmbr_c))

            # checking for death by enemy touch
            #death = game.chck_enm_tch_dth()
            if death:
                game.dfn_oct(0, bmbr_r, bmbr_c)

                continue

            # place bomb
            if inp == 'b':
                if game.set_bmb(bmbr_r, bmbr_c):
                    time_1 = time.time()
                    bitr = itrns
                    bmb_plcd_flg = 1

            # if bomb is already there on board, do the following
            if bmb_plcd_flg:
                # prints 2222
                if (itrns - bitr) == 1:
                    bmb_r = game.bmb[0]
                    bmb_c = game.bmb[1]
                    game.set_bmb_typ(7)
                    game.dfn_oct(7, bmb_r, bmb_c)
                # prints 1111
                elif(itrns - bitr) == 2:
                    bmb_r = game.bmb[0]
                    bmb_c = game.bmb[1]
                    game.set_bmb_typ(8)
                    game.dfn_oct(8, bmb_r, bmb_c)
                # explodes the bombs
                elif (itrns - bitr) == 3:
                    game.bfr_expl_scr_updt()
                    death = game.chck_dth_n_updt_lvs()

                    if game.enem_upd_expl():
                        game.dfn_oct(0, bmbr_r, bmbr_c)
                    game.explosion()
                    expl_flg = 1
                    bitr = 0
                    if death:
                        # if bomber dies here, go to next iteration
                        continue

            if len(game.enem) == 0:
                clear()
                print("\t\t\t\t\tYou cleared level ", game.level, "!")
                print("\n\n\t\t\tThe next level will start in 5 seconds\n")
                time.sleep(5)
                game.level += 1

                lvl_flg = 0
            itrns += 1
            if ip_tm_flg:
                if bmb_plcd_flg:
                    time_1 = math.ceil(time.time() - time_1)
                time.sleep(0.5)


main()

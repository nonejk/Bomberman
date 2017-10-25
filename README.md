# Bomberman Game

The game is a basic terminal based version of the original BOMBERMAN game built in `python`, exclusively without using libraries like pygame , curses, tkinter (basically GUI based libraries), as a part of the SSAD course.

#### The controls are:
* w - UP
* a - LEFT
* d - RIGHT
* s - DOWN
* b - PLACE BOMB
* q - QUIT GAME

#### Symbols:
* X - wall
* % - bricks
* E - enemy
* B - Bomberman

#### How to play
* To play the game, execute the command `python play.py` which is in the src folder.
* Make sure that the terminal is in `full screen` mode before you start playing the game

#### Features:
* OOP concepts have been used extensively
* `100` points for Killing an enemy
* `20` points for Destroying a brick
* The game has infinite levels, where number of enemies doubles with increase in each level
* The bomb has a timer of `3 seconds`
* The bomberman always respawns at the top-left part of the board
* The Bomberman has 3 lives initially
* The `Bomberman dies` if he is around an `explosion` or `touches an enemy`
* The movement of enemies is completely random
* An `enemy dies` when it is in an `explosion`, ie in a radius of 1 block around the bomb when its timer goes to zero
* There can `only be one bomb at a time` on the board
* The `game ends` when the Bomberman `loses all 3 lives` or the `player quits` the game by pressing 'q'
* Comments have been provided in the sourcecode where ever necessary

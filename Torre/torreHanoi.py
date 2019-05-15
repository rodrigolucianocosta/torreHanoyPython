import sys
import os
import random
import time
import curses

# tela principal
screen = curses.initscr()
screen.notimeout(False)
screen.keypad(True)
screen.clear()
#screen.set_title('Torre de Hanoi')

#inicio das cores
curses.start_color()
curses.init_pair( 1, curses.COLOR_RED,curses.COLOR_WHITE)

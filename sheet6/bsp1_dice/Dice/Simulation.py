import curses
import time


def roll_the_dice():
    """Rolls one dice. Opens a clear terminal and prints a dice and delets it very quickly and then prints the next dice and so on. At the end it closes the window"""
    screen = curses.initscr()
    screen.addstr(0, 0, r"┌─────────┐")
    screen.addstr(1, 0, r"│  ●   ●  │")
    screen.addstr(2, 0, r"│  ●   ●  │")
    screen.addstr(3, 0, r"│  ●   ●  │")
    screen.addstr(4, 0, r"└─────────┘")

    screen.refresh()

    time.sleep(0.3)

    screen.addstr(0, 0, r"┌─────────┐")
    screen.addstr(1, 0, r"│  ●   ●  │")
    screen.addstr(2, 0, r"│    ●    │")
    screen.addstr(3, 0, r"│  ●   ●  │")
    screen.addstr(4, 0, r"└─────────┘")
    screen.refresh()

    time.sleep(0.2)

    screen.addstr(0, 0, r"┌─────────┐")
    screen.addstr(1, 0, r"│  ●   ●  │")
    screen.addstr(2, 0, r"│         │")
    screen.addstr(3, 0, r"│  ●   ●  │")
    screen.addstr(4, 0, r"└─────────┘")
    screen.refresh()

    time.sleep(1)
    curses.endwin()

import curses, time, smough_map

def quit():
    curses.endwin()
    sys.exit(0)

def newmap():
    pass

menu_options = { "c: Create New Map": newmap, "q: Exit Smough": quit }

def init():
    screen = curses.initscr()
    curses.noecho()
    screen.clear()
    indent = 3
    screen.addstr(1, 1, "Smough v0.1 (pre-alpha)")
    current_line = 3
    for key, value in menu_options.iteritems():
        screen.addstr(current_line, indent, key)
        current_line += 1
    screen.refresh()
    return screen
def cleanup():
    curses.endwin()

def main():
    screen = init()
    exit = False
    screen.keypad(True)
    while not exit:
        nextchar = screen.getch()
        if nextchar == ord('c') or nextchar == ord('C'):
            my_terrain = smough_map.Terrain()
            my_map = smough_map.Map(10, 10, my_terrain)
            screen.addstr(my_map.__str__())
        exit = nextchar == ord('q') or nextchar == ord('Q')
    
    cleanup()

if __name__ == "__main__":
    main()

import curses, time

def quit():
    curses.endwin()
    sys.exit(0)

def newmap():
    pass

menu_options = { "Create New Map": newmap, "Exit Smough": quit }

def main():
    screen = curses.initscr()
    curses.noecho()
    screen.clear()
    screen.border()
    indent = 3
    screen.addstr(1, 1, "Smough v0.1 (pre-alpha)")
    current_line = 3
    for key, value in menu_options.iteritems():
        screen.addstr(current_line, indent, key)
        current_line += 1
    screen.refresh()
    time.sleep(3)
    curses.endwin()

if __name__ == "__main__":
    main()

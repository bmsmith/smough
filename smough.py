import curses, time

def main():
    screen = curses.initscr()
    time.sleep(3);
    curses.endwin()

if __name__ == "__main__":
    main()

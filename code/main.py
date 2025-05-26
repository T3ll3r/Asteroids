from pygame import *
from constants import * 

def main():
    init()
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.fill((0, 0, 0))
        display.flip()
        for e in event.get():
            if e.type == QUIT:
                quit()
                return
        



if __name__ == "__main__":
    main()
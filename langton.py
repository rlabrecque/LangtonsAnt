import msvcrt
import os
import sys
from enum import Enum

class Direction(Enum):
    North = 0
    West = 1
    South = 2
    East = 3

class Color(Enum):
    White = 0
    Black = 1

class State:
    width = 100
    height = 80
    def __init__(self):
        self.arr = [[Color.White for x in range(self.height)] for x in range(self.width)]
        self.x = 50
        self.y = 40
        self.dir = Direction.North
        self.iteration = 0

    def run(self):
        self.iteration += 1

        if self.arr[self.x][self.y] == Color.White:  # White
            if self.dir == Direction.North:
                self.dir = Direction.West
            elif self.dir == Direction.West:
                self.dir = Direction.South
            elif self.dir == Direction.South:
                self.dir = Direction.East
            elif self.dir == Direction.East:
                self.dir = Direction.North

            self.arr[self.x][self.y] = Color.Black
        else:  # Black
            if self.dir == Direction.North:
                self.dir = Direction.East
            elif self.dir == Direction.East:
                self.dir = Direction.South
            elif self.dir == Direction.South:
                self.dir = Direction.West
            elif self.dir == Direction.West:
                self.dir = Direction.North

            self.arr[self.x][self.y] = Color.White

        if self.dir == Direction.North:
            self.y -= 1
        elif self.dir == Direction.West:
            self.x -= 1
        elif self.dir == Direction.South:
            self.y += 1
        elif self.dir == Direction.East:
            self.x += 1


    def output(self):
        os.system('cls')
        print("Iteration: " + str(self.iteration))
        for posy in range(self.height):
            for posx in range(self.width):
                if posx == self.x and posy == self.y:
                    if self.dir == Direction.North:
                        char = "^"
                    elif self.dir == Direction.West:
                        char = "<"
                    elif self.dir == Direction.South:
                        char = "v"
                    elif self.dir == Direction.East:
                        char = ">"
                    print(char, end="")
                elif self.arr[posx][posy] == Color.White:
                    print("░", end="")
                else:
                    print("█", end="")

            print()



def main():
    s = State()

    if len(sys.argv) == 2:
        runto = int(sys.argv[1])

        for i in range(runto):
            s.run()

    s.output()

    while True:
        if wait():
            print("Quitting!")
            break
        
        s.run()
        s.output()

def wait():
    ch = msvcrt.getch()
    if ch == b'\x1b':  # ESC
        return True
    return False

if __name__ == "__main__":
    main()

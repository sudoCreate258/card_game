#!/usr/bin/python3
from objects import Player, Game

def main():
    p1 = Player("p1")       # TODO create player
    g1 = Game_21(p1)        # TODO create game
    g1.start()              # TODO start game

if __name__ == "__main__":
    main()
    

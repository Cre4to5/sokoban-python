from sokoban import Level, Player
def Console_renderer(level):
    WALL = "###"
    GOAL = " . "
    BOX = "[x]"
    BOX_ON_GOAL = "[o]"
    PLAYER = "\\@/"
    PLAYER_ON_GOAL = "(@)"
    
    for line in level:
            for char in line:
                match char:
                    # case "#":
                    #     print(WALL,end="")
                    # case ".":
                    #     print(GOAL,end="")
                    # case "$":
                    #     print(BOX,end="")
                    # case "*":
                    #     print(BOX_ON_GOAL,end="")
                    # case "@":
                    #     print(PLAYER,end="")
                    # case "+":
                    #     print(PLAYER_ON_GOAL,end="")
                    # case " ":
                    #     print("   ",end="")
                    case _:
                        print(char,end="")
            print()
def main():
    player = Player(Level(0,Console_renderer))
    # print(f"*{type(player)}*")
    while True:
        player.level.display()
        print(player.row, player.collumn)
        dire = input("N,E,S,W:\n")
        # print(type(dire))
        player.move(direction=dire)

if __name__ == "__main__":
    main()


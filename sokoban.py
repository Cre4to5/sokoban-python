class Level:
    def __init__(self,lvl_nr, render):
        try:
            self.level = Level.load(lvl_nr)
            self.render = render
            self.boxes = self.get_boxes
        except Exception as e:
            print(e)
        else:
            self.nr = lvl_nr

    def get_player(self):
        for row, line in enumerate(self.level):
            for collumn, char in enumerate(line):
                if char == "@" or char == "+":
                    # print((j, i, char))
                    return (row, collumn, char)# x, y, char

    def get_boxes(self):
        boxes = list()
        for row, line in enumerate(self.level):
            for collumn, char in enumerate(line):
                if char == "$" or char == "*":
                    boxes.append((row, collumn, char))# x, y, char
        return boxes

    def load(lvl_nr):
        with open("./levels.txt") as file:
            text = file.read()
            levels = text.split("\n\n")
            # print(levels)
            level = levels[lvl_nr].split("\n")
            # print(level)
            rows = []
            for line in level:
                cells = []
                for char in line:
                    cells.append(char)
                rows.append(cells)
            # print(lines)
            return rows
        
    def display(self): self.render(self.level)

class Movable:
    def __init__(self, cords_char):
        row, collumn, char = cords_char
        self.row = row
        self.collumn = collumn
        self.char = char

    def move(self, level, replace_with_arrival=None, replace_with_leving=None, direction =""):
        # print(place)
        row = self.row
        collumn = self.collumn
        match direction:
            case "N":
                row = self.row - 1
            case "E":
                collumn = self.collumn + 1
            case "S":
                row = self.row + 1
            case "W":
                collumn = self.collumn - 1
        place = replace_with_arrival(self.to_replace, level.level, row, collumn)
        if place != "not":
            # print("tak")
            level.level[self.row][self.collumn] = replace_with_leving(level.level)
            level.level[row][collumn] = place
            self.collumn = collumn
            self.row = row
        return level
    
    def to_replace(self, level, row, collumn):
        return level[row][collumn]

class Player(Movable):
    def __init__(self, level):
        self.level = level
        cords_char = level.get_player()
        super().__init__(cords_char)
        self.on_target = not cords_char == "@"
        # pass

    def move(self, direction = ""):
        # place = replace_with(self.to_replace, level, direction)
        self.level = super().move(self.level, self.replace_with_arrival, self.replace_with_leaving, direction)
        # self.level.display()
    
    def replace_with_arrival(self, to_replace, level, row, collumn):
        match to_replace(level, row, collumn):
            case " " | "$":
                return "@"
            case "." | "*":
                return "+"
            case _:
                return "not"
    def replace_with_leaving(self, level):
        match level[self.row][self.collumn]:
            case "@":
                return " "
            case "+":
                return "."
            case _:
                return "_"
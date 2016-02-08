class Map:
    def __init__(self, x, y, start_terrain):
        self.map_array = []
        self.x = x
        self.y = y
        for i in range(0, y):
            self.map_array.append([])
            for j in range(0, x):
                self.map_array[i].append(start_terrain)
    def __str__(self):
        outstr = ""
        for i in range(0, y):
            for j in range(0, x):
                outstr += self.map_array[i][j].symbol
            outstr += "\n"
        return outstr

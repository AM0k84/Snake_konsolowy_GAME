class Map:
    def __init__(self, size_x, size_y, empty_char=' '):
        self.size_x = size_x
        self.size_y = size_y
        self.empty_char = empty_char
        self.__map = []
        for y in range(self.size_y):
            self.__map.append([]) #[[]]
            for x in range(self.size_x):
                self.__map[y].append(self.empty_char)
                #[[' ', ' ',' ',' '],
                #[' ', ' ', ' ', ' '],
                #[' ', ' ', ' ', ' ']
                # ]


    def clean(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                self.__map[y][x] = self.empty_char

    def print(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                print(self.__map[y][x], end='')
            print()

    def put_point(self, point):
        self.__map[point.y][point.x] = point.char

    #my_map.put_point(my_point)

#atrybuty
    #sizeX
    #sizeY
    #empty_char - tło
    # nasza mapa  - #lista 2D znaków

# metody
    # clean() - czyszczenie mapy
    # print() - wypisz mapę na ekenie
    # put_point() - umieść punkt na mapie (Point)



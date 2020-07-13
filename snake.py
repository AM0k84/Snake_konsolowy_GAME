from point import Point

class Snake:
    def __init__(self, max_x, max_y, start_x, start_y, body_char='X'):
        self.body_char = body_char
        self.max_x = max_x
        self.max_y = max_y
        self.direction = Point(1, 0)
        self.body = [Point(start_x, start_y, self.body_char)]

    def move(self):
        # ustaw elemetent 2 tam gdzie 1, 1 tam gdzie 0
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # na koncu przesuń głowę
        self.body[0].x += self.direction.x
        self.body[0].y += self.direction.y

        if self.body[0].x >= self.max_x:
            self.body[0].x = 0

        if self.body[0].x < 0:
            self.body[0].x = self.max_x - 1

        if self.body[0].y >= self.max_y:
            self.body[0].y = 0

        if self.body[0].y < 0:
            self.body[0].y = self.max_y - 1

    # nowy element body wstawimy gdzie głowa
    # przy move sie presnie w dobre miejsce
    def add(self):
        new_element = Point(self.body[0].x, self.body[0].y, self.body_char)
        self.body.append(new_element)

# klasa snake
# atrybuty
  # body - liste punktów - gdzie pierwszy punkt[0] to głowa
  # direction - Point x = -1 ,0, 1 y = -1, 0 , 1
                     #x  y
                     #-1 0 w lewo
                     #1 0 w prawo
                     #0 -1 w górę
                     # 0 1 w dół
# modedy
# move() rusz się
# add() dodaj nowy punkt do snake


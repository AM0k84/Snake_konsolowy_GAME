from point import Point
import random
# Jabło - dziedziczy po point

class Apple(Point):
    def __init__(self, max_x, max_y):
        super(Apple, self).__init__(0, 0, 'A')
        self.max_x = max_x
        self.max_y = max_y
        self.x = random.randint(0, self.max_x - 1)
        self.y = random.randint(0, self.max_y - 1)

    def set_new_place(self):
        self.x = random.randint(0, self.max_x - 1)
        self.y = random.randint(0, self.max_y - 1)


#metody:
# wylosuj nowe miejsce (maxX, maxY)

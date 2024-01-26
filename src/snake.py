from direction import Direction

class Snake:
    def __init__(self, direction=Direction.RIGHT, length=3):
        self.length = length
        self.direction = Direction.RIGHT
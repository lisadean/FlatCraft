from block import Block


class Terrain(Block):
    def __init__(self):
        super().__init__()

    def setPosition(self, pos):
        self.rect.topleft = pos

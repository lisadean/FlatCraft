from terrain import Terrain


class Grass(Terrain):
    def __init__(self, pos):
        super().__init__()
        self.image = './images/grass.png'
        # self.pos = [0, 0]
        self.pos = pos
        self.setImage(self.image)
        self.setSize()
        self.setPosition(self.pos)

from terrain import Terrain


class Ore(Terrain):

    scarcity_percentage = 2

    def __init__(self, pos):
        super().__init__()
        self.image = './images/ore.png'
        self.pos = pos
        self.setImage(self.image)
        self.setSize()
        self.setPosition(self.pos)

from terrain import Terrain


class Tree(Terrain):

    scarcity_percentage = 10

    def __init__(self, pos):
        super().__init__()
        self.image = './images/tree.png'
        self.pos = pos
        self.setImage(self.image)
        self.setSize()
        self.setPosition(self.pos)

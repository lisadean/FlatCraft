from block import Block


class Terrain(Block):
    def __init__(self):
        super().__init__()

    def setPosition(self, pos):
        self.rect.topleft = pos


class Grass(Terrain):
    def __init__(self, pos):
        super().__init__()
        self.image = './images/grass.png'
        self.pos = pos
        self.setImage(self.image)
        self.setSize()
        self.setPosition(self.pos)


class Tree(Terrain):

    scarcity_percentage = 10

    def __init__(self, pos):
        super().__init__()
        self.image = './images/tree.png'
        self.pos = pos
        self.setImage(self.image)
        self.setSize()
        self.setPosition(self.pos)


class Ore(Terrain):

    scarcity_percentage = 2

    def __init__(self, pos):
        super().__init__()
        self.image = './images/ore.png'
        self.pos = pos
        self.setImage(self.image)
        self.setSize()
        self.setPosition(self.pos)

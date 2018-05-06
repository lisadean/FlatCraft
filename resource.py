from block import Block


class Terrain(Block):
    def __init__(self):
        super().__init__()
        self.name = "Generic terrain"
        self.drop = "<undefined>"
        self.harvest_sound = "<undefined>"

    def setPosition(self, pos):
        self.rect.topleft = pos

    def __repr__(self):
        return self.name


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
        self.name = "Tree"
        self.drop = "Wood"
        self.image = './images/tree.png'
        self.harvest_sound = './sounds/wood_chop.ogg'
        self.pos = pos
        self.setImage(self.image)
        self.setSize()
        self.setPosition(self.pos)


class Ore(Terrain):

    scarcity_percentage = 2

    def __init__(self, pos):
        super().__init__()
        self.name = "Ore"
        self.drop = "Metal"
        self.image = './images/ore.png'
        self.harvest_sound = './sounds/ore_mine.ogg'
        self.pos = pos
        self.setImage(self.image)
        self.setSize()
        self.setPosition(self.pos)

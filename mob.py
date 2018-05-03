from block import Block


class Mob(Block):
    def __init__(self):
        super().__init__()
        self.image = './images/goblin.png'
        self.pos = [100, 60]
        self.setImage(self.image)
        self.setSizeAndPosition(self.pos)

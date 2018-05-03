from block import Block


class Player(Block):
    def __init__(self):
        super().__init__()
        self.image = './images/hero.png'
        self.pos = [40, 50]
        self.setImage(self.image)
        self.setSize()
        self.setPosition(self.pos)

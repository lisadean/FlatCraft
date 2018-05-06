from pygame.sprite import spritecollide
from block import Block


class House(Block):
    def __init__(self, pos, harvestable_group, mob_group,
                 house_group):
        super().__init__()
        self.name = "House"
        self.image = './images/house4.png'
        self.setImage(self.image)
        self.setSize()
        self.setPosition(pos)
        if spritecollide(self, harvestable_group, False):
            self = None
        elif spritecollide(self, mob_group, True):
            house_group.add(self)  # Drop a house on a mob to kill it
        elif spritecollide(self, house_group, False):
            self = None
        else:
            house_group.add(self)

    def setPosition(self, pos):
        self.rect.topleft = pos

    def __repr__(self):
        return self.name

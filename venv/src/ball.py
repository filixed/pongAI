import random

class ball:
    def __init__(self):
        self.size = 10
        self.thickness = 1
        self.width = 125
        self.height = 200
        self.speedx = 2#random.random()*2
        self.speedy = 1

    def setWidth(self, width):
        self._width = width

    def setHeight(self, height):
        self._height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
    
    def getSize(self):
        return self.size
    
    def getThick(self):
        return self.thickness

    def move(self):
        self.width+=self.speedx
        self.height+=self.speedy

    def setSpeedxOpposite(self):
        self.speedx*=(-1)

    def setSpeedyOppostie(self):
        self.speedy*=(-1)

    def srodek(self):
        return self.width + (self.size/2)




class paddle:
    def __init__(self, x, y):
        self.width = 75 #srodek 37,5
        self.height = 20
        self.widthX = x
        self.heightY = y
        self.speedx = 1
        self.score = 0

    def getWidth(self):
        return self.widthX

    def getHeight(self):
        return self.heightY

    def getwidth (self):
        return self.width

    def getheight(self):
        return self.height

    def Right(self):
        self.widthX +=2

    def Left(self):
        self.widthX -=2

    def srodek(self):
        return self.widthX + self.width/2

    def updateScore(self):
        self.score+=1

    def getScore(self):
        return self.score



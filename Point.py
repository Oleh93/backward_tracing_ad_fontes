class Point:
    DIRECTONS = {0: [-1, -1], 1: [-1, 0], 2: [-1, 1], 3: [0, 1], 4: [1, 1],
                 5: [1, 0], 6: [1, -1], 7: [0, -1]}

    def __init__(self, i, j, direction=3):
        self.i = i
        self.j = j
        self.direction = direction
        self.exactlybackground = False
        self.isProceeded = False

    def getI(self):
        return self.i

    def getJ(self):
        return self.j

    def faceRight(self):
        self.direction = (self.direction + 2) % 8

    def faceLeftNotClockwise(self):
        if self.direction == 0:
            self.direction = 7
        else:
            self.direction = self.direction - 1

    def faceLeft(self):
        if self.direction == 7:
            self.direction = 0
        else:
            self.direction = self.direction + 1

    def goForward(self):
        point = Point.DIRECTONS[self.direction]
        return point[1] + self.i, point[0] + self.j, self.direction

    def advanceToLeft(self):
        self.faceLeft()
        return self.goForward()

    def advanceToLeftOtherWise(self):
        self.faceLeftNotClockwise()
        return self.goForward()

    def advanceToRight(self):
        self.faceRight()
        return self.goForward()

    def toString(self):
        return self.i, self.j

    def __eq__(self, other):
        if self.getI() == other.getI() and self.getJ() == other.getJ():
            return True
        return False

    def clone(self):
        return Point(self.i, self.j, self.direction)

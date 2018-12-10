from Point import Point


class BackwardTracingService:
    def __init__(self, srcImage):
        self.srcImage = srcImage
        self.contourPixels = []

    def getCountourPoints(self):
        starting_point = self.get_starting_point()  # find starting point
        current_point = starting_point.clone()
        curPixel = self.srcImage[current_point.getJ()][current_point.getI()]
        curPixel.isContourPixel = True
        data = current_point.advanceToRight()
        current_point.direction = data[2]
        checking_point = Point(data[0], data[1])
        while starting_point != current_point or len(self.contourPixels) < 1:
            current_point_clockwise = self.findnext(checking_point,
                                                    starting_point,
                                                    current_point, data)
            current_point_otherwise = self.findnext(checking_point,
                                                    starting_point,
                                                    current_point, data,
                                                    clockwise=False)
            if current_point_clockwise is current_point_otherwise:
                current_point.exactlybackground = True
            else:
                current_point = current_point_clockwise

        return self.srcImage

    def findnext(self, checking_point, starting_point, current_point, data,
            clockwise=True):
        while True:
            if checking_point.isProceeded:
                continue
            if self.srcImage[checking_point.getJ()][checking_point.getI()] == \
                    self.srcImage[starting_point.getJ()][
                        starting_point.getI()]:
                curPixel = self.srcImage[current_point.getJ()][
                    current_point.getI()]

                self.contourPixels.append(curPixel)
                curPixel.isContourPixel = True
                current_point = checking_point.clone()
                if data[2] >= 4:
                    current_point.direction = data[2] - 4
                else:
                    current_point.direction = data[2] + 4

                data = current_point.advanceToRight()
                checking_point.i = data[0]
                checking_point.j = data[1]
                current_point.isProceeded = True
                return current_point
            else:
                if clockwise:
                    data = current_point.advanceToLeft()
                else:
                    data = current_point.advanceToLeftOtherWise()
                checking_point = Point(data[0], data[1])

    def drawContour(self):
        for row in self.srcImage:
            for pixel in row:
                if pixel.isContourPixel:
                    pixel.r = 255
                    pixel.g = 0
                    pixel.b = 0

    def get_starting_point(self):
        for i in range(len(self.srcImage) - 1, -1, -1):
            for j in range(len(self.srcImage[i]) - 1, -1, -1):
                if self.srcImage[i][j - 1] != self.srcImage[i][j]:
                    return Point(j - 1, i)

    def clearBorder(self):
        i_range = [0, len(self.srcImage) - 1]
        j_range = [0, len(self.srcImage[0]) - 1]
        for i in range(len(self.srcImage)):
            for j in range(len(self.srcImage[i])):
                if i in i_range or j in j_range:
                    self.srcImage[i][j] = self.srcImage[0][0].clone()
                    self.srcImage[i][j].i = i
                    self.srcImage[i][j].j = j

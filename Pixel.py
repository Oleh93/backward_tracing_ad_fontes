class Pixel:
    DIFFERENCE = 110

    def __init__(self, r, g, b, i, j, direction=3, isContourPixel=False, ):
        self.i = i
        self.j = j
        self.r = r
        self.g = g
        self.b = b
        self.isContourPixel = isContourPixel
        self.direction = direction

    def __eq__(self, other):
        res = abs(self.r - other.r) < Pixel.DIFFERENCE and \
              abs(self.g - other.g) < Pixel.DIFFERENCE and \
              abs(self.b - other.b) < Pixel.DIFFERENCE
        return res

    def toArr(self):
        return (self.r, self.g, self.b)

    def clone(self):
        return Pixel(self.r, self.g, self.b, self.i, self.j)


def get_array_of_pixels(pixels, size):
    lofpixels = []
    for i in range(size[1]):
        space = []
        for j in range(size[0]):
            r, g, b = pixels[j, i]
            pixel = Pixel(r, g, b, i, j)
            space.append(pixel)
        lofpixels.append(space)
    return lofpixels

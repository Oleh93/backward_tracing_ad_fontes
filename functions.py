from Pixel import Pixel


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

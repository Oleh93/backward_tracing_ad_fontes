from PIL import Image
import numpy as np
from functions import get_array_of_pixels
from BakwardContourTracing import BackwardTracingService
import time


def main():
    input_directory = "input/"
    output_directory = "output/"

    while True:
        try:
            file_name = input("Enter the name of file (Example: photo.jpg):  ")
            im = Image.open(input_directory + file_name)
        except Exception:
            print("Enter correct file name or make sure file exists!\n")
        else:
            break


    start_time = time.time()

    size = im.size
    pixels = im.load()
    lofpixels = get_array_of_pixels(pixels, size)
    traceService = BackwardTracingService(lofpixels)
    traceService.clearBorder()
    traceService.getCountourPoints()
    x = traceService.contourPixels
    traceService.drawContour()
    pixels = traceService.srcImage
    imgSrc = []
    for pixel in pixels:
        spc = []
        for lst in pixel:
            spc.append(lst.toArr())
        imgSrc.append(spc)
    array = np.array(imgSrc, dtype=np.uint8)

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save(output_directory + file_name)
    print("Done!")
    print("time:", time.time() - start_time)


main()


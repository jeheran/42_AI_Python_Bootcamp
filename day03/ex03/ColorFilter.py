import sys
sys.path.insert(0, "/Users/jherelle/bootcamp_python/day04/ex01")
from ImageProcessor import ImageProcessor

class ColorFilter(ImageProcessor):
    def __init__(self):
        pass
    

    def invert(self, array):
        inverted_array = array
        for pix in inverted_array:
            for color in pix:
                color[0] = 1 - color[0]
                color[1] = 1 - color[1]
                color[2] = 1 - color[2]
        return inverted_array


    def to_blue(self, array):
        blue_array = array
        for pix in blue_array:
            for color in pix:
                color[0] = 0
                color[1] = 0
        return blue_array


    def to_green(self, array):
        green_array = array
        for pix in green_array:
            for color in pix:
                color[0] = 0
                color[2] = 0
        return green_array


    def to_red(self, array):
        red_array = array
        for pix in red_array:
            for color in pix:
                color[1] = 0
                color[2] = 0
        return red_array

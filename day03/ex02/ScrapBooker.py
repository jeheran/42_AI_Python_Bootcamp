import numpy as np
import matplotlib
import sys
sys.path.insert(0, "/Users/jherelle/bootcamp_python/day04/ex01")
from ImageProcessor import ImageProcessor

class ScrapBooker(ImageProcessor):

    def __init__(self):
        pass

    def crop(self, array, dimensions, position=(0, 0)):
        if dimensions > array.shape[0] or position[0] + position[1] > array.shape[0]:
            raise TypeError("Dimensions can't be larger than current size")
        cropped = array[position[0]:dimensions,position[1]:dimensions]
        return cropped

    def thin(self, array, n, axis):
        return np.delete(array, n, axis)


    def juxtapose(array, n, axis):
        tmp = array
        i = 0
        if axis == 0:
            while i < n - 1:
                tmp = np.vstack((tmp, array))
                print("stacked once")
                i += 1
        if axis == 1:
            while i < n - 1:
                tmp = np.hstack((tmp, array))
                i += 1
        return tmp

    def mosaic(array, dimensions):
        if not isinstance(dimensions, tuple):
            raise TypeError("Please enter a tuple as dimensions")
        juxtapose_x = ScrapBooker.juxtapose(array, dimensions[0], 0)
        print("H stack ok")
        final = ScrapBooker.juxtapose(juxtapose_x, dimensions[1], 1)
        return final



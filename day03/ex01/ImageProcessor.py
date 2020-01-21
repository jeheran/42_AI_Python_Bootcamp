import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class ImageProcessor:
    def __init__(self):
        pass

    def load(self, path):
        try:
            self.img_data = mpimg.imread(path)
        except:
            raise TypeError("Failed to load img")
        else:
            print("Loading image of dimensions {} X {}\n\n".format(self.img_data.shape[0], self.img_data.shape[1]))
        return self.img_data

    def display(self, array):
        plt.imshow(array)
        plt.show()


import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


class MyPlotLib:
    def __init__(self):
        pass

    def histogram(self, data, features):
        for feature in features:
            if isinstance(data[feature][0], int) or isinstance(data[feature][0], float):
                plt.hist(data[feature])
            else:
                print("===> Not numerical : {}\n".format(feature))
            plt.show()

    def density(self, data, features):
        for feature in features:
            if isinstance(data[feature][0], int) or isinstance(data[feature][0], float):
                plt.hist(data[feature])
            else:
                print("===> Not numerical : {}\n".format(feature))
            plt.show()

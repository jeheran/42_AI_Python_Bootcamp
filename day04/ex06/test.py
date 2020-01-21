from MyPlotLib import MyPlotLib
from FileLoader import FileLoader
import matplotlib.pyplot as plt
import numpy as np

loader = FileLoader()
data = loader.load('../ex00/athlete_events.csv')



plting = MyPlotLib()

MyPlotLib.histogram(plting, data, ["City", "Weight", "Height"])



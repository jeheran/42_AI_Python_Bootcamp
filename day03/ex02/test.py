from ScrapBooker import ScrapBooker
import numpy as np
import matplotlib
#from PIL import Image

img = ScrapBooker()
data_img = img.load("42AI.png")
######################
#img.display(img.crop(data_img, 100, (250, 250)))
#######################
arr = np.array([['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', '1'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', '2'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', '3'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', '4'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', '5'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', '6'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', '7'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', '8'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', '9'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Q', '10']
        ])

#arr = img.thin(arr, 3, 1)
#print(arr)
######################
#juxtaposed_v = ScrapBooker.juxtapose(data_img, 3, 0)
#juxtaposed_h = ScrapBooker.juxtapose(data_img, 3, 1)
#img.display(juxtaposed_v)
#img.display(juxtaposed_h)
#####################
mosaic = ScrapBooker.mosaic(data_img, (6,6))
img.display(mosaic)
#####################


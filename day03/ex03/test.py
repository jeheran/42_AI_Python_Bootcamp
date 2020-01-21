from ColorFilter import ColorFilter


img = ColorFilter()
data_img = ColorFilter.load(img, "elon.png")
####################
#inverted = ColorFilter.invert(img, data_img)
#img.display(inverted)
####################
#blue = ColorFilter.to_blue(img, data_img)
#print(blue)
#img.display(blue)
###################
#green = ColorFilter.to_green(img, data_img)
red = ColorFilter.to_red(img, data_img)
##################
#img.display(green)
img.display(red)
#################


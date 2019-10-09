import cv2 as cv
import numpy as np

def coordinate_to_opencv(l, img):
	# l is a list of 4 numbers, the x and y coordinates of upper left and bottom right corners in that order [x_ul y_ul x_br y_br]
	# img is an opencv image
	# This function converts to standard opencv format (matrix like)
	m = []
	m.append(img.shape[0] - l[1])
	m.append(l[0])
	m.append(img.shape[0] - l[3])
	m.append(l[2])
	return m


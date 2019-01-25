import cv2
import numpy as np
import math
from scipy import ndimage

def getBestShift(img):
    cy,cx = ndimage.measurements.center_of_mass(img)
    rows,cols = img.shape
    shiftx = int(round(cols/2.0-cx))
    shifty = int(round(rows/2.0-cy))
    return shiftx,shifty

def shift(img,sx,sy):
    rows,cols = img.shape
    M = np.float32([[1,0,sx],[0,1,sy]])
    shifted = cv2.warpAffine(img,M,(cols,rows))
    return shifted

def convert_to_mnist(imgSource):
	img_gray = cv2.imread(imgSource,0)
	(thresh, img_gray) = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
	
	while np.sum(img_gray[0]) == 0:
		img_gray = img_gray[1:]
	while np.sum(img_gray[:,0]) == 0:
		img_gray = np.delete(img_gray,0,1)
	while np.sum(img_gray[-1]) == 0:
		img_gray = img_gray[:-1]
	while np.sum(img_gray[:,-1]) == 0:
		img_gray = np.delete(img_gray,-1,1)

	rows,cols = img_gray.shape
	if rows>cols:
		factor = 20.0/rows
		rows = 20
		cols = int(round(cols*factor))
		img_gray = cv2.resize(img_gray,(cols,rows))
	else:
		factor = 20.0/cols
		cols = 20
		rows = int(round(rows*factor))
		img_gray = cv2.resize(img_gray,(cols,rows))

	cols_padding = (int(math.ceil((28-cols)/2.0)), int(math.floor((28-cols)/2.0)))
	rows_padding = (int(math.ceil((28-rows)/2.0)), int(math.floor((28-rows)/2.0)))
	img_gray = np.lib.pad(img_gray, (rows_padding, cols_padding),'constant')

	sx,sy = getBestShift(img_gray)
	img_gray = shift(img_gray,sx,sy)
	cv2.imwrite("output.jpg",img_gray)
	return img_gray
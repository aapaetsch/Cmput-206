import numpy as np
from scipy import ndimage, misc
import skimage.io as sk


def main():
	imgArray = np.zeros(256, dtype = int)
	print(imgArray)
	a = sk.imread('test.jpg', True)
	u = 0
	for i in a:
		u+=1
		j =0
		for x in i:
			j+=x
		j = int(round(j))

		imgArray[j]+=1

	print(imgArray)


	





main()
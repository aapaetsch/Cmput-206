# -*- coding: utf-8 -*-
"""part3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/133vVHfj8nZxXX5-NBCqEbUGKouhFS4U7
"""

from google.colab import drive

drive.mount('/content/gdrive')

!ls '/content/gdrive/My Drive/CMPUT 206 Wi19/Lab1_Files/'
filename_Day = '/content/gdrive/My Drive/CMPUT 206 Wi19/Lab1_Files/day.jpg'
filename_Night = '/content/gdrive/My Drive/CMPUT 206 Wi19/Lab1_Files/night.jpg'
filename_Test = '/content/gdrive/My Drive/CMPUT 206 Wi19/Lab1_Files/test.jpg'

#Your Code 
import numpy as np
from skimage import io, exposure, img_as_ubyte
import matplotlib.pyplot as plt
import math


#write a program to compare histograms of two images day and night, convert to
#gray scale, compute their histograms and print the Bhattacharyya coefficient

def main():
    dayIn = img_as_ubyte(io.imread(filename_Day, as_grey=True))
    nightIn = img_as_ubyte(io.imread(filename_Night, as_grey=True))
#     testIn = img_as_ubyte(io.imread(filename_Test, as_grey=True))
    
    dayHist = builtinHist(dayIn)
    #dayHist = myhist(dayIn)
    nightHist = builtinHist(nightIn)
    #nightHist = myhist(nightIn)
#     testHist = builtinHist(testIn)
    
    plt.legend(('day.jpg','night.jpg'), loc=2)
    plt.show()
    BC(dayHist[0], nightHist[0])
   

def builtinHist(IMG):
    A = exposure.histogram(IMG, nbins=256)
    plt.xlim(0,256)
    plt.ylim(0,6000)
    plt.plot(A[0])
    return A

#Bhattacharya coefficient
def BC(hist1, hist2):
    #normalize the histogram
    hist1 = normalize(hist1)
    hist2 = normalize(hist2)
    sm = 0
    for i in range(len(hist1)):
        sm+=math.sqrt((hist1[i]*hist2[i]))
    print("The Bahattacharya Coefficient is:",sm)
    
def normalize(hist):
    #divide each histogram by the sum of all its entries
    #sumCum= np.cumsum(hist)
    sc = 0
    for i in hist:
        sc+=i
    normHist = np.zeros(256)
    for i in range(len(normHist)):
        normHist[i] = hist[i]/sc
      
    return normHist

main()
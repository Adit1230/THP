import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os

test_num = 100
dataset_path = "Data"
img_pair_list = os.listdir(dataset_path)
stereo = cv.StereoBM_create(numDisparities=64, blockSize=35)

for i in range(0, min(test_num, len(img_pair_list)) ):
    folder = img_pair_list[i]

    #Load image pair
    imgL = cv.imread( 'Data/' + folder + '/im0.png', cv.IMREAD_GRAYSCALE)
    imgR = cv.imread( 'Data/' + folder + '/im1.png', cv.IMREAD_GRAYSCALE)

    #Calculate the depth map
    disparity = stereo.compute(imgL,imgR)

    #Show the depth map using matplotlib
    plt.imshow(disparity,'gray')
    plt.show()

    #To save the depth map
    #plt.savefig( 'Data/' + folder + '/DepthMap.png')

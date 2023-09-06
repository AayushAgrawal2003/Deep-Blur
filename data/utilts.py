import cv2
import skimage.exposure
import numpy as np
from numpy.random import default_rng

# define random seed to change the pattern
seedval = 55
rng = default_rng(seed=seedval)

def create_segmentation_map(image):
    height, width = image.shape
    height -= 10
    width -= 10
    noise = rng.integers(0, 255, (height, width), np.uint8, True)
    blur = cv2.GaussianBlur(noise, (0, 0), sigmaX=15,
                            sigmaY=15, borderType=cv2.BORDER_DEFAULT)

    stretch = skimage.exposure.rescale_intensity(
        blur, in_range='image', out_range=(0, 255)).astype(np.uint8)

    thresh = cv2.threshold(stretch, 175, 255, cv2.THRESH_BINARY)[1]

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
    result = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    result = cv2.morphologyEx(result, cv2.MORPH_CLOSE, kernel)

    return result
    # cv2.imshow('result', result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def create_add_blur(image,mask):
    height, width = image.shape
    kernel_size = (5, 5)  # You can change these values

    for i in range(height):
        for j in range(width):
            if mask[i][j] == 0: 
                image[i][j] = cv2.GaussianBlur(image[i][j], kernel_size, 0)
                
    
    return image


    
    
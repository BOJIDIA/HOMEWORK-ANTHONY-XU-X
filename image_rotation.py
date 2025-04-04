import cv2 as cv
import numpy as np
from typing import *

# relative path: "asset/sunglass_cat.jpg"
# strength: other people can use our program given that the file structures are the same
# -> because relative path gives the location of the file based on the current program,
# it doesn't depend on the machine itself
# weakness: you need to know the exact file structures

def load_image(file_path):
    """
    Return the numerical information of the image as a list
    """
    image = cv.imread(file_path)
    return image

def alter_red(image, value):
    """
    Change every value corresponding to "R" (of BGR) to <value>

    image has dimensions (length, width, BGR)
    """
    n_row = image.shape[0]
    n_col = image.shape[1]
    idx_red = 2

    for i in range(n_row):
        for j in range(n_col):
            image[i, j, idx_red] = value

def alter_blue(image, value):
    """
    Change every value corresponding to "R" (of BGR) to <value>

    image has dimensions (length, width, BGR)
    """
    n_row = image.shape[0]
    n_col = image.shape[1]
    idx_blue = 0

    for i in range(n_row):
        for j in range(n_col):
            image[i, j, idx_blue] = value

def alter_green(image, value):
    """
    Change every value corresponding to "R" (of BGR) to <value>

    image has dimensions (length, width, BGR)
    """
    n_row = image.shape[0]
    n_col = image.shape[1]
    idx_green = 1

    for i in range(n_row):
        for j in range(n_col):
            image[i, j, idx_green] = value


def save_image(to_path, image):
    """
    save image to <to_path>
    """
    cv.imwrite(to_path, image)

def clock_wise_rotation(image):
    """
    Rotate the given <image> 90 degrees clock wise
    Return the rotated image
    """
    n_row = image.shape[0]
    n_col = image.shape[1]

    result = np.zeros((n_col, n_row, 3))

    for i in range(n_row):
        for j in range(n_col):
            result[j, n_row - 1 - i, :] = image[i, j, :]
    return result.astype(np.uint8)

def ccwr(image):
    """
    Rotate the given <image> 90 degerees counterclockwise
    Return the rotated image
    
    """
    n_row = image.shape[0]
    n_col = image.shape[1]
    result = np . zeros((n_col , n_row , 3))
    for i in range (n_row):
        for j in range (n_col):
            result[n_col - j - 1, i, :] = image[i, j , :]
    return result.astype(np.uint8)
    
if __name__ == "__main__":
    image = load_image("New folder/sunglass_cat.jpeg")
    new_image = ccwr(image)
    save_image("New folder/altered_image_rotated_ccw.jpeg", new_image)
import pytest
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import numpy as np

from image_modifier.rotate_90 import rotate_90

#Creating a Test Image for the test cases
test_img = [
    [11, 12, 13, 14],
    [21, 22, 23, 24],
    [31, 32, 33, 34]
]

rotated_test_img_90 = rotate_90(test_img) # rotating the test image by 90 degrees

rotated_test_img_180 = rotate_90(rotated_test_img_90) # rotating the test image by 180 degrees

rotated_test_img_270 = rotate_90(rotated_test_img_180) # rotating the test image by 270 degrees

rotated_test_img_360 = rotate_90(rotated_test_img_270) # rotating the test image by 360 degrees

def check_type(): # Checking the data type of the image
    if test_img != []:
        assert type(test_img) == np.ndarray

def empty(): # Checking if empty image returns empty image
    test_empty = []
    if test_empty == []:
        assert np.array_equal(test_empty, rotate_90(test_empty))

def dimension(): # checking dimension on each rotation
    if test_img != []:
        assert test_img.shape[0] == rotated_test_img_90.shape[1] # 90 degrees
        assert test_img.shape[1] == rotated_test_img_90.shape[0] # 90 degrees

        assert test_img.shape[0] == rotated_test_img_180.shape[0] # 180 degrees
        assert test_img.shape[1] == rotated_test_img_180.shape[1] # 180 degrees

        assert test_img.shape[0] == rotated_test_img_270.shape[1] # 270 degrees
        assert test_img.shape[1] == rotated_test_img_270.shape[0] # 270 degrees

        assert test_img.shape[0] == rotated_test_img_360.shape[0] # 360 degrees
        assert test_img.shape[1] == rotated_test_img_360.shape[1] # 360 degrees

def rotation(): # Checking if the rotation is performed correctly

    expected_rotated_1 = [
        [31, 21, 11],
        [32, 22, 12],
        [33, 23, 13],
        [34, 24, 14]
    ]
    assert np.array_equal(rotate_90(test_img), expected_rotated_1) 

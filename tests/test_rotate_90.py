import pytest
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import numpy as np

from image_modifier.rotate_90 import rotate_90

#Creating a Test Image for the test cases
test_img = [[[245, 112],
        [ 68, 191]],

       [[ 88, 219],
        [ 33,  16]],

       [[209, 232],
        [200,  74]]]

test_img = np.array(test_img)

rotated_test_img_90 = rotate_90(test_img) # rotating the test image by 90 degrees

rotated_test_img_180 = rotate_90(rotated_test_img_90) # rotating the test image by 180 degrees

rotated_test_img_270 = rotate_90(rotated_test_img_180) # rotating the test image by 270 degrees

rotated_test_img_360 = rotate_90(rotated_test_img_270) # rotating the test image by 360 degrees

def test_check_type(): # Checking the data type of the image
    assert type(test_img) == np.ndarray

def test_empty(): # Checking if empty image returns empty image
    test_empty = []
    assert np.array_equal(test_empty, rotate_90(test_empty))

def test_dimension(): # checking dimension after rotation
    assert test_img.shape[0] == rotated_test_img_90.shape[1] # 90 degrees
    assert test_img.shape[1] == rotated_test_img_90.shape[0] # 90 degrees
    assert test_img.shape[2] == rotated_test_img_90.shape[2] # 90 degrees

    assert test_img.shape[0] == rotated_test_img_180.shape[0] # 180 degrees
    assert test_img.shape[1] == rotated_test_img_180.shape[1] # 180 degrees
    assert test_img.shape[2] == rotated_test_img_180.shape[2] # 180 degrees

    assert test_img.shape[0] == rotated_test_img_270.shape[1] # 270 degrees
    assert test_img.shape[1] == rotated_test_img_270.shape[0] # 270 degrees
    assert test_img.shape[2] == rotated_test_img_270.shape[2] # 270 degrees

    assert test_img.shape[0] == rotated_test_img_360.shape[0] # 360 degrees
    assert test_img.shape[1] == rotated_test_img_360.shape[1] # 360 degrees
    assert test_img.shape[2] == rotated_test_img_360.shape[2] # 360 degrees

def test_rotation(): # Checking if the rotation is performed correctly
    
    # checking 90 degree rotation(rotating once)
    expected_rotated_90 = [[[209, 232],
        [ 88, 219],
        [245, 112]],

       [[200,  74],
        [ 33,  16],
        [ 68, 191]]]
    expected_rotated_90 = np.array(expected_rotated_90)

    assert np.array_equal(rotate_90(test_img), expected_rotated_90)

    # checking 180 degree rotation(rotating twice)
    expected_rotated_180 = [[[200,  74],
        [209, 232]],

       [[ 33,  16],
        [ 88, 219]],

       [[ 68, 191],
        [245, 112]]]
    expected_rotated_180 = np.array(expected_rotated_180)

    assert np.array_equal(rotate_90(rotate_90(test_img)), expected_rotated_180)

    # checking 270 degree rotation(rotating thrice)
    expected_rotated_270 = [[[ 68, 191],
        [ 33,  16],
        [200,  74]],

       [[245, 112],
        [ 88, 219],
        [209, 232]]]
    expected_rotated_270 = np.array(expected_rotated_270)

    assert np.array_equal(rotate_90(rotate_90(rotate_90(test_img))), expected_rotated_270)

    # checking 360 degree rotation(rotating four times)
    expected_rotated_360 = [[[245, 112],
        [ 68, 191]],

       [[ 88, 219],
        [ 33,  16]],

       [[209, 232],
        [200,  74]]]
    expected_rotated_360 = np.array(expected_rotated_360)

    assert np.array_equal(test_img, expected_rotated_360) 

import pytest
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import numpy as np

from image_modifier.rotate_90 import rotate_90

#Creating a Test Image for the test cases
test_img = np.array([[[255, 0, 0],   # Red
                            [0, 255, 0],   # Green
                            [0, 0, 255],   # Blue
                            [255, 255, 0]], # Yellow

                           [[128, 128, 128], # Gray
                            [255, 127, 0],   # Orange
                            [0, 255, 255],   # Cyan
                            [255, 0, 255]]]) # Magenta

rotated_test_img_90 = rotate_90(test_img) # rotating the test image by 90 degrees

rotated_test_img_180 = rotate_90(rotated_test_img_90) # rotating the test image by 180 degrees

rotated_test_img_270 = rotate_90(rotated_test_img_180) # rotating the test image by 270 degrees

rotated_test_img_360 = rotate_90(rotated_test_img_270) # rotating the test image by 360 degrees

def test_check_type(): # Checking the data type of the image
    assert type(test_img) == np.ndarray

def test_empty(): # Checking if empty image returns empty image
    test_empty = []
    assert np.array_equal(test_empty, rotate_90(test_empty))

def test_invalid_image(): # Test with a 4D array (invalid shape）
    invalid_image = np.zeros((100, 100, 3, 1), dtype=np.uint8)
    with pytest.raises(ValueError):
        rotate_90(invalid_image)


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
    expected_rotated_90 = np.array([[[128, 128, 128],
        [255,   0,   0]],

       [[255, 127,   0],
        [  0, 255,   0]],

       [[  0, 255, 255],
        [  0,   0, 255]],

       [[255,   0, 255],
        [255, 255,   0]]])

    assert np.array_equal(rotate_90(test_img), expected_rotated_90)

    # checking 180 degree rotation(rotating twice)
    expected_rotated_180 = np.array([[[255,   0, 255],
        [  0, 255, 255],
        [255, 127,   0],
        [128, 128, 128]],

       [[255, 255,   0],
        [  0,   0, 255],
        [  0, 255,   0],
        [255,   0,   0]]])

    assert np.array_equal(rotate_90(rotate_90(test_img)), expected_rotated_180)

    # checking 270 degree rotation(rotating thrice)
    expected_rotated_270 = np.array([[[255, 255,   0],
        [255,   0, 255]],

       [[  0,   0, 255],
        [  0, 255, 255]],

       [[  0, 255,   0],
        [255, 127,   0]],

       [[255,   0,   0],
        [128, 128, 128]]])
    
    assert np.array_equal(rotate_90(rotate_90(rotate_90(test_img))), expected_rotated_270)

    # checking 360 degree rotation(rotating four times)
    expected_rotated_360 = np.array([[[255,   0,   0],
        [  0, 255,   0],
        [  0,   0, 255],
        [255, 255,   0]],

       [[128, 128, 128],
        [255, 127,   0],
        [  0, 255, 255],
        [255,   0, 255]]])

    assert np.array_equal(test_img, expected_rotated_360) 

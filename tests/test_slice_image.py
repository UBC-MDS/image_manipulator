from image_modifier.slice_image import slice_image
import pytest

def test_valud_input():
    # Mock a simple 8x8 pixel image as a 2D list
    image = [[(i, j) for j in range(8)] for i in range(8)]

    # Test valid input
    slices = slice_image(image, 2, 2)
    assert len(slices) == 2 and len(slices[0]) == 2 and len(slices[0][0]) == 4, "Test 1 Failed: Incorrect number of slices or slice size for valid input"

def test_small_image():
    # Test 2: Edge Case Input
    small_image = [[(0, 0)]]
    slices = slice_image(small_image, 1, 1)
    assert len(slices) == 1 and len(slices[0]) == 1 and len(slices[0][0]) == 1, "Test 2 Failed: Incorrect handling of edge case (small image)"

def test_invalid_input():
    # Test invalid input
    image = [[(i, j) for j in range(8)] for i in range(8)]
    try:
        slice_image("not a 2D list", 2, 2)
        assert False, "Test 3 Failed: No error raised for invalid image input"
    except:
        pass

    try:
        slice_image(image, "not an int", 2)
        assert False, "Test 3 Failed: No error raised for invalid horizontal_slices input"
    except:
        pass

    try:
        slice_image(image, 2, "not an int")
        assert False, "Test 3 Failed: No error raised for invalid vertical_slices input"
    except:
        pass

def test_slice_image_content():
    # Test the content of the slices to ensure they are correct
    image = [[(i, j) for j in range(4)] for i in range(4)]
    slices = slice_image(image, 2, 2)
    assert slices[0][0] == [[(0, 0), (0, 1)], [(1, 0), (1, 1)]], "Test 4 Failed: Incorrect content in slices"

def test_large_number_of_slices():
    # Test slicing with more slices than the image size
    image = [[(i, j) for j in range(4)] for i in range(4)]
    slices = slice_image(image, 5, 5)
    assert len(slices) == 4 and all(len(slice) == 4 for slice in slices), "Test 5 Failed: Incorrect handling of more slices than image size"

def test_single_slice():
    # Test slicing into a single slice
    image = [[(i, j) for j in range(4)] for i in range(4)]
    slices = slice_image(image, 1, 1)
    assert len(slices) == 1 and len(slices[0]) == 1, "Test 6 Failed: Incorrect number of slices for single slice"

def test_uneven_slices():
    # Test slicing with uneven slice sizes
    image = [[(i, j) for j in range(5)] for i in range(5)]
    slices = slice_image(image, 2, 3)
    assert len(slices) == 2 and len(slices[0]) == 3, "Test 7 Failed: Incorrect handling of uneven slices"

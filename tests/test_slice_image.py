from image_modifier.slice_image import image_break_into_slices, slice_image
import pytest
import numpy as np
import matplotlib.pyplot as plt

# Tests for image_break_into_slices function
def test_break_into_slices_valid():
    test_image = np.random.rand(100, 100, 3)

    # Valid input: Even division
    slices = image_break_into_slices(test_image, 2, 2)
    assert len(slices) == 2 and len(slices[0]) == 2

    # Valid input: Uneven division
    slices = image_break_into_slices(test_image, 3, 2)
    assert len(slices) == 3 and len(slices[0]) == 2

    # Valid input: Non-square image
    test_image_2 = np.random.rand(100, 50, 3)
    slices = image_break_into_slices(test_image_2, 10, 5)
    assert len(slices) == 10 and len(slices[0]) == 5

def test_break_into_slices_edge_cases():
    test_image = np.random.rand(100, 100, 3)

    # Edge case: More slices than pixels
    slices = image_break_into_slices(test_image, 101, 101)
    assert len(slices) == 100 and len(slices[0]) == 100

    # Edge case: One slice
    slices = image_break_into_slices(test_image, 1, 1)
    assert len(slices) == 1 and len(slices[0]) == 1

    # Edge case: Empty image
    test_image_2 = np.array([])
    with pytest.raises(ValueError):
        image_break_into_slices(test_image_2, 1, 1)
    
def test_break_into_slices_invalid_input():
    test_image = np.random.rand(100, 100, 3)

    # Invalid input: Invalid array
    with pytest.raises(TypeError):
        image_break_into_slices("not an array", 2, 2)

    # Valid input: Single channel image
    test_image_2 = np.random.rand(100, 100) # 2D array for grayscale image
    with pytest.raises(ValueError):
        image_break_into_slices(test_image_2, 2, 2)
    
    # Invalid input: Non-integer slice numbers
    with pytest.raises(TypeError):
        image_break_into_slices(test_image, "2", 2)

    # Invalid input: Negative slice numbers
    with pytest.raises(ValueError):
        image_break_into_slices(test_image, -1, 2)

# Tests for slice_image function
def test_slice_image_valid():
    test_image = np.random.rand(100, 100, 3)

    # Valid input: Even division
    slices = slice_image(test_image, 2, 2)
    assert len(slices) == 2 and len(slices[0]) == 2

    # Valid input: Uneven division
    slices = slice_image(test_image, 3, 2)
    assert len(slices) == 3 and len(slices[0]) == 2

    # Valid input: Non-square image
    test_image_2 = np.random.rand(100, 50, 3)
    slices = slice_image(test_image_2, 10, 5)
    assert len(slices) == 10 and len(slices[0]) == 5

def test_slice_image_edge_cases():
    test_image = np.random.rand(5, 5, 3)

    # Edge case: More slices than pixels
    slices = slice_image(test_image, 6, 6)
    assert len(slices) == 5 and len(slices[0]) == 5

    # Edge case: One slice
    slices = slice_image(test_image, 1, 1)
    assert len(slices) == 1 and len(slices[0]) == 1

def test_slice_image_invalid_input():
    test_image = np.random.rand(100, 100, 3)
    
    # Invalid input: Invalid array
    with pytest.raises(TypeError):
        slice_image("not an array", 2, 2)

    # Invalid input: Single channel image
    test_image_2 = np.random.rand(100, 100) # 2D array for grayscale image
    with pytest.raises(ValueError):
        slice_image(test_image_2, 2, 2)

    # Invalid input: Non-integer slice numbers
    with pytest.raises(TypeError):
        slice_image(test_image, "2", 2)

    # Invalid input: Negative slice numbers
    with pytest.raises(ValueError):
        slice_image(test_image, -1, 2)
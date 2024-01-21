from image_modifier.slice_image import image_break_into_slices, slice_image
import pytest
import numpy as np
import matplotlib.pyplot as plt

def test_image_break_into_slices_valid_input():
    # Test the function with valid input
    image = np.random.rand(8, 8)  # Mock a simple 8x8 pixel image
    horizontal_slices = 2
    vertical_slices = 2

    slices = image_break_into_slices(image, horizontal_slices, vertical_slices)

    # Check if the number of slices is correct
    assert len(slices) == horizontal_slices and all(len(row) == vertical_slices for row in slices), \
        "Function did not return the correct number of slices"

def test_image_break_into_slices_invalid_input():
    # Test the function with invalid input
    image = "not a 2D list"

    with pytest.raises(TypeError):
        image_break_into_slices(image, 2, 2)

def test_break_into_slices_edge_case():
    # Test with an edge case (small image)
    image = np.random.rand(1, 1)
    slices = image_break_into_slices(image, 1, 1)
    assert len(slices) == 1 and len(slices[0]) == 1, "Incorrect handling of small image"

def test_slice_image_input_structure():
    # Test the input structure for slice_image
    mock_slices = [[[0]*4 for _ in range(2)] for _ in range(2)]
    # The actual display functionality can't be easily tested in this environment
    # So we test if the function can be called with the expected input structure
    try:
        slice_image(mock_slices)
        assert True
    except Exception as e:
        assert False, f"Function raised an exception with valid input: {e}"

def test_slice_image_subplot_titles():
    # Test if each subplot has the correct title
    mock_slices = [[[0]*4 for _ in range(2)] for _ in range(2)]
    slice_image(mock_slices)
    for i, ax in enumerate(plt.gcf().axes):
        expected_title = f"Slice {i+1}"
        assert ax.get_title() == expected_title, f"Incorrect title for subplot {i+1}"

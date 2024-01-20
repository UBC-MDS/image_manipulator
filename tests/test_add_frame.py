import numpy as np
import pytest
from image_modifier.add_frame import add_pad, make_borders_colored, add_frame 

# Sample test data
sample_image = np.zeros((200, 200, 3), dtype=np.uint8)

# Tests for add_pad

# Test to make sure the result have correct size with default parameter
def test_add_pad_with_default_border():
    result = add_pad(sample_image)
    assert result.shape == (260, 260, 3)

# Test to make sure the result have correct size with user defined parameter
def test_add_pad_with_custom_border():
    result = add_pad(sample_image, border_size=50)
    assert result.shape == (300, 300, 3)


# Tests for make_borders_colored

# Test to make sure the result have correct size with default parameters
def test_make_borders_colored_default():
    result = make_borders_colored(sample_image)
    assert result.shape == sample_image.shape

# Test to make sure user defined color can be correctly applied to all sides
def test_make_borders_colored_custom_color():
    border_size = 30
    custom_color = (128, 128, 128)
    result = make_borders_colored(sample_image, border_size, color_name=custom_color)

    assert np.all(result[:border_size, :, :] == custom_color)
    assert np.all(result[-border_size:, :, :] == custom_color)
    assert np.all(result[:, :border_size, :] == custom_color)
    assert np.all(result[:, -border_size:, :] == custom_color)

# Test to make sure undefined color would produce an error
def test_make_borders_colored_invalid_color():
    with pytest.raises(ValueError):
        make_borders_colored(sample_image, color_name="unknown_color")

# Tests for add_frame

# When overlay is True, the result image size should not change
def test_add_frame_overlay():
    result = add_frame(sample_image, overlay=True)
    assert result.shape == sample_image.shape

# When overlay is False, the result image size should increase by border_size 
def test_add_frame_no_overlay():
    result = add_frame(sample_image, overlay=False)
    assert result.shape == (260, 260, 3)

# Handle error when input image is a PNG file
def test_add_frame_invalid_image():
    with pytest.raises(ValueError):
        add_frame(np.zeros((200, 200, 4)), overlay=True)  # Assuming alpha channel not supported


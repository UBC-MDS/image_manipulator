import numpy as np
import pytest
from image_modifier.add_frame import add_pad, make_borders_colored, add_frame

# Sample test data for RGB and RGBA images
sample_image_rgb = np.zeros((200, 200, 3), dtype=np.uint8)
sample_image_rgba = np.zeros((200, 200, 4), dtype=np.uint8)  # Add an alpha channel

# Tests for add_pad

def test_add_pad_with_default_border():
    result = add_pad(sample_image_rgb)
    expected_shape = (sample_image_rgb.shape[0] + 60, sample_image_rgb.shape[1] + 60, 3)  # 30 pixels padding on each side
    assert result.shape == expected_shape

def test_add_pad_with_custom_border():
    result = add_pad(sample_image_rgb, border_size=50)
    expected_shape = (sample_image_rgb.shape[0] + 100, sample_image_rgb.shape[1] + 100, 3)  # 50 pixels padding on each side
    assert result.shape == expected_shape

# Tests for make_borders_colored

def test_make_borders_colored_default():
    result = make_borders_colored(sample_image_rgb)
    assert result.shape == sample_image_rgb.shape

def test_make_borders_colored_custom_color():
    border_size = 30
    custom_color = (128, 128, 128)
    result = make_borders_colored(sample_image_rgb, border_size, color_name=custom_color)
    # Check if the border has been correctly colored
    assert np.all(result[:border_size, :, :3] == custom_color)  # Top border check for RGB values

def test_make_borders_colored_rgba_image():
    border_size = 30
    custom_color = (128, 128, 128, 255)  # RGBA color
    result = make_borders_colored(sample_image_rgba, border_size, color_name=custom_color)
    # Check if the border has been correctly colored, including the alpha channel
    assert np.all(result[:border_size, :, :] == custom_color)  # Top border check including alpha

def test_make_borders_colored_invalid_color():
    with pytest.raises(ValueError):
        make_borders_colored(sample_image_rgb, color_name="unknown_color")

# Tests for add_frame

def test_add_frame_overlay():
    result = add_frame(sample_image_rgb, overlay=True)
    assert result.shape == sample_image_rgb.shape

def test_add_frame_no_overlay():
    result = add_frame(sample_image_rgb, overlay=False)
    expected_shape = (sample_image_rgb.shape[0] + 60, sample_image_rgb.shape[1] + 60, 3)  # 30 pixels padding on each side
    assert result.shape == expected_shape

def test_add_frame_rgba_support():
    result = add_frame(sample_image_rgba, overlay=True)
    assert result.shape == sample_image_rgba.shape  # Ensure RGBA image is processed correctly

def test_add_frame_invalid_image():
    with pytest.raises(ValueError):
        # With the added support for RGBA, so this should not raise an error for RGBA images
        add_frame(np.zeros((200, 200, 5)), overlay=True)  # Assuming 5 channels are not supported

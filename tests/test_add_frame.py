import numpy as np
import pytest
from image_modifier.add_frame import add_pad, make_borders_colored, add_frame 

sample_image = np.zeros((200, 200, 3), dtype=np.uint8)

# Tests for add_pad
def test_add_pad_with_default_border():
    result = add_pad(sample_image)
    assert result.shape == (260, 260, 3)

def test_add_pad_with_custom_border():
    result = add_pad(sample_image, border_size=50)
    assert result.shape == (300, 300, 3)

# def test_add_pad_with_large_border():
#     with pytest.raises(ValueError):
#         add_pad(sample_image, border_size=300)

# Tests for make_borders_colored
def test_make_borders_colored_default():
    result = make_borders_colored(sample_image)
    assert result.shape == sample_image.shape

def test_make_borders_colored_custom_color():
    result = make_borders_colored(sample_image, color_name=(128, 128, 128))

def test_make_borders_colored_invalid_color():
    with pytest.raises(ValueError):
        make_borders_colored(sample_image, color_name="unknown_color")

# Tests for add_frame
def test_add_frame_overlay():
    result = add_frame(sample_image, overlay=True)
    assert result.shape == sample_image.shape

def test_add_frame_no_overlay():
    result = add_frame(sample_image, overlay=False)
    assert result.shape == (260, 260, 3)

def test_add_frame_invalid_image():
    with pytest.raises(ValueError):
        add_frame(np.zeros((200, 200, 4)), overlay=True)  # Assuming alpha channel not supported


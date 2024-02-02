import numpy as np
import pytest
from image_modifier.select_channel import select_channel

# command: pytest tests/test_select_channel.py

# Create a sample image with random values in each channel
sample_image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)


def test_select_channel_with_invalid_image_shape():
    """
    Tests that the function raises a ValueError when an image with 
    an invalid shape is given.
    """
    # Test with a 4D array (invalid shape）
    invalid_image = np.zeros((100, 100, 3, 1), dtype=np.uint8)
    with pytest.raises(ValueError):
        select_channel(invalid_image, 'r', without=True)


def test_select_channel_remove_red():
    """
    Confirms that the function correctly removes the red channel from the
    image and leaves the other channels unmodified.
    """
    result = select_channel(sample_image, 'r', without=True)
    # Check if red channel is removed and other channels are not modified
    assert np.all(result[:, :, 0] == 0)
    assert np.array_equal(result[:, :, 1:], sample_image[:, :, 1:])

def test_select_channel_remove_green():
    """
    check that the function correctly removes the green channel from the   
    image and leaves the other channels unmodified.
    """
    # Check if green channel is removed and other channels are not modified
    result = select_channel(sample_image, 'g', without=True)
    assert np.all(result[:, :, 1] == 0)
    assert np.array_equal(result[:, :, [0, 2]], sample_image[:, :, [0, 2]])

def test_select_channel_remove_blue():
    """
    check that the function correctly removes the blue channel from the   
    image and leaves the other channels unmodified.
    """

    # Check if blue channel is removed and other channels are not modified
    result = select_channel(sample_image, 'b', without=True)
    assert np.all(result[:, :, 2] == 0)
    assert np.array_equal(result[:, :, :2], sample_image[:, :, :2])

def test_select_channel_isolate_red():
    """
    Ensures that when the red channel is isolated using the select_channel function,
    the red channel values are preserved and other channels are set to zero.
    """
    
    result = select_channel(sample_image, 'r', without=False)
    assert np.all(result[:, :, 0] == sample_image[:, :, 0])
    assert np.all(result[:, :, 1:] == 0)

def test_select_channel_isolate_green():
    """
    Ensures that when the green channel is isolated using the select_channel function,
    the green channel values are preserved and other channels are set to zero.
    """
    result = select_channel(sample_image, 'g', without=False)
    assert np.all(result[:, :, 1] == sample_image[:, :, 1])
    assert np.all(result[:, :, [0, 2]] == 0)

def test_select_channel_isolate_blue():
    """
    Ensures that when the blue channel is isolated using the select_channel function,
    the blue channel values are preserved and other channels are set to zero.
    """
    
    result = select_channel(sample_image, 'b', without=False)
    assert np.all(result[:, :, 2] == sample_image[:, :, 2])
    assert np.all(result[:, :, :2] == 0)

def test_select_channel_invalid_channel():
    """
    Tests that a ValueError is raised when an invalid channel key is provided
    to the select_channel function.
    """
    
    with pytest.raises(ValueError):
        select_channel(sample_image, 'x', without=True)

def test_select_channel_non_numpy_input():
    """
    Checks that the select_channel function raises a TypeError when the input
    is not a NumPy array.
    """
    with pytest.raises(TypeError):
        select_channel([[0, 0, 0]], 'r', without=True)

def test_select_channel_all_channels_removed():
    """
    Tests the select_channel function's ability to remove all channels, resulting
    in a completely black image.
    """
    result = select_channel(sample_image, 'r', without=True)
    result = select_channel(result, 'g', without=True)
    result = select_channel(result, 'b', without=True)
    assert np.all(result == 0)


def test_select_channel_preserve_values():
    """
    Ensures that the select_channel function preserves the distinct values of each
    channel when isolating a specific channel.
    """
    # Create an image with distinct values for each channel
    test_image = np.zeros((100, 100, 3), dtype=np.uint8)
    test_image[:, :, 0] = 50  # Red channel
    test_image[:, :, 1] = 100  # Green channel
    test_image[:, :, 2] = 150  # Blue channel

    # Isolate the red channel and check if the values are preserved
    red_isolated = select_channel(test_image, 'r', without=False)
    assert np.all(red_isolated[:, :, 0] == 50)
    assert np.all(red_isolated[:, :, 1] == 0)
    assert np.all(red_isolated[:, :, 2] == 0)
def rotate_90(image):
    """
    Rotate a 2D image represented as a list of lists by 90 degrees clockwise.

    Parameters:
        image (list of lists): A 2D list representing the original image.

    Returns:
        list of lists: A new 2D list representing the rotated image.

    Example:
    >>> original_image = [
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... ]
    >>> rotated_image = rotate_90(original_image)
    >>> print(rotated_image)
    [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]

    """

def select_channel(path, channel, without=False):
    """
    Displays an image with/without a specified RGB channel modification and saves the processed image.

    Parameters:
    - path (str): Path to the image file.
    - channel (str): The color channel to interact with. Valid options are 'r' for red, 'g' for green, or 'b' for blue.
    - without (bool, optional): If True, removes the specified channel from the image before saving.
      Defaults to False.

    Returns:
    - None: The function displays the modified image using matplotlib and saves the modified image to a new file.

    The function reads an image from the given path, processes it based on the specified channel, 
    and displays the modified image. It also saves this modified image in the same directory as 
    the original, with the suffix '_modified'.

    Example:
    To display and save an image with green channel selected:
    >>> select_channel('path_to_image.jpg', 'g', without=False)
    
    To display and save an image with the red channel removed:
    >>> select_channel('path_to_image.jpg', 'r', without=True)

    """

def slice_image(image, horizontal_slices, vertical_slices):
    """
    Slices a 2D list representing an image into a specified number of horizontal and vertical slices.

    Parameters:
    image (list of list): A 2D list representing the original image.
    horizontal_slices (int): The number of horizontal slices to divide the image into.
    vertical_slices (int): The number of vertical slices to divide the image into.

    Returns:
    list of list of list: A 3D list representing the sliced image. 
    Each element in the outer list represents a row of slices,
    and each slice is represented as a 2D list of pixel data.

    Example:
    --------
    Given a 2D list representing an image with 8x8 pixels:
    
    >>> slices = slice_image(image, 2, 2)
    
    This will return a 3D list which contains four 'slices', each being a 2D list representing a 4x4 pixel area.
    """
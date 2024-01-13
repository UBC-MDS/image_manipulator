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

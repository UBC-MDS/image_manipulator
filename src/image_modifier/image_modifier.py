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

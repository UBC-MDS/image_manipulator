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

def select_channel(image, channel, without=False):
    """
    Modify an image with/without a specified RGB channel.

    Parameters:
    - image (list of lists): A 2D list representing the original image.
    - channel (str): The color channel to interact with. Valid options are 'r' for red, 'g' for green, or 'b' for blue.
    - without (bool, optional): If True, removes the specified channel from the image. Defaults to False.

    Returns:
    - list of lists: A new 2D list representing the image with the modified channel.

    The function processes an image based on the specified channel, 
    and displays the modified image. 

    Example:
    To modify an image with green channel selected:
    >>> select_channel('path_to_image.jpg', 'g', without=False)
    
    To modify an image with the red channel removed:
    >>> select_channel(image, 'r', without=True)

    """

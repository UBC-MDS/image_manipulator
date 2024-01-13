def add_frame(image, frame_width=20, frame_color='black'):
    """
    Adds a frame to an image loaded from a specified path and returns a modified image as a numpy.ndarray.

    This function uses matplotlib's imread function to load an image from the given file path. It then 
    applies a frame around the image with customizable width and color. The modified image is returned 
    as a numpy.ndarray, which can be displayed using matplotlib.

    Parameters:
    image_path (numpy.ndarray): An image array in the form of numpy.ndarray, suitable for display with matplotlib.
    frame_width (int, optional): The width of the frame to be added around the image. 
                                 The width is applied equally on all sides of the image. 
                                 Defaults to 20.
    frame_color (str, optional): The color of the frame. Colors can be specified in formats
                                 accepted by matplotlib (e.g., color name, RGB, or RGBA tuple).
                                 Defaults to 'black'.

    Returns:
    numpy.ndarray: A new image array with the frame applied, suitable for display with matplotlib.

    Example:
    >>> import matplotlib.pyplot as plt
    >>> framed_image = add_frame(image, frame_width=30, frame_color='blue')
    >>> plt.imshow(framed_image)
    >>> plt.show()
    """

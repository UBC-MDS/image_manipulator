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
    >>> rotated_image = rotate_image_90_degrees(original_image)
    >>> print(rotated_image)
    [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]

    """
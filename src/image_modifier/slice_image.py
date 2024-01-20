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
    # Calculate the height and width of the image
    image_height = len(image)
    image_width = len(image[0]) if image_height > 0 else 0

    # Adjust slice numbers if they exceed image dimensions
    horizontal_slices = min(horizontal_slices, image_height)
    vertical_slices = min(vertical_slices, image_width)

    # Calculate the height and width of each slice
    slice_height = max(1, image_height // horizontal_slices)
    slice_width = max(1, image_width // vertical_slices)

    # Create a 2D list to hold the image slices
    slices = []

    # Slice the image and add each slice to the list
    for h in range(horizontal_slices):
        row = []
        for v in range(vertical_slices):
            # Calculate the coordinates of the slice
            top = h * slice_height
            bottom = min((h + 1) * slice_height, image_height)
            left = v * slice_width
            right = min((v + 1) * slice_width, image_width)

            # Create the slice as a 2D list
            slice = [row[left:right] for row in image[top:bottom]]
            row.append(slice)
        slices.append(row)

    return slices
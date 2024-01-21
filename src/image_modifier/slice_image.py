import numpy as np
import matplotlib.pyplot as plt

def image_break_into_slices(image, horizontal_slices, vertical_slices):
    """
    Slices an image into a specified number of horizontal and vertical slices.

    Parameters:
    image (list of list): A jpeg image.
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
    # Convert the input image into a 2D list
    image = np.array(image)

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
    
def slice_image(image, horizontal_slices=2, vertical_slices=2):
    """
    Display a grid of image slices in a matplotlib subplot.

    This function takes a nested list of image slices (where each slice is a 2D array-like structure) 
    and displays each slice in a grid format using matplotlib. The grid dimensions are determined 
    by the number of rows and columns in the nested list.

    Parameters:
    slices (list of list): A nested list where each inner list represents a row of image slices, 
    and each slice is a 2D list or array-like structure containing pixel data.

    The function first flattens the nested list for processing, then sets up a matplotlib subplot 
    grid with dimensions equal to the number of rows and columns in the input nested list. Each 
    subplot displays an individual image slice with a title indicating its position in the sequence. 
    Axes are turned off for better visualization.

    Note: This function assumes that the input 'slices' is a rectangular grid (i.e., each row contains 
    the same number of slices).

    Returns:
    None; the function directly displays the plot using matplotlib.
    """
    slices = image_break_into_slices(image, horizontal_slices, vertical_slices)

    # Set up the plot dimensions
    n_rows = len(slices)
    n_cols = len(slices[0])
    fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols)

    if n_rows == 1 or n_cols == 1:
        axes = np.array(axes).reshape(n_rows, n_cols)

    # Display each slice
    for i in range(n_rows):
        for j in range(n_cols):
            ax = axes[i, j]
            ax.imshow(slices[i][j])
            ax.set_title(f"Slice {i*n_cols + j + 1}")
            ax.axis('off')

    plt.tight_layout()
    plt.show()
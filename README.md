# ImageModifier

[![](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/UBC-MDS/image_modifier.svg)](https://github.com/UBC-MDS/image_modifier/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/UBC-MDS/image_modifier.svg)](https://github.com/UBC-MDS/image_modifier/commits/main)
[![GitHub release](https://img.shields.io/github/release/UBC-MDS/image_modifier.svg)](https://github.com/UBC-MDS/image_modifier/releases)

![Created by DALL·E](src/logo.png)

*Created by DALL.E*

ImageModifier is a Python package dedicated to providing an intuitive and efficient way to manipulate images. This package focuses on core image processing functions, allowing users to easily modify images through operations like rotating, slicing, adding frame, and adjusting RGB channels. The primary goal is to offer a straightforward way for basic yet powerful image transformations, making it a useful tool for image processing.

## Contributors

Chun Li, Celeste Zhao, He Ma, Karan Khubdikar

## Motivation

ImageModifier offers a streamlined and intuitive approach, making it highly accessible to a wide range of users, unlike many complex image processing tools that can be overwhelming for beginners and cumbersome for quick tasks. This package caters to both novices seeking an easy entry point into image manipulation and experienced users looking for a tool to perform quick modifications without the overhead of more complex software. With core functionalities like rotating, slicing, adding frames, and selecting RGB channels, ImageModifier simplifies these common tasks, allowing users to achieve their goals with minimal coding effort.

## Functions

**rotate_90**: Rotate a 2D image represented as a list of lists by 90 degrees clockwise.

**add_frame**: Adds a frame to an image loaded from a specified path and returns a modified image as a numpy.ndarray.

**slice_image**: Slices a 2D list representing an image into a specified number of horizontal and vertical slices.

**select_channel**: Modify an image with/without a specified RGB channel.

## Installation

```bash
$ pip install image_modifier
```

## Usage

**Importing Image**
The following code can be used to import an image.
```bash
from PIL import Image
image = Image.open(image_path)
```
image_modifier can be used to modify the image (rotate_90/slice/add_frame/select_channel). Following is an example of how the package can be imported and the functions can be used considering add_frame function as an example:

```bash
from image_modifier.add_frame import add_frame

framed_image = add_frame(image, frame_width=30, frame_color='blue')
plt.imshow(framed_image)
plt.show()
```

## Contributing

Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`image_modifier` was created by Karan Khubdikar, Celeste Zhao, He Ma, Chun Li. It is licensed under the terms of the MIT license, and more details can be found in the [LICENSE](LICENSE).

## Credits

`image_modifier` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

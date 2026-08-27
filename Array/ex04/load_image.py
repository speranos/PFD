import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from a file and return it as a numpy array.
    """
    img = Image.open(path)
    img_array = np.array(img)

    height, width, c = img_array.shape
    x_start = (width - 400) // 2
    y_start = (height - 400) // 2

    zoom = img_array[y_start:y_start + 400, x_start:x_start + 400, 1]
    print("The shape of the image is: ", zoom.shape)
    print(zoom)
    return zoom

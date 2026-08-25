import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from a file and return it as a numpy array.
    """
    img = Image.open(path)
    img_array = np.array(img)
    print("The shape of the image is: ", img_array.shape)
    print(img_array)
    return img_array

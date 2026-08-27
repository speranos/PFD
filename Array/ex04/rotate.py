import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def _ft_transpose(pic: np.ndarray) -> np.ndarray:
    """
    Transpose the image array manually.
    """
    height, width = pic.shape
    transposed = np.zeros((width, height), dtype=pic.dtype)
    for i in range(height):
        for j in range(width):
            transposed[j, i] = pic[i, j]
    return transposed


def ft_rotate(pic: np.ndarray) -> np.ndarray:
    rt = _ft_transpose(pic)
    print("New shape after Transpose: ", rt.shape)
    print(rt)
    plt.imshow(rt, cmap='gray')
    plt.show()
    return rt


def main():
    try:
        image_array = ft_load("animal.jpeg")
        ft_rotate(image_array)
    except Exception as e:
        print("Error loading image:", e)


if __name__ == "__main__":
    main()

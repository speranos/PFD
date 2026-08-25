import matplotlib.pyplot as plt
from load_image import ft_load
import numpy as np


def ft_zoom(pic: np.ndarray):
    "Zoom into the center of the image."

    height, width = pic.shape
    start_y = (height - 400) // 2
    start_x = (width - 400) // 2

    zoomed = pic[start_y:start_y + 400, start_x:start_x + 400]
    print("New shape after slicing: ", zoomed.shape)
    print(zoomed)

    plt.imshow(zoomed, cmap='gray')
    plt.show()
    return zoomed


def main():
    try:
        image_array = ft_load("animal.jpeg")
        ft_zoom(image_array)
    except Exception as e:
        print("Error loading image:", e)


if __name__ == "__main__":
    main()

import numpy as np
from PIL import Image
from pathlib import Path


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its shape
    """
    p = Path(path)
    supported = {".jpg", ".jpeg"}
    if p.suffix not in supported:
        raise ValueError('unsupported extension')
    img = Image.open(path)
    img_array = np.array(img)
    print("The shape of the image is: ", img_array.shape)
    print(img_array)
    return img_array


def main():
    try:
        ft_load("landscape.jpg")
    except Exception as e:
        print("Error loading image:", e)


if __name__ == "__main__":
    main()

import numpy as np
from PIL import Image


# dive into pillow + test def use cases 
# + error handling + handling file extensions
def ft_load(path: str) -> np.ndarray:
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

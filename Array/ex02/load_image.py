import numpy as np
from PIL import Image


#dive into pillow + test def use cases + error handling + handling file extensions
def ft_load(path: str) -> np.ndarray:
    img = Image.open(path)
    return np.array(img)






def main():
    img_array = ft_load("landscape.jpg")
    print("The shape of the image is: ", img_array.shape)
    print(img_array)

if __name__ == "__main__":
    main()
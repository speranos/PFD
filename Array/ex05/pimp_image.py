from array import array
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_green(array) -> array:
    """
    Set the red and blue channels to 0, keeping only the green channel.
    """
    cp = array.copy()
    cp[:, :, 0] = 0  # Set red channel to 0
    cp[:, :, 2] = 0  # Set blue channel to 0
    plt.imshow(cp)
    plt.show()
    return cp


def ft_red(array) -> array:
    """
    Set the green and blue channels to 0, keeping only the red channel.
    """
    cp = array.copy()
    cp[:, :, 1] = 0  # Set green channel to 0
    cp[:, :, 2] = 0  # Set blue channel to 0
    plt.imshow(cp)
    plt.show()
    return cp


def ft_blue(array) -> array:
    """
    Set the red and green channels to 0, keeping only the blue channel.
    """
    cp = array.copy()
    cp[:, :, 0] = 0  # Set red channel to 0
    cp[:, :, 1] = 0  # Set green channel to 0
    print("New shape:", cp.shape)
    print(cp)
    plt.imshow(cp)
    plt.show()
    return cp


def ft_invert(array) -> array:
    """
    Invert the colors of the image.
    """
    cp = array.copy()
    cp = 255 - cp  # Invert colors
    plt.imshow(cp)
    plt.show()
    return cp


def ft_grey(array) -> array:
    """
    Convert the image to greyscale.
    """
    cp = array.copy()
    t = cp.sum(axis=2)  # Sum of RGB channels
    cp = t // 3
    plt.imshow(cp, cmap='gray')
    plt.show()
    return cp


def main():
    pic = ft_load("landscape.jpg")
    ft_red(pic)
    ft_green(pic)
    ft_blue(pic)
    ft_invert(pic)
    ft_grey(pic)


if __name__ == "__main__":
    main()

import numpy as np
from load_image import load_image
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    return 255 - array


def ft_red(array) -> np.ndarray:
    """
    Change the color of the image received in red.
    """
    red = array.copy()
    for i in range(len(red)):
        for j in range(len(red[i])):
            red[i][j][1] = 0
            red[i][j][2] = 0
    return red


def ft_green(array) -> np.ndarray:
    """
    Change the color of the image received in green.
    """
    green = array.copy()
    for i in range(len(green)):
        for j in range(len(green[i])):
            green[i][j][0] = 0
            green[i][j][2] = 0
    return green


def ft_blue(array) -> np.ndarray:
    """
    Change the color of the image received in blue.
    """
    blue = array.copy()
    for i in range(len(blue)):
        for j in range(len(blue[i])):
            blue[i][j][0] = 0
            blue[i][j][1] = 0
    return blue


def ft_grey(array) -> np.ndarray:
    """
    Change the color of the image received in grey.
    """
    grey = array.copy()
    for i in range(len(grey)):
        for j in range(len(grey[i])):
            R, V, B = array[i, j, :3]
            grey_value = R * 0.299 + V * 0.587 + B * 0.114
            grey[i, j] = np.clip(grey_value, 0, 255)
    return grey


def main():
    """
    Main function to demonstrate image manipulation.
    """
    try:
        image = load_image("landscape.jpg")
        ft_invert(image)
        ft_red(image)
        ft_green(image)
        ft_blue(image)
        ft_grey(image)
        print(ft_invert.__doc__)

    except FileNotFoundError:
        print("Error: The specified image file was not found.")

    else:
        image = ft_invert(image)

        image = np.squeeze(image)

        plt.imshow(image, cmap='gray')
        plt.axis('off')
        plt.show()


if __name__ == "__main__":
    main()

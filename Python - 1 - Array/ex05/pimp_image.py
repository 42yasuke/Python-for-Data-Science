import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    invert_img = 255 - array
    display_image(invert_img, "Invert")
    return invert_img


def ft_red(array) -> np.ndarray:
    """
    Change the color of the image received in red.
    """
    red = array.copy()
    red[:, :, 1] = 0  # Met le vert à 0
    red[:, :, 2] = 0  # Met le bleu à 0
    display_image(red, "Red")
    return red


def ft_green(array) -> np.ndarray:
    """
    Change the color of the image received in green.
    """
    green = array.copy()
    green[:, :, 0] = 0  # Met le rouge à 0
    green[:, :, 2] = 0  # Met le bleu à 0
    display_image(green, "Green")
    return green


def ft_blue(array) -> np.ndarray:
    """
    Change the color of the image received in blue.
    """
    blue = array.copy()
    blue[:, :, 0] = 0  # Met le rouge à 0
    blue[:, :, 1] = 0  # Met le vert à 0
    display_image(blue, "Blue")
    return blue


def ft_grey(array) -> np.ndarray:
    """
    Change the color of the image received in grey.
    """
    # Formule de luminance
    grey = np.dot(array[..., :3], [0.299, 0.587, 0.114])
    grey = np.clip(grey, 0, 255).astype(np.uint8)
    # Pour garder 3 canaux (R=G=B)
    grey = np.stack([grey, grey, grey], axis=2)
    display_image(grey, "Grey")
    return grey


def display_image(img, title):
    """
    Display the image using matplotlib with a title.
    """
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')
    plt.show()


def main():
    """
    Main function to demonstrate image manipulation.
    """
    try:
        array = ft_load("landscape.jpg")
    except Exception as e:
        print(f"Error: {e}")
        return

    # Appliquer et afficher chaque filtre
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)

    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()

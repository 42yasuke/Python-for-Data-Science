from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def trim(array, x, y, width, height, depth=3):
    return array[y:y+height, x:x+width, :depth]


def transpose(array):
    """
    Transpose a 2D array (swap rows and columns)
    """
    rows, cols = array.shape[0], array.shape[1]
    result = np.zeros((cols, rows), dtype=array.dtype)
    for i in range(rows):
        for j in range(cols):
            result[j, i] = array[i, j]
    return result


def main():
    """
    Open the image, trim it, convert to grayscale,
    then transpose and display it.
    """
    try:
        image = ft_load('animal.jpeg')
    except Exception as e:
        print(e)
        return

    # Trim (découper un carré)
    image = trim(image, 450, 100, 400, 400, 1)

    print(f'The shape of the image is: {image.shape}', end='')
    print(f' or ({image.shape[0]}, {image.shape[1]})')
    print(image)

    # Supprimer la dimension inutile
    image = np.squeeze(image)

    # Transposer (rotation)
    image = transpose(image)

    print(f'New shape after Transpose: {image.shape}')
    print(image)

    # Afficher
    plt.imshow(image, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()

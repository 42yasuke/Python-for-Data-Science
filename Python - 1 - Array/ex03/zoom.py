from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def trim(array, x, y, width, height, depth=3):
    """
    Trim an array using the given parameters
    """
    return array[y:y + height, x:x + width, :depth]


def main():
    """
    Open the image, trim it and convert it to grayscale,
    then display it.
    """
    try:
        image = ft_load('animal.jpeg')
    except Exception as e:
        print(e)
        return

    print("Original shape:", image.shape)
    print(image)

    # Trim et conversion en niveaux de rouge (on garde que le canal rouge)
    image = trim(image, 450, 100, 400, 400, 1)

    print(f"New shape after slicing: {image.shape}", end='')
    print(f" or ({image.shape[0]}, {image.shape[1]})")

    # passage de (400,400,1) à (400,400) necessaire pour plt.imshow
    image = np.squeeze(image)

    print(image)

    # Affichage
    plt.imshow(image, cmap='gray')  # Affichage en niveaux de gris
    plt.show()


if __name__ == "__main__":
    main()

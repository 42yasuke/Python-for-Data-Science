from load_image import load_image
import numpy as np
import matplotlib.pyplot as plt


def trim(array, x, y, width, height, depth=3):
    return array[y:y+width, x:x+height, :depth]


def transpose(array):
    """
        Transpose an array
    """
    rows, cols = array.shape[0], array.shape[1]
    result = np.zeros((cols, rows), dtype=array.dtype)
    for i in range(rows):
        for j in range(cols):
            result[j, i] = array[i, j]
    return result


def main():
    """
    Open the image, trim it and convert it to grayscale,
    then transpose and display it.
    """
    try:
        image = load_image('animal.jpeg')
    except Exception as e:
        print(e)
        exit()

    image = trim(image, 450, 100, 400, 400, 1)

    print(f'The shape of the image is: {image.shape}', end='')
    print(f' or ({image.shape[0]}, {image.shape[1]})')
    print(image)

    image = transpose(image)

    image = np.squeeze(image)

    print(f'New shape after Transpose: {image.shape}')
    print(image)

    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()

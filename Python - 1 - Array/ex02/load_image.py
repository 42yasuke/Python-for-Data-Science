import numpy as np
from PIL import Image


def ft_load(path: str):
    """
    Load an image, print its format and pixel content in RGB format.

    Parameters:
    path (str): The file path to the image.

    Returns:
    np.ndarray: The image represented as a NumPy array.
    """
    if not (path.lower().endswith('.jpg') or path.lower().endswith('.jpeg')):
        raise ValueError("Error: Only JPG and JPEG formats are supported")

    try:
        img = Image.open(path)
        img = img.convert('RGB')
        img_array = np.array(img)

        print(f"The shape of image is: {img_array.shape}")

        return img_array

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file '{path}' was not found")
    except Exception as e:
        raise Exception(f"Error: Unable to load image - {str(e)}")


def main():
    """
    Main function to demonstrate loading an image.
    """
    try:
        print(ft_load("landscape.jpg"))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

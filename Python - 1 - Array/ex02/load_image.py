import numpy as np
from PIL import Image


def load_image(image_path):
	"""
	Load an image from the specified file path and convert it to a NumPy array.

	Parameters:
	image_path (str): The file path to the image.

	Returns:
	np.ndarray: The image represented as a NumPy array.
	"""
	img = Image.open(image_path)
	img_array = np.array(img)
	print("The shape of image is: ", img_array.shape)
	return img_array


def main():
	"""
	Main function to demonstrate loading an image.
	"""
	try:
		print(load_image("landscape.jpg"))
	except FileNotFoundError:
		print("Error: The specified image file was not found.")


if __name__ == "__main__":
	main()

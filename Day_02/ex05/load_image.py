from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """
    Loads an image and returns its pixel data as a NumPy array.
    Prints the format and size of the image.
    """
    try:
        # Load the image
        image = Image.open(path)
        image = image.convert("RGB")  # Ensure image is in RGB mode

        # Convert to NumPy array
        pixels = np.array(image)

        # Print image info
        print(f"The shape of image is: {pixels.shape}")  # Shape: (height, width, channels)

        return pixels

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

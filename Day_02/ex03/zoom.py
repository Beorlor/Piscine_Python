import matplotlib.pyplot as plt
from load_image import ft_load
import numpy as np


# Need to be able to zoom anywhere in the image, not just the center
def zoom_image(pixels: np.ndarray, zoom_width: int, zoom_height: int):
    """
    Zooms into the center of the image, converts it to grayscale,
    and displays it.
    """
    try:
        # Calculate the center of the image
        height, width, _ = pixels.shape
        center_x, center_y = width // 2, height // 2

        # Calculate slicing coordinates
        x_start = center_x - zoom_width // 2
        x_end = center_x + zoom_width // 2
        y_start = center_y - zoom_height // 2
        y_end = center_y + zoom_height // 2

        # Slice the image to zoom in
        zoomed = pixels[y_start:y_end, x_start:x_end]

        # Rotate the image 90 degrees counter-clockwise

        # Convert to grayscale
        grayscale = zoomed.mean(axis=2).astype(np.uint8)

        # Display the grayscale image
        plt.imshow(grayscale, cmap='gray')
        plt.axis('on')
        plt.title("Zoomed Grayscale Image")
        plt.show()

        print(f"New shape after slicing: {grayscale.shape}")
        print(grayscale)

    except Exception as e:
        print(f"Error: {e}")


def main():
    # Load the image
    image_path = "animal.jpeg"
    pixels = ft_load(image_path)

    if pixels is not None:
        zoom_image(pixels, zoom_width=400, zoom_height=400)


if __name__ == "__main__":
    main()

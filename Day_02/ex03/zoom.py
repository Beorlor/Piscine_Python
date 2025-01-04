import matplotlib.pyplot as plt
from load_image import ft_load

def zoom_image(pixels: np.ndarray, x_start: int, x_end: int, y_start: int, y_end: int):
    """
    Zooms into the image by slicing it and displays the result.
    """
    try:
        # Slicing the image to zoom in
        zoomed_pixels = pixels[y_start:y_end, x_start:x_end, :]  # Slicing rows and columns

        # Print new shape
        print(f"New shape after slicing: {zoomed_pixels.shape}")

        # Display the image
        plt.imshow(zoomed_pixels)
        plt.axis('on')  # Show x and y axis
        plt.show()

    except Exception as e:
        print(f"An error occurred while zooming: {e}")

def main():
    # Load the image
    image_path = "animal.jpeg"
    pixels = ft_load(image_path)

    if pixels is not None:
        # Zoom into the image
        zoom_image(pixels, x_start=100, x_end=500, y_start=100, y_end=500)

if __name__ == "__main__":
    main()

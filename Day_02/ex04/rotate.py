from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def transpose_image(array):
    """
    Transposes the input image array manually
    (rows become columns and vice versa).
    """
    # Validate input array dimensions
    if len(array.shape) < 2:
        raise ValueError("Input array must be at least 2D for transposing.")

    # Manual transpose: switch rows and columns
    height, width, channels = array.shape
    transposed = np.zeros((width, height, channels), dtype=array.dtype)

    for y in range(height):
        for x in range(width):
            transposed[x, y] = array[y, x]

    return transposed


def main():
    try:
        # Load the image
        image_path = "animal.jpeg"
        pixels = ft_load(image_path)

        if pixels is not None:
            # Extract a square part of the image (e.g., top-left 400x400
            # pixels)
            square_part = pixels[:400, :400, :]

            # Print the shape before transpose
            print(f"The shape of the image is: {square_part.shape}")
            print(square_part)

            # Perform the manual transpose
            transposed_image = transpose_image(square_part)

            # Print the new shape after the transpose
            print(f"New shape after Transpose: {transposed_image.shape}")
            print(transposed_image)

            # Display the transposed image
            plt.imshow(transposed_image.astype("uint8"))
            plt.axis("on")
            plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

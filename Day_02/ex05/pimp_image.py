def ft_invert(array):
    """
    Inverts the colors of the image by subtracting each RGB value from 255.
    """
    return 255 - array


def ft_red(array):
    """
    Keeps only the red channel of the image by setting green and blue to 0.
    """
    red_image = array.copy()
    red_image[:, :, 1] = 0  # Set green channel to 0
    red_image[:, :, 2] = 0  # Set blue channel to 0
    return red_image


def ft_green(array):
    """
    Keeps only the green channel of the image by setting red and blue to 0.
    """
    green_image = array.copy()
    green_image[:, :, 0] = 0  # Set red channel to 0
    green_image[:, :, 2] = 0  # Set blue channel to 0
    return green_image


def ft_blue(array):
    """
    Keeps only the blue channel of the image by setting red and green to 0.
    """
    blue_image = array.copy()
    blue_image[:, :, 0] = 0  # Set red channel to 0
    blue_image[:, :, 1] = 0  # Set green channel to 0
    return blue_image


def ft_grey(array):
    """
    Converts the image to grayscale using the average of the RGB channels.
    """
    grey_image = array.copy()
    grey_values = (grey_image[:, :, 0] + grey_image[:, :, 1] + grey_image[:, :, 2]) // 3
    grey_image[:, :, 0] = grey_values  # Set red channel to grey
    grey_image[:, :, 1] = grey_values  # Set green channel to grey
    grey_image[:, :, 2] = grey_values  # Set blue channel to grey
    return grey_image

def main():
    try:
        # Load the image
        image_path = "landscape.jpg"
        pixels = ft_load(image_path)

        if pixels is not None:
            # Apply filters and display results
            filters = {
                "Original": pixels,
                "Inverted": ft_invert(pixels),
                "Red": ft_red(pixels),
                "Green": ft_green(pixels),
                "Blue": ft_blue(pixels),
                "Grey": ft_grey(pixels),
            }

            for name, filtered_image in filters.items():
                plt.imshow(filtered_image.astype("uint8"))
                plt.title(name)
                plt.axis("off")
                plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
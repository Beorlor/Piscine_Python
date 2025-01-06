'''
vanilla
lst = [1, 2, 3, 4, 5]
result = [x * 2 for x in lst]
print(result)  # [2, 4, 6, 8, 10]

vs numpy
arr = np.array([1, 2, 3, 4, 5])
result = arr * 2
print(result)  # [ 2  4  6  8 10]
'''

from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Charge une image, affiche son format et son contenu en pixels RGB.
    Gère au moins les formats JPG et JPEG.
    """
    try:
        # Ouvrir l'image avec PIL
        image = Image.open(path)

        # Vérifier le format
        if image.format not in ["JPEG", "JPG"]:
            raise ValueError(
                "Unsupported image format. Only JPG and JPEG are supported.")

        # Conversion en RGB si nécessaire
        image = image.convert("RGB")

        # Transformation en tableau numpy
        pixels = np.array(image)

        # Afficher les dimensions
        print(f"The shape of image is: {pixels.shape}")
        print(pixels)

        return pixels

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")


def main():
    # Test avec une image JPG ou JPEG
    try:
        image_path = "landscape.jpg"
        ft_load(image_path)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

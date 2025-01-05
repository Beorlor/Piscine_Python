import pandas as pd

def load(path: str) -> pd.DataFrame or None:
    """
    Load a dataset from the given path, print its dimensions,
    and return the dataset as a pandas DataFrame.
    
    :param path: Path to the CSV file
    :return: DataFrame if successful, None otherwise
    """
    try:
        # Chargement du fichier CSV
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except FileNotFoundError:
        print(f"Error: File not found at path '{path}'")
        return None
    except pd.errors.ParserError:
        print("Error: Failed to parse the CSV file.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    print(load("life_expectancy_years.csv"))

if __name__ == "__main__":
    main()
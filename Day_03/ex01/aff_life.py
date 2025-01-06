import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def plot_life_expectancy(dataset: pd.DataFrame, country: str) -> None:
    """
    Plot life expectancy data for a specific country.

    :param dataset: The dataset as a pandas DataFrame.
    :param country: The name of the country to plot.
    """
    try:
        # Ensure the country exists in the dataset
        if country not in dataset['country'].values:
            print(f"Error: {country} is not in the dataset.")
            return

        # Extract data for the given country
        country_data = dataset[dataset['country'] == country].iloc[0]
        years = dataset.columns[1:].astype(int)  # Year columns to integers
        life_expectancy = country_data.iloc[1:].values

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(years, life_expectancy, label=country)
        plt.title(f"{country} Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.legend()
        plt.grid(False)
        plt.show()
    except KeyError as e:
        print(f"Key error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to load the dataset and plot life expectancy data.
    """
    # Path to the dataset file
    dataset_path = "life_expectancy_years.csv"

    # Load the dataset
    dataset = load(dataset_path)
    if dataset is None:
        print("Failed to load dataset.")
        return

    # Specify the country (replace 'France' with the country of your campus)
    country = "France"

    # Plot the life expectancy data for the given country
    plot_life_expectancy(dataset, country)


if __name__ == "__main__":
    main()

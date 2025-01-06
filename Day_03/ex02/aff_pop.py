import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
from matplotlib.ticker import FixedLocator, FuncFormatter



def clean_population_data(dataset: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the population data by removing letter suffixes (M, k, B) and converting to numeric.

    :param dataset: The dataset as a pandas DataFrame.
    :return: Cleaned dataset with numeric population values.
    """
    for column in dataset.columns[1:]:
        dataset[column] = dataset[column].apply(
            lambda x: 
            float(x.replace('M', '')) * 1e6 if 'M' in str(x) else
            float(x.replace('k', '')) * 1e3 if 'k' in str(x) else
            float(x.replace('B', '')) * 1e9 if 'B' in str(x) else
            float(x) if str(x).replace('.', '', 1).isdigit() else
            None
        )
    return dataset


def plot_population_comparison(dataset: pd.DataFrame, country1: str, country2: str) -> None:
    """
    Plot population data for two specific countries.

    :param dataset: The dataset as a pandas DataFrame.
    :param country1: The name of the first country to plot.
    :param country2: The name of the second country to plot.
    """
    try:
        # Ensure both countries exist in the dataset
        if country1 not in dataset['country'].values or country2 not in dataset['country'].values:
            print(f"Error: One or both countries are not in the dataset.")
            return

        # Extract data for each country
        country1_data = dataset[dataset['country'] == country1].iloc[0]
        country2_data = dataset[dataset['country'] == country2].iloc[0]

        # Extract years and population data
        years = dataset.columns[1:].astype(int)  # Convert year columns to integers
        population1 = country1_data.iloc[1:].values
        population2 = country2_data.iloc[1:].values

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(years, population1, label=country1)
        plt.plot(years, population2, label=country2)
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")

       # Format the y-axis to show population in millions
        plt.gca().yaxis.set_major_locator(FixedLocator([20e6, 40e6, 60e6]))
        plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x / 1e6)}M"))


        plt.legend(loc="lower right")
        plt.grid(False)
        plt.show()
    except KeyError as e:
        print(f"Key error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to load the dataset and plot population comparison.
    """
    # Path to the dataset file
    dataset_path = "population_total.csv"

    # Load the dataset
    dataset = load(dataset_path)
    if dataset is None:
        print("Failed to load dataset.")
        return

    # Clean the population data
    dataset = clean_population_data(dataset)

    # Specify the countries for comparison
    country1 = "France"
    country2 = "Belgium" # "Gabon"

    # Plot the population data for the two countries
    plot_population_comparison(dataset, country1, country2)


if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def prepare_data(income_path: str, life_expectancy_path: str, year: int) -> pd.DataFrame:
    """
    Load and merge the income and life expectancy data for a given year.

    :param income_path: Path to the income dataset CSV.
    :param life_expectancy_path: Path to the life expectancy dataset CSV.
    :param year: The year for which to filter the data.
    :return: A merged DataFrame with income and life expectancy data for the specified year.
    """
    # Load the datasets
    income_data = load(income_path)
    life_expectancy_data = load(life_expectancy_path)

    if income_data is None or life_expectancy_data is None:
        print("Error loading datasets.")
        return None

    # Ensure the year exists in both datasets
    year_str = str(year)
    if year_str not in income_data.columns or year_str not in life_expectancy_data.columns:
        print(f"Error: Year {year} not found in one or both datasets.")
        return None

    # Select relevant columns and merge datasets
    income_data = income_data[['country', year_str]]
    life_expectancy_data = life_expectancy_data[['country', year_str]]
    merged_data = pd.merge(
        income_data, life_expectancy_data, on="country", suffixes=('_income', '_life')
    )

    # Rename columns for clarity
    merged_data.columns = ['country', 'income', 'life_expectancy']

    # Drop rows with missing or invalid data
    merged_data.dropna(inplace=True)

    # Convert columns to numeric
    merged_data['income'] = pd.to_numeric(merged_data['income'], errors='coerce')
    merged_data['life_expectancy'] = pd.to_numeric(merged_data['life_expectancy'], errors='coerce')

    return merged_data.dropna()


def plot_projection(data: pd.DataFrame, year: int) -> None:
    """
    Plot the projection of life expectancy versus GDP for a given year.

    :param data: The merged DataFrame containing income and life expectancy data.
    :param year: The year for which the projection is being plotted.
    """
    if data is None or data.empty:
        print("Error: No data to plot.")
        return

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.scatter(data['income'], data['life_expectancy'], alpha=1)
    plt.title(f"{year}")
    plt.xlabel("Gross Domestic Product (GDP)")
    plt.ylabel("Life Expectancy")
    plt.xscale('log')  # Use logarithmic scale for GDP
    plt.grid(False)

    # Set the ticks for the x-axis
    ticks = [300, 1000, 10000]  # Example of specific tick values
    tick_labels = ['300', '1k', '10k']  # Corresponding labels
    plt.xticks(ticks, tick_labels)

    plt.show()


def main():
    """
    Main function to load data, prepare it, and plot the projection.
    """
    # File paths
    income_path = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    life_expectancy_path = "life_expectancy_years.csv"

    # Specify the year for analysis
    year = 1900

    # Prepare the data
    data = prepare_data(income_path, life_expectancy_path, year)

    # Plot the projection
    plot_projection(data, year)


if __name__ == "__main__":
    main()

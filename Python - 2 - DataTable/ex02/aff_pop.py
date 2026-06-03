import matplotlib.pyplot as plt
from load_csv import load


def convert_val(x):
    """Convert population string to float value."""
    if isinstance(x, (int, float)):
        return float(x)
    x_str = str(x)
    return float(x_str.replace('M', 'e6').replace('k', 'e3'))


def format_y_axis(value, pos):
    """Format y-axis labels to show in millions or thousands."""
    if value >= 1_000_000:
        return f'{int(value/1_000_000)}M'
    elif value >= 1_000:
        return f'{int(value/1_000)}k'
    return str(int(value))


def main():
    """Compare population projections of France vs Belgium (1800-2050)."""
    # Load dataset
    df = load("population_total.csv")
    if df is None:
        return

    # Validate dataset
    if 'country' not in df.columns:
        print("Error: Invalid CSV format - missing 'country' column")
        return

    # Set country as index
    df = df.set_index('country')

    # Check countries exist
    countries = ['France', 'Belgium']
    for country in countries:
        if country not in df.index:
            print(f"Error: '{country}' not found in dataset")
            return

    # Select years from 1800 to 2050
    years = [str(year) for year in range(1800, 2051)]
    available_years = [year for year in years if year in df.columns]

    # Get data for both countries
    france_raw = df.loc['France'][available_years]
    belgium_raw = df.loc['Belgium'][available_years]

    # Convert population values
    france_values = [convert_val(x) for x in france_raw]
    belgium_values = [convert_val(x) for x in belgium_raw]

    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(available_years, france_values, label='France', color='green')
    plt.plot(available_years, belgium_values, label='Belgium', color='blue')

    # Customize plot
    plt.title('Population Projections')
    plt.ylabel('Population')
    plt.xlabel('Year')

    # Configure x-axis (show every 40 years)
    plt.xticks(available_years[::40], rotation=45)

    # Configure y-axis with custom formatter
    ax = plt.gca()
    ax.yaxis.set_major_formatter(plt.FuncFormatter(format_y_axis))

    plt.show()


if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
from load_csv import load


# Convert values (e.g., '64.5M' -> 64500000.0)
def convert_val(x):
    """Convert population string to float value."""
    return float(x.replace('M', 'e6').replace('k', 'e3'))


# Formater l'axe Y pour afficher "20M", "40M", "60M"
def format_y_axis(value, pos):
    """Format y-axis labels to show in millions or thousands."""
    if value >= 1_000_000:
        return f'{int(value/1_000_000)}M'
    elif value >= 1_000:
        return f'{int(value/1_000)}k'
    return str(int(value))


def main():
    """Compare population projections of France vs Belgium"""
    df = load("population_total.csv")
    df = df.set_index('country')

    # Get data for both countries
    france = df.loc['France'].iloc[:251]
    belgium = df.loc['Belgium'].iloc[:251]

    france_values = [convert_val(x) for x in france]
    belgium_values = [convert_val(x) for x in belgium]
    years = france.index

    # Create plot
    plt.plot(years, france_values, label='France', color='green')
    plt.plot(years, belgium_values, label='Belgium', color='blue')

    plt.title('Population Projections')
    plt.ylabel('Population')
    plt.xlabel('Year')
    plt.legend()

    # Show only some years on x-axis
    plt.xticks(years[::40])

    # Appliquer le formateur
    plt.gca().yaxis.set_major_formatter(format_y_axis)

    # Format y-axis to show 20M, 40M, 60M
    plt.yticks([20000000, 40000000, 60000000])

    plt.show()


if __name__ == "__main__":
    main()

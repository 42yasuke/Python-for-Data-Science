import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Main function to load the dataset and
    plot the life expectancy projections for France.
    """
    try:
        df = load("life_expectancy_years.csv")
    except Exception as e:
        print(e)
        return

    # Check Dataframe
    if 'country' not in df.columns:
        print("Not the expected CSV file")
        return

    df = df.set_index('country')

    # Check that DF contains France
    if 'France' not in df.index:
        print("Not the expected CSV file")
        return

    # Check that every columns can be parsed as int
    try:
        [int(x) for x in df.loc['France'].index]
    except Exception:
        print("Not the expected CSV file")
        return

    plt.plot(df.loc['France'])
    plt.title('France Life expectancy Projections')
    plt.ylabel('Life expectancy')
    plt.xlabel('Year')
    plt.xticks([x for x in df.loc['France'].index if (int(x) % 40 == 0)])
    plt.show()


if __name__ == "__main__":
    main()

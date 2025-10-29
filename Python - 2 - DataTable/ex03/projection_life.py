from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Plot the relation between incomes and life expectancy"""
    try:
        # Loading data
        income_data = load('income_per_person_gdppercapita_'
                           'ppp_inflation_adjusted.csv')
        life_expectancy_data = load('life_expectancy_years.csv')

        # Extract data for the year 1900
        YEAR = '1900'
        income_values = income_data[YEAR]
        life_expectancy_values = life_expectancy_data[YEAR]

        # Graphical representation
        plt.scatter(income_values, life_expectancy_values)

        plt.xlabel('Gross domestic product')
        plt.ylabel('Life expectancy')
        plt.title(YEAR)

        plt.xscale('log')
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()

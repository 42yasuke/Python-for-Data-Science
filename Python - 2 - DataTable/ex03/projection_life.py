from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
        Plot the relation between incomes and life expectancy
    """
    incomf = 'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'

    try:
        income_data = load(incomf)  # using a var to bypass flake8
        life_expectancy_data = load('life_expectancy_years.csv')
    except Exception as e:
        print(e)
        exit(0)

    # Extract the relevant columns
    YEAR = '1900'
    income_values = income_data[YEAR]
    life_expectancy_values = life_expectancy_data[YEAR]

    plt.scatter(income_values, life_expectancy_values)

    plt.xlabel('Gross domestic product')
    plt.ylabel('Life expectancy')
    plt.title(YEAR)

    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

    plt.show()


if __name__ == '__main__':
    main()

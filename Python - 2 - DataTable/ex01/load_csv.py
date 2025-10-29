import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
        Load a csv file in a dataframe.
    """
    df = pd.read_csv(path)
    print('Loading dataset of dimensions', df.shape)
    return df


def main():
    """
    Main function to load the dataset and handle exceptions.
    """
    try:
        print(load("life_expectancy_years.csv"))
    except FileNotFoundError as fe:
        print("FileNotFoundError : ", fe)


if __name__ == "__main__":
    main()

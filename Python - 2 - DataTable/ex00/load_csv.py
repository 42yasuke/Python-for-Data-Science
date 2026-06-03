import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    Load a csv file in a dataframe.

    Args:
        path (str): Path to the CSV file

    Returns:
        DataFrame with the data, or None if an error occurs
    """
    try:
        df = pd.read_csv(path)
        print(f'Loading dataset of dimensions {df.shape}')
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError,
            pd.errors.ParserError, PermissionError) as e:
        print(f"Error loading file: {e}")
        return None


def main():
    """
    Main function to load the dataset and handle exceptions.
    """
    data = load("life_expectancy_years.csv")
    if data is not None:
        print(data)


if __name__ == "__main__":
    main()

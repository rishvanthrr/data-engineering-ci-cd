import pandas as pd


def transform_data(df):
    """
    Increase salary by 10% and validate required columns.
    """
    df = df.copy()

    # Validate required columns
    required_columns = ["name", "age", "salary"]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    # Increase salary by 10%
    df["salary"] = df["salary"] * 1.10

    return df


def run_pipeline(input_file, output_file):
    """
    Read input CSV, transform data, and save output CSV.
    """
    df = pd.read_csv(input_file)

    transformed_df = transform_data(df)

    transformed_df.to_csv(output_file, index=False)

    return transformed_df


if __name__ == "__main__":
    run_pipeline(
        "data/input.csv",
        "data/output.csv"
    )
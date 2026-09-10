import pandas as pd


def transform_data(df):
    """
    Increase salary by 10%.
    """
    df = df.copy()
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
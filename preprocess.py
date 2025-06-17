
"""
preprocess.py
-------------
Simple data cleaning and feature engineering script for InsightViz.
"""

import pandas as pd
import argparse
from pathlib import Path

def preprocess(input_csv: str, output_csv: str):
    df = pd.read_csv(input_csv)

    # Example: create AverageChargesPerMonth feature
    df['avg_charges_per_month'] = df['total_charges'] / df['tenure_months'].replace({0: 1})

    # Fill any missing numeric values with median
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    df.to_csv(output_csv, index=False)
    print(f"Preprocessed data saved to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Path to raw csv')
    parser.add_argument('--output', default='data/cleaned_data.csv', help='Path for cleaned csv')
    args = parser.parse_args()

    preprocess(args.input, args.output)

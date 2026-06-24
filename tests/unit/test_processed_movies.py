import pandas as pd

df = pd.read_parquet(
    "data/processed/movies_clean.parquet"
)

print(df.head())

print("\n Shape:")
print(df.shape)

print("\n Columns:")
print(df.columns.tolist())

print("\n Data Types:")
print(df.dtypes)
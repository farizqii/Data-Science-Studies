import pandas as pd  # type: ignore
import string

df = pd.read_csv(r".\Datas\PokemonDatas.csv", index_col="Name")

# Data Cleaning = The process of fixing/removing:
#                 incomplete, incorrect, or irrelevant data.
#                 ~75% of work done with Pandas is data cleaning

# 1. Drop Irrelevant Columns
# df = df.drop(columns=["Legendary", "No"])

# 2. Handle Missing Data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2": "None"})

# 3. Fix Inconsistent Values
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Fire": "FIRE", "Water": "WATER"})

# 4. Standardize Text
# df["Type1"] = df["Type1"].str.lower()

# 5. Fix Data Types
# df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove Duplicate Values
df = df.drop_duplicates()

print(df)
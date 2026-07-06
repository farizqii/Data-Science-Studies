import pandas as pd  # type: ignore
import string

df = pd.read_csv(r".\Datas\PokemonDatas.csv", index_col="Name")

# SELECTION BY COLUMN
# print(df["Name"])
# print(df["Height"])
# print(df[["Name", "Height", "Weight"]])

# SELECTION BY ROWS
# print(df.loc["Pikachu"])
# print(df.loc["Pikachu", ["Height", "Weight"]])
# print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])
# print(df.iloc[0:11:3])
# print(df.iloc[0:11:3, 0:3])

pokemon = input("Enter a Pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found!")
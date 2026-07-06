import pandas as pd  # type: ignore
import string

df = pd.read_csv(r".\Datas\PokemonDatas.csv", index_col="Name")

# Aggregate Functions = Reduces a set of values into a single summary value.
#                       Used to summarize and analyze data.
#                       Often used with the groupby() function

# WHOLE DATAFRAME
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# SINGLE COLUMNS
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())

# GROUPS
group = df.groupby("Type1")
# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min())
# print(group["Height"].max())
# print(group["Height"].count())
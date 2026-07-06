import pandas as pd  # type: ignore
import string

df = pd.read_csv(r".\Datas\PokemonDatas.csv")

print("Truncated Version:")
print(str(df) + '\n')

# print("Full Versions:") # Use caution working with large data files
# print(str(df.to_string()) + '\n')

print("Poison Pokemons:")
poisonPokemons = df[(df['Type1'] == "Poison") | (df["Type2"] == "Poison")]
print(str(poisonPokemons))
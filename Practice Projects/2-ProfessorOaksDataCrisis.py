# Scenario:
# Professor Oak's computer crashed, and his research assistants managed to salvage a .csv file
# containing data on various Pokemon. However, the data is a bit messy, and the Professor needs
# answers for his upcoming research paper on Pokemon biology. He has hired your as his Lead
# Data Scientist to clean the database and run some analytics.

# Phase 1: LOADING & CLEANING (The Foundations)
# 1. Load the data: Read PokemonDatas.csv into a DataFrame. Make sure the Name column is set
#    as the index so you can easily search for Pokemon by name later.

# 2. Drop the Dead Weight: The No column is redundant now that we have the names as the index.
#    Drop the No column entirely.

# 3. Handle Missing Values: Many Pokemon don't have a secondary type, meaning the Type2 column
#    is full of missing data (NaN). Fill all missing values in Type2 with the string "None".

# 4. Standardize Text: To make searching easier, convert all the text in the Type1 and Type2
#    columns to uppercase (e.g., "Grass" becomes "GRASS").

# Phase 2: FEATURE ENGINEERING (Creating New Data)
# The Professor wants to study the physical density of Pokemon
# 1. Calculate BMI: Create a new column BMI (Body Mass Index). The formula that the professor wants
#                   you to use is: BMI = Weight / (Height * Height)

# Phase 3: Advanced Filtering (Finding Specific Subjects)
# The professor needs a specific list of Pokemon for a field study.
# 1. The Giants: Filter your DataFrame to find all Pokemon that have a Height greater than 2.0 meters
#                AND a Weight than 100.0 kg. Save this filtered DataFrame into a new variable called
#                giant_pokemon.

# 2. The Mythics: From that giant_pokemon list, filter it down even further to show only the ones
#                 where Legendary is True.

# Phase 4: Grouping & Analytics (The Bro Code Finale)
# 1. Type Analysis: Group the main, cleaned DataFrame by Type.

# 2. Find the Averages: Calculate the average (mean) Height and Weight for each Type1 category.

# 3. Based on your grouped data, which primary Pokémon type is the heaviest on average?

# Phase 5: Exporting
# 1. Save your work: Save your fully cleaned and updated main DataFrame

import pandas as pd  # type: ignore
import string

# PHASE 1
# Data Load
df = pd.read_csv(r".\Datas\PokemonDatas.csv", index_col="Name")
# Drop the dead weight
df = df.drop(columns=["No"])
df = df.drop_duplicates()
# Handle Missing Value
df = df.fillna({"Type2": "None"})
# Standardize Text
df["Type1"] = df["Type1"].str.upper()
df["Type2"] = df["Type2"].str.upper()

# PHASE 2
# Add a new BMI Column
df["BMI"] = round(df["Weight"] / (df["Height"] * df["Height"]))

# PHASE 3
# Giant Pokemons DataFrame
giant_pokemon = df[(df["Height"] > 2.0) & (df["Weight"] > 100.0)]

# Mythic Pokemons
giant_pokemon["Legendary"] = giant_pokemon["Legendary"].astype(bool)
mythic_giants = giant_pokemon[giant_pokemon["Legendary"] == True]

# PHASE 4
# Grouping
group = df.groupby("Type1")
# Average from Height and Weight
mean = round(group[["Height", "Weight"]].mean())
# Heviest Pokemon Type
heaviestPokemonType = mean["Weight"].idxmax()
print(heaviestPokemonType)

# PHASE 5
# Save the Work
# df.to_csv(r".\Datas\Oak_Cleaned_Pokemon.csv")
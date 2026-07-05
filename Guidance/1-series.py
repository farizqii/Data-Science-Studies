import pandas as pd
import string

# Series = A Pandas 1-Dimensional Array that can hold any data type
#          Think of it like a single column in an Excel spreadsheet (1-Dimensional)

# Create a list of uppercase letters from A to Z
alphabet_list = list(string.ascii_uppercase)

# Datasets for different data types
dataInt = [100, 102, 104, 106, 108]
dataFloat = [100.1, 102.5, 104.8, 106.2, 108.4]
dataString = ["C++", "Python", "Java", "JavaScript", "Ruby", "Go", "Rust", "Swift", "Kotlin", "PHP"]
dataBool = [True, False, True, False, True]

# Automatically create a dictionary for calorie intake over 5 days (No need to create an index for this one, as the keys will serve as the index)
calorieIntake = {"Day 1": 2000, "Day 2": 2200, "Day 3": 1800, "Day 4": 2500, "Day 5": 2100}

# Create Pandas Series for each data type
seriesInt = pd.Series(dataInt, index=range(1, len(dataInt) + 1))
seriesFloat = pd.Series(dataFloat, index=alphabet_list[:len(dataFloat)])
seriesString = pd.Series(dataString, index=range(1, len(dataString) + 1))
seriesBool = pd.Series(dataBool, index=alphabet_list[:len(dataBool)])
seriesCalories = pd.Series(calorieIntake)

# Print the Series
print("Integer Series:")
print(seriesInt)

print("\nFloat Series:")
print(seriesFloat)

print("\nString Series:")
print(seriesString)

print("\nBoolean Series:")
print(seriesBool)

print("\nCalorie Intake Series:")
print(seriesCalories)

# Test
print("\nTest:")
print(seriesInt.loc[4])
print(seriesCalories.loc['Day 2'])
print(seriesInt[seriesInt >= 106])

# Update a value one of the calorie intake values
seriesCalories.loc['Day 2'] += 500
print("\nUpdated Calorie Intake Series:")
print(seriesCalories.loc['Day 2'])
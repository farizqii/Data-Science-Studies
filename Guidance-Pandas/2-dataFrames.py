import pandas as pd # type: ignore
import string

# DataFrame = A tubular data structure with rows & columns (2-Dimensional)
#             Think of it like a table in a database or an Excel spreadsheet (2-Dimensional)

dataEmployees = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 45],
}

dfEmployees = pd.DataFrame(dataEmployees, index=["Employee 1", "Employee 2", "Employee 3", "Employee 4", "Employee 5"])

# Print the DataFrame
print("Full DataFrame:")
print(dfEmployees)

print("\nDataFrame Info (by label):")
print(dfEmployees.loc["Employee 3"])

print("\nDataFrame Info (by integer position):")
print(dfEmployees.iloc[3]) # Starts at 0, so this will return the 4th row (David)

# Add a new column
dfEmployees["Job"] = ["Engineer", "Manager", "Analyst", "Designer", "Consultant"]
print("\nUpdated DataFrame with Job column:")
print(dfEmployees)

# Add new rows
new_employees = pd.DataFrame([{"Name": "Sam", "Age": 19, "Job": "Intern"},
                            {"Name": "Lily", "Age": 28, "Job": "Data Scientist"}],
                            index=["Employee 6", "Employee 7"])
dfEmployees = pd.concat([dfEmployees, new_employees])
print("\nUpdated DataFrame with new employees:")
print(dfEmployees)
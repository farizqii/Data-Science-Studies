import pandas as pd # type: ignore
import string

# Scenario = You've been asked to help a small, local bookstore organize their inventory.
#            The owner has handed you a messy list of their top-selling books, prices, and
#            current stock levels. Your job is to digitize this using Pandas and answer a few
#            basic questions about the store's inventory.

# Task 1: Create the Data Structures
# 1. Create a Series: The store owner wants to track the genres they carry.
#                  Create a Pandas Series containing the following genres: Fiction, 
#                  Non-Fiction, Sci-Fi, Mystery, and Biography.

# 2. Create a DataFrame: Below is the raw data for the bookstore's inventory. Convert this
#                        Python dictionary into a Pandas DataFrame called invetory_df.

raw_data = {
    'Title': ['The Great Gatsby', 'Sapiens', 'Dune', 'Gone Girl', 'Steve Jobs'],
    'Author': ['F. Scott Fitzgerald', 'Yuval Noah Harari', 'Frank Herbert', 'Gillian Flynn', 'Walter Isaacson'],
    'Price': [10.99, 15.50, 12.00, 9.99, 18.25],
    'Stock': [14, 8, 22, 5, 11]
}

genresSeries = pd.Series(["Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Biography"])
inventory_df = pd.DataFrame(raw_data, index=(1, 2, 3, 4, 5))
# FULL DATAFRAME
print("Full DataFrame:")
print(str(inventory_df) + '\n')

# Task 2: Inspect the Data
# Now that your data is in a DataFrame, let's look around.
# Write the Pandas code to do the following:

# - Display the first 3 rows of the DataFrame.
# - Display a quick summary of the DataFrame 
# - Extract just the Title column as a single Pandas Series.

#INSPECTION
print("Display The First 3 Rows:")
print('\n' + str(inventory_df.head(3)) + '\n')

print("Display The Quick Summary:") 
inventory_df.info()

print("Extract Title Column:")
titleSeries = inventory_df['Title']
print('\n' + str(titleSeries) + '\n')

# Task 3: Basic Indexing and Filtering
# The owner is asking you some specific questions. Use Pandas to find the answers:

# - Low Stock Alert: Filter the DataFrame to show only the books
#                    that have fewer than 10 copies in stock.
# - Premium Books: Filter the DataFrame to show only the books that 
#                  cost more than $12.00.

#INSPECTION
print("The Lowest Stocks:")
print('\n' + str(inventory_df[inventory_df['Stock'] < 10]) + '\n')

print("Premimum Books:")
print('\n' + str(inventory_df[inventory_df['Price'] > 12.00]) + '\n')

# Task 4: A Little Math (Bonus)
# DataFrames make math easy. Try to figure out:

# - What is the total number of books currently in stock across all titles?
# - Create a new column in your DataFrame called Total_Value.
#   This should be calculated by multiplying the Price column by the Stock column.

#INSPECTION
print("The Total Books In Stocks Across All Titles:")
totalBookStocks = inventory_df['Stock'].sum()
print('\n' + str(totalBookStocks) + '\n')

print("New Column In The DataFrame:")
inventory_df["Total_Value"] = inventory_df['Price'] * inventory_df['Stock']
print(inventory_df)
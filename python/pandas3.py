import pandas as pd

# 1. Creating a DataFrame from a Dictionary
data_dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df_dict = pd.DataFrame(data_dict)
print("DataFrame from Dictionary:")
print(df_dict)

# Save to Excel
df_dict.to_excel("pandas_data_dict.xlsx", index=False)

# ----------------------------------------------------

# 2. Creating a DataFrame from a List of Lists
data_list_of_lists = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

df_list_of_lists = pd.DataFrame(data_list_of_lists, columns=["Name", "Age", "City"])
print("\nDataFrame from List of Lists:")
print(df_list_of_lists)

# Save to Excel
df_list_of_lists.to_excel("pandas_data_list_of_lists.xlsx", index=False)

# ----------------------------------------------------

# 3. Creating a DataFrame from a List of Dictionaries
data_list_of_dicts = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]

df_list_of_dicts = pd.DataFrame(data_list_of_dicts)
print("\nDataFrame from List of Dictionaries:")
print(df_list_of_dicts)

# Save to Excel
df_list_of_dicts.to_excel("pandas_data_list_of_dicts.xlsx", index=False)

# ----------------------------------------------------

# 4. Creating a DataFrame from a Single List
data_single_list = ["Alice", "Bob", "Charlie"]

df_single_list = pd.DataFrame(data_single_list, columns=["Name"])
print("\nDataFrame from Single List:")
print(df_single_list)

# Save to Excel
df_single_list.to_excel("pandas_data_single_list.xlsx", index=False)

# ----------------------------------------------------

# 5. Saving All DataFrames into One Excel File with Multiple Sheets
with pd.ExcelWriter("pandas_combined_dataframes.xlsx") as writer:
    df_dict.to_excel(writer, sheet_name="From Dictionary", index=False)
    df_list_of_lists.to_excel(writer, sheet_name="From List of Lists", index=False)
    df_list_of_dicts.to_excel(writer, sheet_name="From List of Dicts", index=False)
    df_single_list.to_excel(writer, sheet_name="From Single List", index=False)

print("\nAll DataFrames saved to individual Excel files and combined Excel file.")

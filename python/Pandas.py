import pandas as pd

# ========= LOADING/READING THE DATASET =========
df = pd.read_excel("pandas1.xlsx")  # Where df is short for data frame
# print(df)

# ========= SHOW THE DATA TYPES OF EACH COLUMN =========
# print(df.dtypes)

# ========= GET ONLY THE FIRST 6 ROWS OF DATA =========
# print(df.head(6))

# ========= GET ONLY THE LAST 6 ROWS OF DATA =========
# print(df.tail(6))

# ========= GET NUMBER OF ROWS X COLUMNS =========
# print(f'shape: ${df.shape}')

# ========= GET INFO OF THE DATA =========
# print(df.info)

# ========= READ COLUMNS (THERE IS A COLUMN TITLED; COUNTRIES) =========
# print(df.Countries)
# print(df['Products'])  #Same as above
# print(df[['Countries', 'Products']])    #Print more than one column.


# ========= READ ROWS (USE ROW NUMBER) =========
# print(df.iloc[0])   # A single row
# print(df.iloc[0:3])   # row 0,1,2

# ========= GET DATA WITHIN A CELL ========
# print(df.iloc[0,5]) #Get the value of row 0, column 5 (ie Order Date)


# ======== SORTING =======================
# print(df.sort_values('Countries'))  # Ascending by default
# print(df.sort_values('Countries', ascending=False))  # Descending order
# print(df.sort_values(['Countries', 'Quantity']))    # Both in ascending order
# print(df.sort_values(['Countries', 'Quantity'], ascending=[1, 0]))  # 1 mean true

# ======== FILTER =======================
# print(df.loc[df['Countries'] == "Nigeria"])

# ======== CREATING COLUMNS =======================
# ie 3 columns; Revenues, Costs, profit
# df['Revenues'] = df['Quantity'] * df['Revenue per product']
# df['Costs'] = df['Quantity'] * df['Cost per product']
# df['Profit'] = df['Revenues'] - df['Costs']
# print(df)

# ======== DELETING COLUMNS =======================
# del df['Profit']

# ========= DATE FUNCTION ================
# df['M1'] = df['Order Date'].dt.strftime('%m')    # Create a column M1, extracting month in numbers from Order Date
# df['M1'] = df['Order Date'].dt.month             # Similar to the above (Also, in numbers)
# df['M1'] = df['Order Date'].apply(lambda x: x.strftime('%B'))             # Extract month name, instead of numbers.
# df['M1'] = df['Order Date'].dt.strftime('%Y')    # Extracting Year
df['M1'] = df['Order Date'].apply(lambda x: x.strftime('%B/%Y'))      #Combining Month and Year

print(df)


# ======== SAVE/SAVING A COPY OF THE FILE =======================
# df.to_excel('Pandas1b.xlsx', index=False)


import pandas as pd

df = pd.read_excel("pandas2.xlsx")
# del df['Profit']

# Delete some unwanted columns
del df['Total(100)']
del df['Grade']
del df['Comment']

# Create a new column
df["Total(100)"] = df["Exam(65)"] + df["Midterm(20)"] + df["C.A(15)"]

# Assuming; 80-100 = A (on column, Grade)
# 70-79 = B
# 60-69 = C
# 55-59 = D
# 50-54 = E
# 0-49 = F

df['Grade'] = df['Total(100)'].apply(lambda x: 'A' if x >= 80
else 'B' if x >= 70
else 'C' if x >= 60
else 'D' if x >= 55
else 'E' if x >= 50
else 'F')

# ======== FORMAT DECIMAL NUMBERS (ie, make all 2 dp) =======================

# 1. For a single column
decimalplaces = 2
df['Exam(65)'] = df['Exam(65)'].apply(lambda x: round(x, decimalplaces))

# 2. For the entire data frame
df = df.round(decimals=3)


# ======== COUNT VALUES =======================
# print(df['Grade'].count())          # Number of rows in the column
# print(df['Grade'].value_counts())   # Number of each element in the column
# print(df['Total(100)'].sum())       # Sum of all values in the column
# print(df['Total(100)'].mean())      # Mean of all values in the column
# print(df['Total(100)'].std())       # Standard deviation of all values in the column
# print(df['Total(100)'].max())       # Maximum of all values in the column


# =================== PERCENTAGE (ie %ge difference) ===================
# Simply use the mathematics of getting percentage. ie (x2-x1)/100 * ...

# print(df)

# Import libraries
import pandas as pd
import numpy as np


# Read csv file into a DataFrame object (df)
df = pd.read_csv("property data.csv")


# Print first 5 lines of df
# print(df.head())

# Prints the value stored in the csv in a specific column
# print(df['COL_NAME'])
# Prints if the data is null or not
# print(df['COL_NAME'].isnull())


# Making a list of missing value types (differs for different csv files)
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("property data.csv", na_values=missing_values)


# Detecting numbers in a column that shouldn't have any
count = 0
for row in df['OWN_OCCUPIED']:
    try:
        int(row)
        df.loc[count, 'OWN_OCCUPIED'] = np.nan
    except ValueError:
        pass
    count += 1
print('\n' + str(count) + " Numbers detected where they shouldn't be in the OWN_OCCUPIED"
                          " column where value should be Y/N.\n")

# Check for any missing values
print("Any Missing Values? ")
if df.isnull().values.any():
    # Total number of missing values
    print(str("Yes, " + str(df.isnull().sum().sum())) + " Missing values found in the table. \n")
else:
    print("No")
# Total missing values for each feature
print("Missing Values: \n" + str(df.isnull().sum()) + '\n')


# Fills in missing values of ST_NUM with the default value
print("Replacing null values with a default value (999) in ST_NUM.")
default = 999
df['ST_NUM'].fillna(default, inplace=True)
print(df['ST_NUM'])

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

# Read an Excel file named "sales_data.xlsx" into a DataFrame.
# Set "Row ID" as the index column for the DataFrame.
data = pd.read_excel("sales_data.xlsx", index_col = "Row ID")

# Create a new column called "month_year" by formatting the "Order Date" column
# as a string in the format "MM-YYYY".
data["month_year"] = data["Order Date"].dt.strftime("%m-%Y")

# Group the DataFrame 'data' by the values in the "month_year" column,
# creating separate groups for each unique "month_year" value.
gb = data.groupby("month_year")

# Initialize an empty list called 'ls'.
ls = []

# Iterate through the group names in the 'gb' object.
for df in gb.groups:
    # Get the group data associated with the current group name and append it to the '1s' list.
    ls.append(gb.get_group(df))
    
for df in ls:
    # Extract the "month_year" value from the first row of the DataFrame.
    file_name = df["month_year"].iloc[0]
    
    # Save the data in the current DataFrame to an Excel file.
    # The file name is derived from the "month_year" value, and the '.xlsx' extension is added.
    # The 'index=False' parameter specifies not to write the index to the Excel file.
    df.to_excel("{}.xlsx".format(file_name), index=False)
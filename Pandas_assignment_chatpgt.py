# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:03:20 2023

@author: chuc2
"""

import pandas as pd

# Read the Excel file into a DataFrame
data = pd.read_excel("sales_data.xlsx", index_col="Row ID")

# Extract the month and year from the "Order Date" column and create a new column
data["month_year"] = data["Order Date"].dt.strftime("%m-%Y")

# Group the data by the "month_year" column
grouped_data = data.groupby("month_year")

# Iterate through the groups and save each group to a separate Excel file
for group_name, group_data in grouped_data:
    # Generate the file name based on the group name
    file_name = f"{group_name}.xlsx"

    # Save the group data to an Excel file with the group name as the file name
    group_data.to_excel(file_name, index=False)

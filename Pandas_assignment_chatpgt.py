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
# 'group_name' is the name of the group (e.g., the value in the "month_year" column)
# 'group_data' is the DataFrame containing the data for that group
# This would iterate through each group (grouped by the values in the "month_year" column) 
# and provide you with both the group name (e.g., "03-2022") and the associated DataFrame
# containing data for that group.
for group_name, group_data in grouped_data:
    # Generate the file name based on the group name
    file_name = f"{group_name}.xlsx"

    # Save the group data to an Excel file with the group name as the file name
    group_data.to_excel(file_name, index=False)

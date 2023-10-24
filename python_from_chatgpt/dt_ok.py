import pandas as pd
import numpy as np

# Create the 'data' DataFrame
data = pd.DataFrame({'A': ["chuc", np.nan, "Sua", "Vinh", np.nan, np.nan, "Tam", np.nan, "Thuan", "Hao", np.nan, "Phuc"],
                     'B': [np.nan, 6, 7, np.nan, np.nan, 8, np.nan, 66, np.nan, np.nan, 33, np.nan], 
                     'C': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 
                     'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]})

# Create the 'data2' DataFrame
data2 = pd.DataFrame({'A': ["chuc", "Vinh", "Thuan"],
                      'C': [8, 9, 7]})



data3 = pd.DataFrame({'A': ["chuc", np.nan, "Sua", "Vinh", np.nan, np.nan, "Tam", np.nan, "Thuan", "Hao", np.nan, "Phuc"],
                     'B': [np.nan, 6, 7, np.nan, np.nan, 8, np.nan, 66, np.nan, np.nan, 33, np.nan], 
                     'C': [8, np.nan, np.nan, 9, np.nan, np.nan, np.nan, np.nan, 7, np.nan, np.nan, np.nan], 
                     'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]})

# Merge 'data' and 'data2' based on the 'A' column and update 'C' and 'D' columns
data3 = data.merge(data2, on='A', how='left')
data3['C'] = data3['C_y'].fillna(data3['C_x'])
if 'D_y' in data3.columns:
    data3['D'] = data3['D_y'].fillna(data3['D_x'])
    data3 = data3.drop(['C_x', 'C_y', 'D_x', 'D_y'], axis=1)
else:
    data3 = data3.drop(['C_x', 'C_y'], axis=1)

# Print the resulting 'data3' DataFrame
print(data3)
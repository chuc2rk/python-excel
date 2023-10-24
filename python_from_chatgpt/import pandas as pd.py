import pandas as pd
import numpy as np

# Create a sample DataFrame
data = pd.DataFrame({'A': [4, np.nan, np.nan, 7, np.nan, np.nan, np.nan, np.nan, 5, np.nan, np.nan, np.nan],
                     'B': [np.nan, 5, 8, np.nan, 8, np.nan, 9, 7, np.nan, np.nan, 6, np.nan], 
                     'C': [3, np.nan, np.nan, 4, np.nan, np.nan, np.nan, np.nan, 9, np.nan, np.nan, np.nan], 
                     'D': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]})

# Initialize y
y = None

# Loop through each row in the DataFrame
for index, row in data.iterrows():
    # Check if the cell in column "A" is not NaN
    if not pd.isna(row["A"]):
        y = row["C"]
    else:
        # Modify the "D" column in place using "iat"
        data.at[index, "D"] = y * row["B"]

# Print the modified DataFrame
print(data)

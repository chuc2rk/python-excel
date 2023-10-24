# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 10:53:25 2023

@author: KHKT
"""

import pandas as pd

xd = pd.read_excel("xl15.xlsx", sheet_name="1.ATGT", header=1)
xd1 = pd.read_excel("xl15.xlsx", sheet_name="Phân tích đơn giá ok", header=7)

xd1_cp = xd1.iloc[:48]

xd1_sl = xd1_cp[["STT", "Tên công tác ", "Khối lượng"]]

#xd1_sl = xd1_slT.groupby("STT", as_index=False).sum(numeric_only=True)


xd_sl = xd[["STT", "Tên công tác ", "Đơn vị", "Định mức","Đơn giá ", "Khối lượng", "KLTC","TTTC"]]

for _, row in xd1_sl.iterrows():
    mask = (xd_sl["Tên công tác "] == row["Tên công tác "])  & xd_sl["Khối lượng"].isna()
    xd_sl.loc[mask, "Khối lượng"] = row["Khối lượng"]
  

    
# Initialize y
y = 0

# Loop through each row in the DataFrame
for index, row in xd_sl.iterrows():
    # Check if the cell in column "A" is not NaN
    if not pd.isna(row['STT']):
        y = row['Khối lượng']
    else:
        # Modify the "D" column in place using "iat"
        xd_sl.at[index, "KLTC"] = y * row["Định mức"]
        
        
for index, row in xd_sl.iterrows():
        # Modify the "D" column in place using "iat"
        xd_sl.at[index, "TTTC"] = (row["Đơn giá "] * row["KLTC"])
        
        
#result = xd_sl.groupby("Hạng mục công việc").sum()

p_table = pd.pivot_table(xd_sl, index=['Tên công tác ', "Đơn vị"], aggfunc= {'Đơn giá ': 'mean', 'KLTC': 'sum', 'TTTC': 'sum'})

df = p_table[p_table['Đơn giá '].notna()]

#df_s = df.sort_values("ĐƠN VỊ")

df.to_excel('Tonghop1.xlsx')

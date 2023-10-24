# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 10:53:25 2023

@author: KHKT
"""

import pandas as pd

xd = pd.read_excel("dth.xls", sheet_name="PTĐG1", header=3)
xd1 = pd.read_excel("dth.xls", sheet_name="DTCT", header=3)

#temp = xd.merge(xd1, on="Số định mức", how='left')
#temp2 = temp.drop_duplicates("Hạng mục công việc_x")
xd1_slT = xd1[["Số định mức", "Hạng mục công việc", "Khối lượng"]]

xd1_slT1 = xd1_slT[pd.to_numeric(xd1_slT['Khối lượng'], errors='coerce').notnull()]

xd1_sl = xd1_slT1.groupby("Số định mức", as_index=False).sum()


xd_sl = xd[["Số định mức", "Hạng mục công việc", "ĐƠN VỊ", "ĐỊNH MỨC","ĐƠN GIÁ", "Khối lượng", "KLTC","TTTC"]]

for _, row in xd1_sl.iterrows():
    mask = (xd_sl["Số định mức"] == row["Số định mức"]) #& xd_sl["Khối lượng"].isna()
    xd_sl.loc[mask, "Khối lượng"] = row["Khối lượng"]
  

    
# Initialize y
y = 0.0

# Loop through each row in the DataFrame
for index, row in xd_sl.iterrows():
    # Check if the cell in column "A" is not NaN
    if not pd.isna(row['Số định mức']):
        y = row['Khối lượng']
    else:
        # Modify the "D" column in place using "iat"
        xd_sl.at[index, "KLTC"] = y * row["ĐỊNH MỨC"]

#xd_sl = xd_sl[xd_sl['ĐƠN GIÁ'].notna()]        
        
for index, row in xd_sl.iterrows():
        # Modify the "D" column in place using "iat"
        xd_sl.at[index, "TTTC"] = (row["ĐƠN GIÁ"] * row["KLTC"])
        
        
#result = xd_sl.groupby("Hạng mục công việc").sum()

p_table = pd.pivot_table(xd_sl, index=['Hạng mục công việc', "ĐƠN VỊ"], aggfunc= {'ĐƠN GIÁ': 'mean', 'KLTC': 'sum', 'TTTC': 'sum'})

df = p_table[p_table['ĐƠN GIÁ'].notna()]

df.to_excel('Tonghop2.xlsx')



# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 10:53:25 2023

@author: KHKT
"""

import pandas as pd

xd = pd.read_excel("dth.xls", sheet_name="PTĐG1", header=3)
xd1 = pd.read_excel("dth.xls", sheet_name="DTCT", header=3)

#temp = xd.merge(xd1, on="Số định mức", how='left')
#temp2 = temp.drop_duplicates("Hạng mục công việc_x")
xd1_slT = xd1[["Số định mức", "Hạng mục công việc", "Khối lượng"]]

#xd1_slT1 = xd1_slT[pd.to_numeric(xd1_slT['Khối lượng'], errors='coerce').notnull()]

# convert age column to numeric type
xd1_slT['Khối lượng'] = pd.to_numeric(xd1_slT['Khối lượng'], errors='coerce')

# remove rows with NaN values
xd1_slT = xd1_slT.dropna(subset=['Khối lượng'])

xd1_sl = xd1_slT.groupby("Số định mức", as_index=False).sum(numeric_only=True)


xd_sl = xd[["Số định mức", "Hạng mục công việc", "ĐƠN VỊ", "ĐỊNH MỨC","ĐƠN GIÁ", "Khối lượng", "KLTC","TTTC"]]

for _, row in xd1_sl.iterrows():
    mask = (xd_sl["Số định mức"] == row["Số định mức"]) #& xd_sl["Khối lượng"].isna()
    xd_sl.loc[mask, "Khối lượng"] = row["Khối lượng"]
  

    
# Initialize y
y = 0.0

# Loop through each row in the DataFrame
for index, row in xd_sl.iterrows():
    # Check if the cell in column "A" is not NaN
    if not pd.isna(row['Số định mức']):
        y = row['Khối lượng']
    else:
        # Modify the "D" column in place using "iat"
        xd_sl.at[index, "KLTC"] = y * row["ĐỊNH MỨC"]

#xd_sl = xd_sl[xd_sl['ĐƠN GIÁ'].notna()]        
        
for index, row in xd_sl.iterrows():
        # Modify the "D" column in place using "iat"
        xd_sl.at[index, "TTTC"] = (row["ĐƠN GIÁ"] * row["KLTC"])
        
        
#result = xd_sl.groupby("Hạng mục công việc").sum()

p_table = pd.pivot_table(xd_sl, index=['Hạng mục công việc', "ĐƠN VỊ"], aggfunc= {'ĐƠN GIÁ': 'mean', 'KLTC': 'sum', 'TTTC': 'sum'})

df = p_table[p_table['ĐƠN GIÁ'].notna()]

df.to_excel('Tonghop2.xlsx')
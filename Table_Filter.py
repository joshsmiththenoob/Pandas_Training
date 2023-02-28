# filter data with condition
import pandas as pd

# read csv file with pandas
Starbucks_Table = pd.read_csv('./Starbucks satisfactory survey.csv')
print(Starbucks_Table)

# filter data with if condition
filt = (Starbucks_Table['3. Are you currently....?'] == 'Student')
print("兩種方法尋找特定欄位的值為student的所有資料")
print(Starbucks_Table[filt])
print(Starbucks_Table.loc[filt])
print("="*50)

print("利用loc尋找特定欄位的值為student、並篩選特定欄位的所有資料")
print(Starbucks_Table.loc[filt, ['3. Are you currently....?', '5. How often do you visit Starbucks?', '10. What do you most frequently purchase at Starbucks?']])
print("="*50)

# filter data with if multiple conditions
# & : and ; | : or
filt = (Starbucks_Table['3. Are you currently....?'] == 'Student') & (Starbucks_Table['9. Do you have Starbucks membership card?'] == 'Yes')
print("利用loc查詢符合兩個條件的所有資料")
print(Starbucks_Table.loc[filt])
print("="*50)

print("利用loc查詢符合兩個條件,並篩選特定欄位的所有資料")
print(Starbucks_Table.loc[filt, ['3. Are you currently....?', '5. How often do you visit Starbucks?', '10. What do you most frequently purchase at Starbucks?']])
print("="*50)


# filter data with "is in" method
# if mutilple conditions is in '3. Are you currently....?' column
filt_value = ['Employed', 'Self-employed', 'Student'] # target value where we want to get data from
filt = (Starbucks_Table['3. Are you currently....?'].isin(filt_value)) # condition
print("利用loc查詢符合多個條件,並篩選特定欄位的所有資料")
print(Starbucks_Table.loc[filt, ['3. Are you currently....?', '5. How often do you visit Starbucks?', '10. What do you most frequently purchase at Starbucks?']])
print("="*50)

# filter data with string and RegExp (regular expression)
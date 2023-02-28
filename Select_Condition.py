import pandas as pd

# create table
grades = {
    "name" : ["Mike", "Sherry", "Cindy", "John"],
    "math" : [80, 75, 93, 86],
    "chinese" : [63, 90, 85, 70] 
}

my_table = pd.DataFrame(grades)
print("初始表格 : \n",my_table)
print("="*50)

# use where condition to filter data
print("篩選math大於80的資料集")
# my_table["column name"] > 80 : return Boolean(True or False) if values of specific column > 80
print('my_table["math"] > 80 : 查詢特定欄位下所有資料的值是否大於80 -> 回傳 Boolean')
print(my_table["math"] > 80)
print("="*50)

print('my_table[my_table["math"] > 80] : 查詢特定欄位、大於80的資料')
print(my_table[my_table["math"] > 80])
print("="*50)

# is in : get the record if it is in table
print('my_table["name"].isin(["John"]) : 查詢表格特定欄位是否有該筆資料 -> 回傳 Boolean')
print(my_table["name"].isin(["John"]))
print("="*50)

print("篩選name欄位包含John的資料")
print(my_table[my_table["name"].isin(["John"])])
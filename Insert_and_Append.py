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

# insert : insert column in specific column index
my_table.insert(2,column= "English", value=[88,72,74,98])
print("於第三個(index=2)欄位插入English欄位的資料")
print(my_table)
print("="*50)

# append : append record with dict
# create new record
new_rec = {"name" : "Henry",
           "math" : 60,
           "English" : 51,
           "chinese" :63}
new_table = my_table.append(new_rec, ignore_index=True)
print("於表格最後面新增(附加)一筆資料")
print(new_table)
print("="*50)

# concat : = concate table1 with table2 
# get another table
table2 = pd.DataFrame({
    "name" : ["Henry"],
    "math" : [99],
    "English" : [19],
    "chinese" : ["123"]
})

new_table = pd.concat([my_table,table2])
print("合併表格後得出的新表格")
print(new_table)
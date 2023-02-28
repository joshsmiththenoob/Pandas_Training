import pandas

# create table
grades = {
    "name" : ["Mike", "Sherry", "Cindy", "John"],
    "math" : [80, 75, 93, 86],
    "chinese" : [63, 90, 85, 70] 
}

my_table = pandas.DataFrame(grades)
print("初始表格 : \n",my_table)
print("="*50)


# Head : Select first n records of table
new_table = my_table.head(2)      # select first 2 recs of table
print("Head前兩筆資料 : \n",new_table)
print("="*50)

# Tail : Select last n records of table
new_table = my_table.tail(2)      # select last 2 recs of table
print("Tail最後兩筆資料 : \n", new_table)
print("="*50)

# select specific column and index to get data
# one column
print("my_table['name'] : ","取得單一欄位資料(型別為Series)")
print(my_table["name"])
print(type(my_table["name"]))
print("="*50)

print("my_table[['name']] : ","取得單一欄位資料(型別為DataFrame)")
print(my_table[["name"]])
print(type(my_table[["name"]]))
print("="*50)

# multiple columns
print("my_table[['name','chinese']] : ","取得多欄位資料(型別為DataFrame)")
print(my_table[["name","chinese"]])
print("="*50)

# index
print("my_table[0:3] : 取得索引值(index)0~2的紀錄(資料)")
print(my_table[0:3])
print("="*50)

# at[index,'column name']
print("at[index,'column name'] : 特定筆數、特定欄位的資料")
print(my_table.at[1,"math"])
print("="*50)

# iat[index, column index]
print("iat[index, column index] : 第幾筆、第幾個欄位的資料")
print(my_table.iat[1,1])
print("="*50)

# loc[[index0:index1],['column name1', 'column name2']]
print("loc[[index0, index1],['column name1', 'column name2']] : 查詢特定範圍(index、colum name)的資料")
print(my_table.loc[[0,2],["name","math"]])
print("="*50)

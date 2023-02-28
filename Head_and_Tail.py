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
print("my_table['name'] : ","取得單一欄位資料(型別為Series)")
print(my_table["name"])
print(type(my_table["name"]))
print("="*50)

print("my_table[['name']] : ","取得單一欄位資料(型別為DataFrame)")
print(my_table[["name"]])
print(type(my_table[["name"]]))
print("="*50)


print("my_table[['name','chinese']] : ","取得多欄位資料(型別為DataFrame)")
print(my_table[["name","chinese"]])
print("="*50)

print("取得索引值(index)0~2的紀錄(資料)")
print(my_table[0:3])

print("at['index','column'] : 特定筆數、特定欄位的資料")
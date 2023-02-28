import pandas

# get data with dict
# dict {key(1st column) : [1st row's data, 2nd row's data, 3rd row's data.....],}
grades = {
    "name" : ["Mike", "Sherry", "Cindy", "John"],
    "math" : [80, 75, 93, 86],
    "chinese" : [63, 90, 85, 70] 
}

# create table of data
my_table = pandas.DataFrame(grades)

print("使用字典建立table(Dataframe)")
print(my_table)
print("="*50)

# custom index and column name of table
my_table.index = ["s1","s2","s3","s4"]  # custom index
my_table.columns = ["Students_Name", "Math_Score", "Chinese_Score"] # custom column name

print("自訂義的每筆資料之index以及欄位名稱")
print(my_table)

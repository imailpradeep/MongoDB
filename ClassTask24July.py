'''
Program aims to complete the following tasks:
    1. Create a  table attribute dataset and dress dataset
    2. Do a bulk load for these two table for respective dataset
    3. read these dataset in pandas as a dataframe
    4. Convert attribute dataset in json format
    5. Store this dataset into mongodb
    6. in sql task try to perform left join operation with attrubute dataset and dress dataset on column Dress_ID
    7. Write a sql query to find out how many unique dress that we have based on dress id
    8. Try to find out how mnay dress is having recommendation 0
    9. Try to find out total dress sell for individual dress id
    10. Try to find out a third highest most selling dress id
'''

import pymongo, pandas as pd, mysql.connector as conn

# Make connection with MySQL and create database
mysqlobj = conn.connect(host = "localhost" , user ="Pradeep" , passwd = "ammaacha")
cursor = mysqlobj.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS July24ClassTask;')
cursor.execute('USE July24ClassTask;')

# Upload files in MySQL
#cursor.execute('LOAD DATA INFILE"C:\Users\prade\Downloads\AttributeDataSet.csv" INTO TABLE Attribute')
#cursor.execute('LOAD DATA INFILE"C:\Users\prade\Downloads\DressSales.csv" INTO TABLE Attribute')
#above upload had unicodeescape error hencce uploaded files using wizard in MySQL workbench

# Upload files using Python and convert to csv format
#df_attribute = pd.read_excel(r"C:\Users\prade\Downloads\AttributeDataSet.xlsx")
#df_dress = pd.read_excel(r"C:\Users\prade\Downloads\DressSales.xlsx")
#a = df_attribute.to_csv()
#b = df_dress.to_csv()
#above upload had unicodeescape error hencce uploaded files using wizard in MySQL workbench

df_attribute = pd.read_sql('select * from July24ClassTask.attribute', mysqlobj)
df_dress = pd.read_sql('select * from July24ClassTask.dresssales', mysqlobj)

print('The attribute table is converted to dataframe', type(df_attribute))
print('The dress sales table is converted to dataframe',type(df_dress))

# Make connection with MongoDB
d = {'23':'adfs'}
a = df_attribute.to_json()


client = pymongo.MongoClient("mongodb+srv://imailpradeep:ammaacha@cluster0.gujy4jv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['July24ClassTask_MongoDB']
collection = database["Attribute_MongoDB"]
#collection.insert_many(d)


cursor.execute('SELECT * FROM attribute;')
record = cursor.fetchall()
for i in record:
    pass #print(i)

cursor.execute('SELECT * FROM dresssales;')
record = cursor.fetchall()
for i in record:
    print(i)
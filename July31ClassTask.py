'''
pip install csvkit
pip install pymysql
pip install pymongo
python -m pip install "pymongo[srv]"
pip install mysql-connector-python
'''

import pandas as pd
import pymongo
import csvkit as cs
import mysql.connector as conn

df_Fitbit = pd.read_csv('D:\iNeuron\FitBit_data.csv')
df_Superstore = pd.read_excel('D:\iNeuron\Superstore_USA.xlsx')

client = pymongo.MongoClient("mongodb+srv://imailpradeep:ammaacha@cluster0.gujy4jv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['FitBit']    # creating database obj.
collection = database['FitBit_data'] # creating collection (just like table in sql)

mysqlobj = conn.connect(host = "localhost" , user ="Pradeep" , passwd = "ammaacha")
cursor = mysqlobj.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS July31ClassTask;')
cursor.execute('USE July31ClassTask;')

json_fitbit = df_Fitbit.to_json("Fitbit.json")
df_json = pd.read_json("Fitbit.json")
print(df_json)
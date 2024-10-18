from pyspark import SparkContext, SparkConf, SQLContext
import pyodbc
import pandas as pd

appName = "PySpark SQL Server Example - via ODBC"
master = "yarn"
conf = SparkConf() \
    .setAppName(appName) \
    .setMaster(master) 
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

database = "test"
table = "dbo.Employees"
user = "sa"
password  = "password123"

conn = pyodbc.connect(f'DRIVER={{ODBC Driver 13 for SQL Server}};SERVER=localhost,31433;DATABASE={database};UID={user};PWD={password}')
query = f"SELECT EmployeeID, EmployeeName, Position FROM {table}"
pdf = pd.read_sql(query, conn)
sparkDF =  spark.createDataFrame(pdf)
sparkDF.show()
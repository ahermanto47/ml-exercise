from pyspark import SparkContext, SparkConf, SQLContext

appName = "PySpark SQL Server Example - via JDBC"
master = "yarn"
conf = SparkConf() \
    .setAppName(appName) \
    .setMaster(master) \
    # .set("spark.driver.extraClassPath","/home/hadoop/spark-3.5.3-bin-hadoop3/python/pyspark/sqljdbc_12.8/enu/jars/mssql-jdbc-12.8.1.jre8.jar")
    .set("spark.driver.extraClassPath","sqljdbc_12.8/enu/jars/mssql-jdbc-12.8.1.jre8.jar")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

database = "TestDB"
table = "dbo.Employees"
user = "sa"
password  = "password123"

jdbcDF = spark.read.format("jdbc") \
    .option("url", f"jdbc:sqlserver://localhost:31433;databaseName={database}") \
    .option("dbtable", "Employees") \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
    .load()

jdbcDF.show()
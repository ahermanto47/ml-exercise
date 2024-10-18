server_name = "jdbc:sqlserver://localhost:31443"
database_name = "TestDB"
url = server_name + ";" + "databaseName=" + database_name + ";"

table_name = "test"
username = "username"
password = "password123" # Please specify password here

jdbcDF = spark.read \
        .format("com.microsoft.sqlserver.jdbc.spark") \
        .option("url", url) \
        .option("dbtable", table_name) \
        .option("user", username) \
        .option("password", password).load()
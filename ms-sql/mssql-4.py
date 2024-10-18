# Set url & credentials
jdbc_url = 'jdbc:sqlserver://192.168.39.29:32462;databaseName=TestDB;Encrypt=False'
sql_username = 'sa'
sql_password = 'password123'

# Fetch the driver manager from your spark context
driver_manager = spark._sc._gateway.jvm.java.sql.DriverManager

# Create a connection object using a jdbc-url, + sql uname & pass
con = driver_manager.getConnection(jdbc_url, sql_username, sql_password)

# Write your SQL statement as a string
# statement = "exec lowerQuantity 160, ?"
# statement = f"""
# EXEC getQuantityByName
#   'banana', ?
# """
statement = "exec ? = getQuantityByName 'banana'"

# Create callable statement and execute it
exec_statement = con.prepareCall(statement)
exec_statement.registerOutParameter(1, spark._sc._gateway.jvm.java.sql.Types.ARRAY)
exec_statement.execute()

result = exec_statement.getInt(1)

print(result)

# Close connections
exec_statement.close()
con.close()
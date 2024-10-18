connection_properties = {
    "user": "sa",
    "password":"password123",
    "driver":"com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

jdbc_url = 'jdbc:sqlserver://192.168.39.29:32462;databaseName=TestDB;Encrypt=False'

statement = """
(
    DECLARE @OutputQuantity int;
    EXECUTE getQuantityByName @Name = 'banana', @Quantity = @OutputQuantity OUTPUT;
    PRINT CONVERT(varchar(10),@OutputQuantity);
    GO
)
"""
jdbc_procDF = spark.read.jdbc(url=jdbc_url, table=statement, properties=connection_properties)
jdbc_procDF.display()
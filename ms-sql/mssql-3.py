jdbcDF = spark.read
            .format('jdbc')
            .option('url', 'jdbc:sqlserver://192.168.39.29:32462;databaseName=TestDB;Encrypt=False')
            .option('user','sa')
            .option('password', 'password123')
            .option('dbtable', 'Inventory')
            .load()

jdbcDF.show()
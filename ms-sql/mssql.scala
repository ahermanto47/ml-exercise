import java.sql.DriverManager
import java.sql.Connection
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Row
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types.{StructType, StructField, StringType,IntegerType};
import java.sql.ResultSet

val username = "sa"
val pass = "password123"
val url = "jdbc:sqlserver://192.168.39.29:32462;databaseName=TestDB;Encrypt=False"

val columns = Seq ("id", "name", "quantity")

val schema = StructType(List(
    StructField("id", StringType, nullable = true),
    StructField("name", StringType,  nullable = true),
    StructField("quantity", StringType,  nullable = true)
))

val conn = DriverManager.getConnection(url, username, pass)
val rs = conn.createStatement.executeQuery("exec getAllItems")

def parseResultSet(rs: ResultSet): Row = {
    val resultSetRecord = columns.map(c => rs.getString(c))
    Row(resultSetRecord:_*)
}

def resultSetToIter(rs: ResultSet)(f: ResultSet => Row): Iterator[Row] = new Iterator[Row] {
    def hasNext: Boolean = rs.next()
    def next(): Row = f(rs)
}

def paralleliseResultSet(rs: ResultSet, spark:SparkSession): DataFrame = {
  val rdd = spark.sparkContext.parallelize(resultSetToIter(rs)(parseResultSet).toSeq)     
  spark.createDataFrame(rdd, schema)
}


val df: DataFrame = paralleliseResultSet(rs,spark)
df.createOrReplaceTempView("df")

spark.sql("""select * from df""").show(10)

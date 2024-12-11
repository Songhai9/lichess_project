from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("Lichess Project") \
    .getOrCreate()

# Verify the Spark session
print(spark.version)

from pyspark.sql import SparkSession

# Minimal Spark session creation
spark = SparkSession.builder \
    .appName("TestSparkSession") \
    .master("local[*]") \
    .getOrCreate()

print("Spark session created successfully!")

# Stop the Spark session
spark.stop()

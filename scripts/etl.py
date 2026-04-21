from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("ETL").getOrCreate()

df = spark.read.parquet("/user/hive/warehouse/ebay_listings_optimized")

df_clean = df.dropDuplicates(["itemId"])

df_clean = df_clean.withColumn(
    "total_price",
    F.coalesce(F.col("price"), F.lit(0)) + F.coalesce(F.col("shipping_cost"), F.lit(0))
)

df_clean.write.mode("overwrite").parquet("/user/processed/ebay")

print("ETL completed")

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Real-Time Fraud Detection") \
    .getOrCreate()

# Simulate streaming source (use static data for now)
df = spark.read.csv("../data/sample_transactions.csv", header=True, inferSchema=True)

# Define simple fraud detection logic
# Example: flag transactions over $10,000 as potentially fraudulent
df_with_flags = df.withColumn(
    "is_fraud",
    when(col("amount") > 10000, 1).otherwise(0)
)

# Show flagged records
fraudulent = df_with_flags.filter(col("is_fraud") == 1)
fraudulent.show()

# Save results as Parquet (simulating Delta Lake)
df_with_flags.write.mode("overwrite").parquet("../data/fraud_results.parquet")

spark.stop()

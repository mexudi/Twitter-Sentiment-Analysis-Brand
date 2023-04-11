import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.appName("KafkaConsumer").getOrCreate()

# Define the schema for the incoming JSON data
schema = StructType([
    StructField("id", IntegerType()),
    StructField("date", StringType()),
    StructField("content", StringType()),
    StructField("username", StringType()),
    StructField("replyCount", IntegerType()),
    StructField("retweetCount", IntegerType()),
    StructField("likeCount", IntegerType())
])

# Read data from Kafka topic as a DataFrame
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "TW_ANALYSIS") \
    .load() \
    .selectExpr("CAST(value AS STRING)")

# Parse the JSON data and display it on the console
df \
    .select(from_json("value", schema).alias("tweet")) \
    .select("tweet.*") \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start() \
    .awaitTermination()

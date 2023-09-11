from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("Read CSV File into DataFrame").getOrCreate()
products = spark.read.csv("products.csv", sep=",", inferSchema=True, header=True)
categories = spark.read.csv("categories.csv", sep=",", inferSchema=True, header=True)
products.join(categories, products.category_id == categories.id, "left").select(
    F.col("product_name"), F.col("category_name")
).show(truncate=False)

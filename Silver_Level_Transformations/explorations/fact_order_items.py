# Databricks notebook source
from pyspark.sql import functions as F
from pyspark.sql.types import *

items_schema = ArrayType(
        StructType(
            [
                StructField("item_id", StringType()),
                StructField("name", StringType()),
                StructField("category", StringType()),
                StructField("quantity", IntegerType()),
                StructField("unit_price", DecimalType(10, 2)),
                StructField("subtotal", DecimalType(10, 2)),
            ]
        )
)

df_fact_order_items = (
        spark.readStream
        .format("delta")
        .table("ws_restaurantanalyticsplatform_7405614613479137.01_bronze.orders")
        .withColumn("order_timestamp", F.to_timestamp(F.col("order_timestamp")))
        .withColumn("items_parsed", F.from_json(F.col("items"), items_schema))
        .withColumn("item", F.explode(F.col("items_parsed")))
        .withColumn("order_date", F.to_date(F.col("order_timestamp")))
        .select(
            "order_id",
            F.col("item.item_id").alias("item_id"),
            "restaurant_id",
            "order_timestamp",
            "order_date",
            F.col("item.name").alias("item_name"),
            F.col("item.category").alias("category"),
            F.col("item.quantity").alias("quantity"),
            F.col("item.unit_price").cast("decimal(10,2)").alias("unit_price"),
            F.col("item.subtotal").cast("decimal(10,2)").alias("subtotal"),
        )
    )

#display(df_fact_order_items)
df_fact_order_items1 = (
        spark.read
        .table("ws_restaurantanalyticsplatform_7405614613479137.01_bronze.orders")
        .withColumn("order_timestamp", F.to_timestamp(F.col("order_timestamp")))
        .withColumn("items_parsed", F.from_json(F.col("items"), items_schema))
)
display(df_fact_order_items1.limit(10), checkpointLocation="/Volumes/ws_restaurantanalyticsplatform_7405614613479137/datafiles/data/checkpoints/exploration_fact_order_items1")

df_fact_order_items2 = (
        spark.read
        .table("ws_restaurantanalyticsplatform_7405614613479137.01_bronze.orders")
        .withColumn("order_timestamp", F.to_timestamp(F.col("order_timestamp")))
        .withColumn("items_parsed", F.from_json(F.col("items"), items_schema))
        .withColumn("item", F.explode(F.col("items_parsed")))
)
display(df_fact_order_items2.limit(10), checkpointLocation="/Volumes/ws_restaurantanalyticsplatform_7405614613479137/datafiles/data/checkpoints/exploration_fact_order_items2")
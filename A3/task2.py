import re
import sys
from operator import add
from pyspark import SQLContext
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.functions import col
from pyspark.sql.types import *

sc = SparkContext.getOrCreate()
spark = SQLContext(sc)
country=sys.argv[1]
df = spark.read.option("header", "true").option("inferschema", "true").csv(sys.argv[1])
dfg= spark.read.option("header", "true").option("inferschema", "true").csv(sys.argv[2])

dfg = dfg.withColumn("LandAverageTemperature", dfg["LandAverageTemperature"].cast(FloatType()))
dfg = dfg.withColumn("dt", dfg["dt"].cast(DateType()))
df = df.withColumn("AverageTemperature", df["AverageTemperature"].cast(FloatType()))
df = df.withColumn("dt", df["dt"].cast(DateType()))

df2 = df.groupBy("dt","Country").max().withColumnRenamed('max(AverageTemperature)','maxTemp')

df3=dfg.join(df2,(df2["dt"] == dfg["dt"]) & (df2["maxTemp"] >dfg["LandAverageTemperature"]))
#df4=df3.groupBy('Country').count().rdd.map(list).sortByKey()
df4=df3.groupBy('Country').count().sort(col("Country")).rdd.map(list)
for i in df4.collect():
    print(i[0],"\t",i[1])
sc.stop()

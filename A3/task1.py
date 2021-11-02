import re
import sys
from operator import add
from pyspark import SQLContext
from pyspark.sql import SparkSession
from pyspark import SparkContext

sc = SparkContext.getOrCreate()
spark = SQLContext(sc)
country=sys.argv[1]

df = spark.read.options(header='True').csv(sys.argv[2]).na.drop().rdd

df3=df.filter(lambda x: x[4] == country).map(lambda x:(x[3],float(x[1])))
df4=df3.groupByKey().mapValues(lambda x:[i for i in x if (i > (sum(x) / len(x)))]).mapValues(len)

for i in df4.collect():
    if(i[1]!=0):
        print("{}\t{}".format(i[0],i[1]))

sc.stop()

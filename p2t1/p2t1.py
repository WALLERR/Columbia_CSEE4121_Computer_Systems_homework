#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.databricks:spark-xml_2.12:0.14.0 pyspark-shell'

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Streaming').getOrCreate()

from pyspark.sql.types import StructType

struct_type = StructType().add('article', 'string').add('rank', 'double')


df = spark.readStream.option("sep", "\t").schema(struct_type).csv("gs://dataproc-staging-us-central1-398592550746-z8akpufv/pagerank_whole")

df_5 = df.select('article', 'rank').where('rank > 0.5')

df_5.writeStream.format("csv").option("delimiter", "\t")    .option("checkpointLocation", "hdfs://cluster-zihao-node1-m/user/root/p2t1")     .option("path", "hdfs://cluster-zihao-node1-m/user/root/p2t1").start()


# In[6]:


df_5.writeStream.format("csv").option("delimiter", "\t")    .option("checkpointLocation", "gs://dataproc-staging-us-central1-398592550746-z8akpufv/pagerank_whole_05")     .option("path", "gs://dataproc-staging-us-central1-398592550746-z8akpufv/pagerank_whole_05").start()


# In[10]:


from pyspark.sql import SparkSession


whole_path = 'gs://dataproc-staging-us-central1-398592550746-z8akpufv/pagerank_whole_05'
spark = SparkSession.builder.getOrCreate()
dt = spark.read.option("delimiter", "\t").option("header", False).csv(whole_path + "/*.csv")


# In[11]:


dt.count()


# In[ ]:





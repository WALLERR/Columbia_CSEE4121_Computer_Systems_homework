#!/usr/bin/env python
# coding: utf-8

# In[1]:


#set-up
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.databricks:spark-xml_2.12:0.14.0 pyspark-shell'

import regex
from pyspark.sql.functions import explode, udf, col, lower, when
from pyspark.sql.types import ArrayType, StringType


# In[2]:


from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()


# In[3]:


# load the data as a dataframe
df = spark.read.format('xml').options(rowTag='page').load('hdfs:/enwiki_small.xml')


# In[4]:


# we define a function that breaks down the text in our revision colunm into the links inside the brakets and apply 
# the logic listed in the assignment: filtering out links containing ':' and '#' and only including the first link 
#if multiple links are present. 

def return_links(text):
    try:
        matches = regex.findall(r'\[\[((?:[^[\]]+|(?R))*+)\]\]', text)
    except:
        matches = []
    output = []
    for match in matches:
        for link in match.split('|'):
            if ':' in link and 'Category:' not in link:
                continue
            elif '#' in link:
                continue
            else:
                output.append(link.lower())
                break
    return output

return_links_udf = udf(lambda text: return_links(text), ArrayType(StringType()))


# In[5]:


#We select only the columns of interest from our dataframe. we only want the 'title' 
#and the 'revision' columns saved as 'text'
new_test = df.select(col('title'), col('revision.text._VALUE').alias('text'))


# In[6]:


#Now we can apply our equation which returns all hyperlinks included between brackets and applies the logic necessary. 
new_test = new_test.withColumn('inner_links', explode(return_links_udf(col('text'))))


# In[7]:


#We take the results and ensure all results are lowercase, turning any uppercase leters to lowercase. 
new_test = new_test.select(lower(col('title')).alias('new_title'), lower(col('inner_links')).alias('new_inner_links'))


# In[8]:


#Drop na fields
new_test = new_test.select(col('new_title'),col('new_inner_links')).na.drop()


# In[9]:


#sort in ascending order 
new_test= new_test.select(col('new_title'),col('new_inner_links')).sort(["new_title","new_inner_links"],ascending=True)


# In[12]:


#save the output as a cvs file
new_test.limit(5).write.option('delimeter', '\t').csv('gs://adrianstorage/p1t2', mode = 'overwrite')


# In[13]:


new_test.coalesce(1).write.option('delimeter', '\t').csv('gs://adrianstorage/p1t2_whole', mode = 'overwrite')


# In[ ]:





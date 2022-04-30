#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark import SparkContext
from pyspark.sql import SparkSession
import pandas as pd

from collections import Counter
sc = SparkContext()


# In[3]:


spark = spark = SparkSession.builder.appName("how to read csv file").getOrCreate()
df = spark.read.csv("gs://dataproc-staging-us-central1-398592550746-z8akpufv/task2_small/part-00000-f4c8cb20-2045-4202-866c-e138fddf3b19-c000.csv",
                    inferSchema=True, header=False)


# In[4]:


df.show()


# In[5]:


data = [
    ("article1", "article2"), 
    ("article1", "article3"),
    ("article1", "article4"), 
    ("article2", "article1"), 
    ("article3", "article1"),
    ("article5", "article1")
]
rdd = sc.parallelize(data)


# In[25]:


def get_articles(input_file):
    articles = {}
    counter = []
    for item in input_file.collect():
        article_left, article_right = item
        counter.append(article_left)

        if article_right not in articles:
            articles[article_right] = [article_left]
        else:
            articles[article_right].append(article_left)
            
        if article_left not in articles:
            articles[article_left] = []
    counter = Counter(counter)

    return articles, counter

def get_ranks(articles):
    ranks = {}
    for article in articles:
        ranks[article] = 1
    return ranks

def get_contributions(articles, ranks, counter):
    contributions = {}
    for article in articles:
        contributions[article] = 0
        neighbors = articles[article]
        for neighbor in neighbors:
            if neighbor not in ranks:
                contributions[neighbor] = 0
                print('log')
            contributions[article] += ranks[neighbor] / counter[neighbor]
    return contributions

def update_ranks(ranks, contributions):
    for article in ranks:
        ranks[article] = 0.15 + 0.85 * contributions[article]
    return ranks

def main():
    articles, counter = get_articles(df)
    ranks = get_ranks(articles)
    for i in range(10):
        contributions = get_contributions(articles, ranks, counter)
        ranks = update_ranks(ranks, contributions)
#     print(ranks)
    return ranks

if __name__ == '__main__':
    ranks = main()


# In[26]:


dt = pd.DataFrame(ranks.items(), columns=['article', 'rank'])
dt = dt.sort_values(by=["article", "rank"], ascending=True)
dt.head(5)


# In[29]:


dt[dt['rank'] != 0.15].sort_values(by=["article", "rank"], ascending=True).head(5).to_csv('gs://dataproc-staging-us-central1-398592550746-z8akpufv/p1t3.csv', index=False)


# In[ ]:





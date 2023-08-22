# from functools import reduce
# from collections import defaultdict
# import re
# import time

# with open("randomtext.txt","r") as f:
#     text = f.read()

# def map_function(line):
#     words = line.split()
#     words_count = defaultdict(int)
#     pattern = r'\.|,|:|;|-'

#     for word in words:
#         word_repl = re.sub(pattern,"",word)
#         words_count[word_repl.lower()] += 1
#     return words_count.items()

# def reduce_function(map,counts):
#     return map,sum(counts)


# start_time = time.time()
# lines = text.split("\n")

# mapped_data = map(map_function,lines)

# #Shuffle and Sort

# intermediate = defaultdict(list)
# for word_count_pairs in mapped_data:
#     for word, count in word_count_pairs:
#         intermediate[word].append(count)

# #Reduce

# words_counts = []
# for item in intermediate.items():
#     result = reduce(reduce_function,item)
#     words_counts.append(result)

# with open("word_count.txt","w") as f:
#     for word_count in words_counts:
#         f.write(str(word_count) + "\n")

# result_time = time.time() - start_time
# print("Result time " + str(result_time))#0.007001161575317383
# from functools import reduce

# values = [4,7,3,9,2,6,10,1,12]

# def higher(a,b):
#     print((a,b))
#     if a > b:
#         return a
#     else:
#         return b

# def sum(a,b):
#     print((a,b))
#     return a + b
    
# result = reduce(higher,values)
# print(result)

# result = reduce(sum,values)
# print(result)

# from functools import reduce
# from collections import defaultdict

# data = [("Alice", 85), ("Bob", 92), ("Alice", 78), ("Bob", 95), ("Charlie", 89)]

# def map_function(item):
#     student,score = item
#     return student,(score,1)

# def reduce_function(student,score_count_pairs):
#     total_score = sum(score for score,count in score_count_pairs)
#     total_count = sum(count for score,count in score_count_pairs)
#     average_score = total_score / total_count
#     return student,average_score

# mapped_data = map(map_function,data)

# intermdediate = defaultdict(list)
# for student,score_count_pair in mapped_data:
#     intermdediate[student].append(score_count_pair)

# average_scores = []
# for item in intermdediate.items():
#     result = reduce(reduce_function,item)
#     average_scores.append(result)

# print(average_scores)

# from pyspark import SparkContext,SparkConf
# import re
# import time

# def map_word(word):
#     pattern = r'\.|,|:|;|-'
#     word_repl = re.sub(pattern,"",word)
#     return (word_repl,1)


# conf = SparkConf().setAppName("WordCount")
# sc = SparkContext(conf=conf)

# lines = sc.textFile("randomtext.txt")

# start_time = time.time()
# word_counts = lines.flatMap(lambda line:line.split()).map(map_word).reduceByKey(lambda a,b:a+b)

# with open("word_count2.txt","w") as f:
#     for (word,count) in word_counts.collect():
#         f.write(str((word,count))+"\n")

# result_time = time.time() - start_time#4.2850182056427
# print("Result time : " + str(result_time))
# sc.stop()

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("AverageScore").getOrCreate()

data = spark.read.options(delimiter=";").csv("Student_scores.csv",header=True,inferSchema=True)
average_scores = data.groupBy("Name").agg(avg("Score").alias("average_score"))

average_scores.show()
spark.stop()
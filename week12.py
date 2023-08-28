from pyspark.sql import SparkSession
from pyspark.sql.functions import sum


# spark = SparkSession.builder.appName("RDDExampleApp").getOrCreate()
spark = SparkSession.builder.appName("SparkDFsExampleApp").getOrCreate()


# def sum(a, b):
#     return a + b


# def to_word_init(word):
#     return (word, 1)


# def line_split(line):
#     return line.split()


# test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# rdd = spark.sparkContext.parallelize(test_data)

# rdd_squared = rdd.map(lambda x: x * x)
# rdd_sum = rdd_squared.reduce(sum)
# rdd_odd_numbers = rdd.filter(lambda x: x % 2 != 0)

# print("\n\n\n\n")
# print("Squared RDD : ", rdd_squared.collect())
# print("Sumed RDD : ", rdd_sum)
# print("Odd numbers : ", rdd_odd_numbers.collect())
# print("\n\n\n\n")

# rnd_text_rdd = spark.sparkContext.textFile("randomtext.txt")

# # word_count_rdd = (
# #     rnd_text_rdd.flatMap(lambda line: line.split())#for each line we get all the word (split at space)
# #     .map(lambda word: (word, 1))#(any_word,1)
# #     .reduceByKey(lamda a,b:a+b)#(any_word,1), (any_word,1) ---> (any_word,2),(any_word,1) --->
# #      # (any_word,3)
# # )

# word_count_rdd = rnd_text_rdd.flatMap(line_split).map(to_word_init).reduceByKey(sum)


# # print("Word counts",word_count_rdd.collect())
# with open("WordCountRDD.txt", "w") as f:
#     f.write(str(word_count_rdd.collect()))


# text_rdd = spark.sparkContext.textFile("randomtext.txt")

# a_b_count_rdd = (
#     text_rdd.flatMap(line_split)
#     .filter(lambda word: word.startswith("a") or word.startswith("b"))
#     .map(to_word_init).reduceByKey(sum)
# )

# with open("WordCountRDD_a_b.txt", "w") as f:
#     f.write(str(a_b_count_rdd.collect()))

# DataFrames

df = spark.read.option("sep",";").csv("Student_scores.csv", header=True, inferSchema=True)
# df.show()

# print("\n\n\n\n\n\n")
# print(df.dtypes)

# df.select(sum(df.Score)).show()
# print("\n\n\nStudents scores sum:",df.select(sum(df.Score).alias("all_scores_sum")).first())
# print("\n\n\nStudents scores sum:",df.select(sum(df.Score).alias("all_scores_sum")).first().all_scores_sum,"\n\n\n\n")

# df.groupBy("Name").avg("Score").show()

# print("\n")
# good_students_df = df.filter(df["Score"] > 5)
# good_students_df.show()

df_2 = spark.read.option("sep",";").csv("Student_profiles.csv", header=True, inferSchema=True)

df.createOrReplaceTempView("student_scores")
df_2.createOrReplaceTempView("student_profile")

query = """SELECT a.Name,a.Score,b.Age FROM student_scores AS a 
       JOIN student_profile AS b ON
     a.Name = b.Name"""

result_df = spark.sql(query)
result_df.show()

query = """SELECT Name,round(avg(Score),2) AS average_value FROM student_scores
  GROUP BY Name"""

result_df = spark.sql(query)
result_df.show()

spark.sparkContext.stop()

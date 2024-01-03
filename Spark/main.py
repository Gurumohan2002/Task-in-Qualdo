from pyspark.sql import SparkSession
from pyspark.sql.functions import mean as mean_, std as std_,col
from pyspark.sql.functions import min as minimum_, median as median_ , max as maximum_
import pyspark.sql.functions as F
from pyspark.sql.functions import length

spark = SparkSession.builder.appName("Read CSV from GCS").getOrCreate()

keyfile_path = "C:\\Users\\HI\\Qualdo_Tasks\\Spark\\bustling-syntax-405306-419798141eca.json"
spark._jsc.hadoopConfiguration().set("google.cloud.auth.service.account.json.keyfile", keyfile_path)

bucket_name = "new_file"
file_path = f"gs://{bucket_name}/dest_file_name.csv"

df = spark.read.csv(file_path, header=True)
# df.show()


#Creating a dataframe manually and printing the rows in which the given specific column does not have the null values in it  
def new_task1():
    df1 = spark.createDataFrame([ ("A", 1, None), ("B", None, "123" ), ("B", 3, "456"), ("D", None, None), ], ["Name", "Value", "id"]) 
    
    #Here checking for only one specific column with null values
    print("\nThe rows in which the Value Column has no null values in it:")
    df2 = df1.na.drop(subset='Value')  
    df2.show()
    # df1.show()
    
    print("\nThe rows in which the Value Column and id Column has no null values in it:")
    #Here checking for the multiple columns with null values
    df2=df1.na.drop(subset=["Value","id"])
    df2.show()
    # df1.show()

# For Printing the average and standard deviation for any column with numeric value
def avg_and_mean():
    
    df_0 = df.select(
    mean_(col('AveragePrice')).alias('mean'),
    std_(col('AveragePrice')).alias('std')).collect()
    avg = df_0[0]['mean']
    std = df_0[0]['std']
    
    print(f"\nThe Average value of the column 'AveragePrice':{avg}")
    print(f"\nThe standard deviation value for the column 'AveragePrice':{std}\n")

# For counting the words with their count and printing the maximum 5 words with high count
def count_of_top_5_words(): 
    
    df_1=df   
    print("\nThe count of words with their top 5 highest count in the specific column '4046':")
    df_1.groupBy('4046').count().orderBy('count', ascending=False).show(5)

# For calculating the minimum ,maximum , median ,25th percentile and 75th percentile for a numeric column
def min_max_median_25_75():
    
    df_3=df
    df_2 = df.select(
        minimum_(col('AveragePrice')).alias('min'),
        median_(col('AveragePrice')).alias('median'),
        maximum_(col('AveragePrice')).alias('max')
    ).collect()

    min = df_2[0]['min']
    median = df_2[0]['median']
    max = df_2[0]['max'] 
    
    print(f"\nThe minimum value for thr AveragePrice column is:{min}")
    print(f"\nThe median value for the AveragePrice column is : {median}")
    print(f"\nThe maximum value for the AveragePrice column is :{max}\n")
    print("The 25th pecentile and 75th percentile by grouping the type column:")
    df_4 = df_3.groupby('type').agg(F.expr('percentile(AveragePrice, array(0.25))')[0].alias('%25'),
                                F.expr('percentile(AveragePrice, array(0.75))')[0].alias('%75'))

    df_4.show()
    print("After joining the both dataframes:")
    df_3.join(df_4, on='type', how='left').show()

# For changing the column name in the dataframe
def change_column_name():
    print("\nBefore  Changing the column name from the dataframe :")
    df.printSchema()
    
    print("\nAfter Changing the column name from the dataframe :")
    df.withColumnRenamed("AveragePrice","avg_price").printSchema()

# To get the count of number of characters from the given specific columns
def num_of_char():
    print("\nThe number of characters in the region Column with its length:")
    wordsLengthsDF =df.select("region",length('region').alias('lengths'))
    wordsLengthsDF.show()
    
# Main function    
def main():
    avg_and_mean()
    # count_of_top_5_words()
    # min_max_median_25_75()
    # change_column_name()
    # num_of_char()
    # new_task1()

# Calling main function
if __name__ == "__main__":
    main()
#!/usr/bin/env python
# coding: utf-8

# ## SilverLayer_DataTransformation
# 
# null

# In[23]:


# Welcome to your new notebook
# Type here in the cell editor to add code!

from pyspark.sql.functions import *


# In[24]:


try:
    bronzefileName
except NameError:
    bronzefileName = "cc_add.csv"  # default for manual runs


# In[25]:


path = f"abfss://62a7fe2a-4553-4bdb-b9f1-eeffec628df4@onelake.dfs.fabric.microsoft.com/62e6144e-112d-4d99-9746-09dab6a01bd7/Files/CreditCardFiles/{bronzefileName}"



#print(path)


# In[26]:


df = spark.read.format("csv").option("header", "true").load(path)

#display(df)


# In[27]:


# Add AgeGroup column

df = df.withColumn(
    "Revenue",
    col("Annual_Fees") + col("Total_Trans_Amt") + col("Interest_Earned")
)

#display(df)


# In[28]:


from pyspark.sql.functions import col, to_date, datediff, floor

df = df.withColumn(
    "Week_Number",
    floor(datediff(to_date(col("Week_Start_Date"), "dd-MM-yyyy"),
                    to_date(concat(col("current_year"), lit("-01-01")))) / 7) + 1
)

#display(df)


# In[29]:


df = df.withColumnRenamed("Use Chip", "use_chip")\
        .withColumnRenamed("Exp Type", "Exp_Type")


#display(df)


# In[30]:


int_columns = ["Client_Num", "Annual_Fees", "Activation_30_Days", "Customer_Acq_Cost", "current_year", "Credit_Limit", "Total_Revolving_Bal", "Total_Trans_Amt", "Total_Trans_Vol", "Delinquent_Acc" ]

for c in int_columns:
    df = df.withColumn(c, col(c).cast("int"))


float_columns = ["Avg_Utilization_Ratio", "Interest_Earned"]

for c in float_columns:
    df = df.withColumn(c, col(c).cast("float"))


df = df.withColumn(
    "Week_Start_Date",
    to_date(col("Week_Start_Date"), "dd-MM-yyyy")
)


#display(df)


# In[31]:


display(df)


# In[32]:


df.write \
  .format("delta") \
  .mode("append") \
  .saveAsTable("creditcard_silver_Table")


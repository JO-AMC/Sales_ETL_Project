#Importing libraries
import pandas as pd

df = pd.read_csv("C:\\Users\\God\\Desktop\\Sales_ETL_Project\\data\\raw\\SalesData.csv")

print(df.head(3))

#checking total null rows
print(df.isnull().sum())

#Remove null values
df = df.dropna()

#Cheching Duplicates
df = df.drop_duplicates()

print(df.shape)

#Save Cleaned Data
df.to_csv("C:\\Users\\God\\Desktop\\Sales_ETL_Project\\data\\cleaned\\Cleaned_SalesData.csv", index=False)

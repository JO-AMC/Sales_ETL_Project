import pandas as pd
from sqlalchemy import create_engine

#Read cleanned data
df = pd.read_csv("C:\\Users\\God\\Desktop\\Sales_ETL_Project\\data\\cleaned\\Cleaned_SalesData.csv")

#Mysql connection
engine = create_engine(
    "mysql+pymysql://root:John%402007@localhost:3306/sales_etl"
)
#change column names
df.columns = [
    "Order_ID",
    "Product",
    "Quantity_Ordered",
    "Price_Each",
    "Order_Date",
    "Purchase_Address"
]

#Load data
df.to_sql("Sales", con=engine, if_exists="append", index = False)

print("Data Loaded Successfully!")

use sales_etl;
select * from sales

select count(Order_ID) as Total_Orders from Sales;

select count(distinct Order_ID) as Total_Orders from sales;

select sum(Quantity_Ordered) as Total_Quantity from sales;

select avg(Quantity_ordered * Price_Each) as Average_Order_Value from sales;

select sum((Price_Each - 30) * Quantity_Ordered) as Total_Profit from Sales;

select Product,sum(Quantity_Ordered * Price_Each) as Sales 
from Sales 
group by Product 
order by Sales DESC 
limit 10
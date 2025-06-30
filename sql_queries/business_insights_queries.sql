Business Question 1: What are our total sales and profit?
SELECT
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit
FROM sales;

Business Question 2: What are our best-selling product categories?
SELECT
    Category,
    SUM(Sales) AS TotalSales,
    COUNT(OrderID) AS NumberOfOrders
FROM sales
GROUP BY Category
ORDER BY TotalSales DESC;

Business Question 3: Who are our Top 10 most valuable customers?
SELECT
    CustomerName,
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit
FROM sales
GROUP BY CustomerName
ORDER BY TotalSales DESC
LIMIT 10;

Business Question 4: How are sales performing on a monthly basis?
-- For SQLite, we use strftime. In other SQL versions, you might use DATE_TRUNC or other functions.
SELECT
    strftime('%Y-%m', OrderDate) AS SalesMonth,
    SUM(Sales) AS MonthlySales,
    SUM(Profit) AS MonthlyProfit
FROM sales
GROUP BY SalesMonth
ORDER BY SalesMonth;

Business Question 5: Which region is the most profitable?
SELECT
    Region,
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit,
    AVG(ProfitMargin) AS AverageProfitMargin
FROM sales
GROUP BY Region
ORDER BY TotalProfit DESC;


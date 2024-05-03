SELECT product_id, SUM(total) as total_sales
FROM cognizant.s1
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 10;


SELECT category, AVG(unit_price) as average_unit_price
FROM cognizant.s1
GROUP BY category
ORDER BY average_unit_price DESC;

SELECT customer_type, AVG(quantity) as average_quantity_sold
FROM cognizant.s1
GROUP BY customer_type;

SELECT day_of_week, AVG(total) as average_sales
FROM  cognizant.s1
GROUP BY day_of_week
ORDER BY average_sales DESC;

SELECT category, AVG(quantity) as average_quantity_per_transaction
FROM cognizant.s1
GROUP BY category
ORDER BY average_quantity_per_transaction DESC
LIMIT 1;


SELECT day_of_week, customer_type, AVG(total) as average_sales
FROM cognizant.s1
GROUP BY day_of_week, customer_type
ORDER BY customer_type DESC;

SELECT day_of_week, customer_type, AVG(total) as average_sales
FROM cognizant.s1
GROUP BY day_of_week, customer_type
ORDER BY CASE
           WHEN day_of_week = 'Monday' THEN 1
           WHEN day_of_week = 'Tuesday' THEN 2
           WHEN day_of_week = 'Wednesday' THEN 3
           WHEN day_of_week = 'Thursday' THEN 4
           WHEN day_of_week = 'Friday' THEN 5
           WHEN day_of_week = 'Saturday' THEN 6
           WHEN day_of_week = 'Sunday' THEN 7
           ELSE 8
         END;
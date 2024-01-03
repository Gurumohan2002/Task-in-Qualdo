CREATE DATABASE sqltask;
USE sqltask;
CREATE TABLE orders (
    ord_no INT PRIMARY KEY,
    purch_amt NUMERIC,
    ord_date DATE,
    customer_id INT,
    salesman_id INT
);

INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id)
VALUES
    (70001, 150.5, '2012-10-05', 3005, 5002),
    (70009, 270.65, '2012-09-10', 3001, 5005),
    (70002, 65.26, '2012-10-05', 3002, 5001),
    (70004, 110.5, '2012-08-17', 3009, 5003),
    (70007, 948.5, '2012-09-10', 3005, 5002),
    (70005, 2400.6, '2012-07-27', 3007, 5001),
    (70008, 5760, '2012-09-10', 3002, 5001),
    (70010, 1983.43, '2012-10-10', 3004, 5006),
    (70003, 2480.4, '2012-10-10', 3009, 5003),
    (70012, 250.45, '2012-06-27', 3008, 5002),
    (70011, 75.29, '2012-08-17', 3003, 5007),
    (70013, 3045.6, '2012-04-25', 3002, 5001);


 Select * from orders;
+--------+-----------+------------+-------------+-------------+
| ord_no | purch_amt | ord_date   | customer_id | salesman_id |
+--------+-----------+------------+-------------+-------------+
|  70001 |       151 | 2012-10-05 |        3005 |        5002 |
|  70002 |        65 | 2012-10-05 |        3002 |        5001 |
|  70003 |      2480 | 2012-10-10 |        3009 |        5003 |
|  70004 |       111 | 2012-08-17 |        3009 |        5003 |
|  70005 |      2401 | 2012-07-27 |        3007 |        5001 |
|  70007 |       949 | 2012-09-10 |        3005 |        5002 |
|  70008 |      5760 | 2012-09-10 |        3002 |        5001 |
|  70009 |       271 | 2012-09-10 |        3001 |        5005 |
|  70010 |      1983 | 2012-10-10 |        3004 |        5006 |
|  70011 |        75 | 2012-08-17 |        3003 |        5007 |
|  70012 |       250 | 2012-06-27 |        3008 |        5002 |
|  70013 |      3046 | 2012-04-25 |        3002 |        5001 |
+--------+-----------+------------+-------------+-------------+

-- SELECT count(purch_amt) as Count,sum(purch_amt) as Total,salesman_id from orders GROUP BY salesman_id having Total<2000 ORDER BY Total DESC;

-- +-------+-------+-------------+
-- | Count | Total | salesman_id |
-- +-------+-------+-------------+
-- |     1 |    75 |        5007 |
-- |     1 |   271 |        5005 |
-- |     3 |  1350 |        5002 |
-- |     1 |  1983 |        5006 |
-- +-------+-------+-------------+

-- Select distinct(salesman_id) from orders group by salesman_id having purch_amt<2000 order by purch_amt desc;


-- Select salesman_id,max(purch_amt) from orders where purch_amt<2000 group by salesman_id,purch_amt order by purch_amt desc limit 5;

-- +-------------+-----------+
-- | salesman_id | purch_amt |
-- +-------------+-----------+
-- |        5006 |      1983 |
-- |        5002 |       949 |
-- |        5005 |       271 |
-- |        5002 |       250 |
-- |        5002 |       151 |
-- +-------------+-----------+

 Select salesman_id from orders where purch_amt<2000 group by salesman_id order by max(purch_amt) desc limit 5;

+-------------+----------------+
| salesman_id | max(purch_amt) |
+-------------+----------------+
|        5006 |           1983 |
|        5002 |            949 |
|        5005 |            271 |
|        5003 |            111 |
|        5007 |             75 |
+-------------+----------------+

Select salesman_id from orders where purch_amt<2000 group by salesman_id order by max(purch_amt) desc limit 5;
+-------------+
| salesman_id |
+-------------+
|        5006 |
|        5002 |
|        5005 |
|        5003 |
|        5007 |
+-------------+

-- SELECT count(purch_amt) as Count,sum(purch_amt) as Total,salesman_id from orders GROUP BY salesman_id having Total>100 ORDER BY Total;

-- +-------+-------+-------------+
-- | Count | Total | salesman_id |
-- +-------+-------+-------------+
-- |     1 |   271 |        5005 |
-- |     3 |  1350 |        5002 |
-- |     1 |  1983 |        5006 |
-- |     2 |  2591 |        5003 |
-- |     4 | 11272 |        5001 |
-- +-------+-------+-------------+

-- select distinct salesman_id from orders where purch_amt <= 2000 order by purch_amt desc limit 5;

-- SELECT distinct(salesman_id),purch_amt from orders where purch_amt>100 GROUP BY salesman_id,purch_amt  ORDER BY purch_amt asc limit 5;

-- +-------------+-----------+
-- | salesman_id | purch_amt |
-- +-------------+-----------+
-- |        5003 |       111 |
-- |        5002 |       151 |
-- |        5002 |       250 |
-- |        5005 |       271 |
-- |        5002 |       949 |
-- +-------------+-----------+

Select salesman_id from orders where purch_amt<2000 group by salesman_id order by max(purch_amt) asc limit 5;

+-------------+----------------+
| salesman_id | max(purch_amt) |
+-------------+----------------+
|        5001 |             65 |
|        5007 |             75 |
|        5003 |            111 |
|        5005 |            271 |
|        5002 |            949 |
+-------------+----------------+

Select salesman_id from orders where purch_amt<2000 group by salesman_id order by max(purch_amt) asc limit 5;
+-------------+
| salesman_id |
+-------------+
|        5001 |
|        5007 |
|        5003 |
|        5005 |
|        5002 |
+-------------+
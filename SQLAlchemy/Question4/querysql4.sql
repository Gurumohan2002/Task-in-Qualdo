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

Select * from salesman;
+-------------+------------+----------+------------+
| salesman_id | name       | city     | commission |
+-------------+------------+----------+------------+
|        5001 | James Hoog | New York |       0.15 |
|        5002 | Nail Knite | Paris    |       0.13 |
|        5003 | Lauson Hen | San Jose |       0.12 |
|        5005 | Pit Alex   | London   |       0.11 |
|        5006 | Mc Lyon    | Paris    |       0.14 |
|        5007 | Paul Adam  | Rome     |       0.13 |
+-------------+------------+----------+------------+

CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    cust_name VARCHAR(255),
    city VARCHAR(255),
    grade INT,
    salesman_id INT
);

INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id)
VALUES
    (3002, 'Nick Rimando', 'New York', 100, 5001),
    (3007, 'Brad Davis', 'New York', 200, 5001),
    (3005, 'Graham Zusi', 'California', 200, 5002),
    (3008, 'Julian Green', 'London', 300, 5002),
    (3004, 'Fabian Johnson', 'Paris', 300, 5006),
    (3009, 'Geoff Cameron', 'Berlin', 100, 5003),
    (3003, 'Jozy Altidor', 'Moscow', 200, 5007),
    (3001, 'Brad Guzan', 'London', NULL, 5005);

 Select * from customer;
+-------------+----------------+------------+-------+-------------+
| customer_id | cust_name      | city       | grade | salesman_id |
+-------------+----------------+------------+-------+-------------+
|        3001 | Brad Guzan     | London     |  NULL |        5005 |
|        3002 | Nick Rimando   | New York   |   100 |        5001 |
|        3003 | Jozy Altidor   | Moscow     |   200 |        5007 |
|        3004 | Fabian Johnson | Paris      |   300 |        5006 |
|        3005 | Graham Zusi    | California |   200 |        5002 |
|        3007 | Brad Davis     | New York   |   200 |        5001 |
|        3008 | Julian Green   | London     |   300 |        5002 |
|        3009 | Geoff Cameron  | Berlin     |   100 |        5003 |
+-------------+----------------+------------+-------+-------------+


Select c.cust_name,c.city,c.grade,s.name,o.ord_no,o.ord_date,o.purch_amt 
from salesman as s
inner join  customer as c on s.salesman_id=c.salesman_id 
inner join orders as o on c.customer_id=o.customer_id
having c.grade is not null and o.purch_amt>2000;


+---------------+----------+-------+------------+--------+------------+-----------+
| cust_name     | city     | grade | name       | ord_no | ord_date   | purch_amt |
+---------------+----------+-------+------------+--------+------------+-----------+
| Geoff Cameron | Berlin   |   100 | Lauson Hen |  70003 | 2012-10-10 |      2480 |
| Brad Davis    | New York |   200 | James Hoog |  70005 | 2012-07-27 |      2401 |
| Nick Rimando  | New York |   100 | James Hoog |  70008 | 2012-09-10 |      5760 |
| Nick Rimando  | New York |   100 | James Hoog |  70013 | 2012-04-25 |      3046 |
+---------------+----------+-------+------------+--------+------------+-----------+


SELECT c.cust_name, c.city, o.ord_no, o.ord_date, o.purch_amt as Order_Amount
FROM customer AS c
INNER JOIN orders AS o ON c.customer_id = o.customer_id
where c.grade is not null;


+----------------+------------+--------+------------+--------------+
| cust_name      | city       | ord_no | ord_date   | Order_Amount |
+----------------+------------+--------+------------+--------------+
| Graham Zusi    | California |  70001 | 2012-10-05 |          151 |
| Nick Rimando   | New York   |  70002 | 2012-10-05 |           65 |
| Geoff Cameron  | Berlin     |  70003 | 2012-10-10 |         2480 |
| Geoff Cameron  | Berlin     |  70004 | 2012-08-17 |          111 |
| Brad Davis     | New York   |  70005 | 2012-07-27 |         2401 |
| Graham Zusi    | California |  70007 | 2012-09-10 |          949 |
| Nick Rimando   | New York   |  70008 | 2012-09-10 |         5760 |
| Fabian Johnson | Paris      |  70010 | 2012-10-10 |         1983 |
| Jozy Altidor   | Moscow     |  70011 | 2012-08-17 |           75 |
| Julian Green   | London     |  70012 | 2012-06-27 |          250 |
| Nick Rimando   | New York   |  70013 | 2012-04-25 |         3046 |
+----------------+------------+--------+------------+--------------+

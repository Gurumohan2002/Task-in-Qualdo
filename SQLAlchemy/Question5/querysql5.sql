CREATE TABLE employee (
    emp_idno INT PRIMARY KEY,
    emp_fname VARCHAR(255),
    emp_lname VARCHAR(255),
    emp_dept INT
);

INSERT INTO employee (emp_idno, emp_fname, emp_lname, emp_dept)
VALUES
    (127323, 'Michale', 'Robbin', 57),
    (526689, 'Carlos', 'Snares', 63),
    (843795, 'Enric', 'Dosio', 57),
    (328717, 'Jhon', 'Snares', 63),
    (444527, 'Joseph', 'Dosni', 47),
    (659831, 'Zanifer', 'Emily', 47),
    (847674, 'Kuleswar', 'Sitaraman', 57),
    (748681, 'Henrey', 'Gabriel', 47),
    (555935, 'Alex', 'Manuel', 57),
    (539569, 'George', 'Mardy', 27),
    (733843, 'Mario', 'Saule', 63),
    (631548, 'Alan', 'Snappy', 27),
    (839139, 'Maria', 'Foster', 57);

Select * from employee;
+----------+-----------+-----------+----------+
| emp_idno | emp_fname | emp_lname | emp_dept |
+----------+-----------+-----------+----------+
|   127323 | Michale   | Robbin    |       57 |
|   328717 | Jhon      | Snares    |       63 |
|   444527 | Joseph    | Dosni     |       47 |
|   526689 | Carlos    | Snares    |       63 |
|   539569 | George    | Mardy     |       27 |
|   555935 | Alex      | Manuel    |       57 |
|   631548 | Alan      | Snappy    |       27 |
|   659831 | Zanifer   | Emily     |       47 |
|   733843 | Mario     | Saule     |       63 |
|   748681 | Henrey    | Gabriel   |       47 |
|   839139 | Maria     | Foster    |       57 |
|   843795 | Enric     | Dosio     |       57 |
|   847674 | Kuleswar  | Sitaraman |       57 |
+----------+-----------+-----------+----------+

CREATE TABLE department (
    dpt_code INT PRIMARY KEY,
    dpt_name VARCHAR(255),
    dpt_allotment INT
);

INSERT INTO department (dpt_code, dpt_name, dpt_allotment)
VALUES
    (57, 'IT', 65000),
    (63, 'Finance', 15000),
    (47, 'HR', 240000),
    (27, 'RD', 55000),
    (89, 'QC', 75000);


 Select * from  department;
+----------+----------+---------------+
| dpt_code | dpt_name | dpt_allotment |
+----------+----------+---------------+
|       27 | RD       |         55000 |
|       47 | HR       |        240000 |
|       57 | IT       |         65000 |
|       63 | Finance  |         15000 |
|       89 | QC       |         75000 |
+----------+----------+---------------+ 

Select e.emp_fname,e.emp_lname from employee as e join department as d 
on e.emp_dept=d.dpt_code where dpt_allotment>50000;

+-----------+-----------+
| emp_fname | emp_lname |
+-----------+-----------+
| Michale   | Robbin    |
| Joseph    | Dosni     |
| George    | Mardy     |
| Alex      | Manuel    |
| Alan      | Snappy    |
| Zanifer   | Emily     |
| Henrey    | Gabriel   |
| Maria     | Foster    |
| Enric     | Dosio     |
| Kuleswar  | Sitaraman |
+-----------+-----------+


Select e.emp_fname,e.emp_lname from employee as e join department as d 
on e.emp_dept=d.dpt_code where d.dpt_allotment = 
(Select min(dpt_allotment) from department where 
dpt_allotment>(select min(dpt_allotment) from department));

+-----------+-----------+
| emp_fname | emp_lname |
+-----------+-----------+
| George    | Mardy     |
| Alan      | Snappy    |
+-----------+-----------+







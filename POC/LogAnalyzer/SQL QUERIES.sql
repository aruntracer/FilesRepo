DDL/DML:
CREATE TABLE MSSINT.TEST_DATA(EMP_ID NUMBER,EMP_NAME VARCHAR2(200),SALARY NUMBER,DEPT_ID NUMBER);
INSERT INTO MSSINT.TEST_DATA VALUES(1,'AK',2000,10);
INSERT INTO MSSINT.TEST_DATA VALUES(2,'PK',3000,10);
INSERT INTO MSSINT.TEST_DATA VALUES(3,'CK',4000,10);
INSERT INTO MSSINT.TEST_DATA VALUES(4,'GK',2500,20);
INSERT INTO MSSINT.TEST_DATA VALUES(5,'WK',8000,20);
INSERT INTO MSSINT.TEST_DATA VALUES(6,'WK',8000,20);
-------------
select dbms_metadata.get_ddl('TABLE','DEPT','SCOTT') from dual;
 
select dbms_metadata.get_ddl('INDEX','DEPT_IDX','SCOTT') from dual;

DENSE_RANK - ANALYTICAL:

As an analytic function, DENSE_RANK computes the rank of each row returned from a query with respect to the other rows, based on the values of the value_exprs in the order_by_clause.

SELECT DEPT_ID,LAST_NAME,SALARY,DENSE_RANK() OVER (PARTITION BY DEPT_ID ORDER BY SALARY) RANK FROM MSSMIGR.G1
ORDER BY DEPT_ID,RANK,LAST_NAME;

DEPT_ID	LAST_NAME	SALARY RANK

10			A3		1500	1
10			A1		2500	2
10			A2		3000	3
20			B2		500		1
20			B3		3600	2
20			B1		5600	3

NOTE: IF BOTH SALARY IS SAME THEN RANK ALSO WILL BE SAME AND NEXT NEW RANK WILL GIVEN RANK VALUE OF IMMEDIATE NEXT RANK WITH RESPECT TO THE RANK GIVEN SO FAR.

DENSE_RANK - AGGREGATE:

As an aggregate function, DENSE_RANK calculates the dense rank of a hypothetical row identified by the arguments of the function with respect to a given sort specification. The arguments of the function must all evaluate to constant expressions within each aggregate group, because they identify a single row within each group. The constant argument expressions and the expressions in the
order_by_clause of the aggregate match by position. Therefore, the number of arguments must be the same and types must be compatible.

EID NAME    SALARY  COMM_PCT
100	Steven	24000	
101	Neena	17000	0.6
102	Lex		17000	0.8
145	John	14000	0.4

SELECT DENSE_RANK(17000,0.6) WITHIN GROUP (ORDER BY salary DESC,COMM_PCT DESC) "Dense Rank"
FROM OE.employees;

O/P:
Dense Rank
3

SELECT DENSE_RANK(17000) WITHIN GROUP (ORDER BY salary DESC) "Dense Rank"
FROM OE.employees;

O/P:
Dense Rank
2

NOTE: IF BOTH SALARY IS SAME THEN RANK ALSO WILL BE SAME.

Hierarchical Query Examples:


To find the children of a parent row, Oracle evaluates the PRIOR expression of the CONNECT BY condition for the parent row and the other expression for each row in the table. Rows for which the condition is true are the children of the parent. The CONNECT BY condition can contain other conditions to further filter the rows selected by the query.

If the CONNECT BY condition results in a loop in the hierarchy, then Oracle returns an error. A loop occurs if one row is both the parent (or grandparent or direct ancestor) and a child (or a grandchild or a direct descendent) of another row.


condition can be any condition as described in Chapter 6, "Conditions."
START WITH specifies the root row(s) of the hierarchy.
CONNECT BY specifies the relationship between parent rows and child rows of the hierarchy.

CONNECT BY Example The following hierarchical query uses the CONNECT BY clause to define the relationship between employees and managers:

--Find all parents
SELECT employee_id, last_name, manager_id
FROM oe.employees
START WITH employee_id = 101
CONNECT BY PRIOR manager_id = employee_id;-- parent = child

--Find all childs
SELECT employee_id, last_name, manager_id
FROM oe.employees
START WITH EMPLOYEE_ID = 103
CONNECT BY PRIOR employee_id = manager_id;--child = parent

LEVEL : The position in the hierarchy of the current row in relation to the root node.

SELECT employee_id, last, manager_id,LEVEL
FROM oe.employees
START WITH employee_id = 101
CONNECT BY PRIOR manager_id = employee_id;-- parent = child

SELECT employee_id, last_name, manager_id,LEVEL
FROM oe.employees
START WITH employee_id = 101
CONNECT BY PRIOR employee_id = manager_id;-- parent = child


--------SYS_CONNECT_BY_PATH
Returns the path of a column value from root to node, with column values separated by char for each row returned by CONNECT BY condition.

SELECT EMPLOYEE_ID,SYS_CONNECT_BY_PATH(last_name, '/') "Path"
FROM employees
START WITH EMPLOYEE_ID =101
CONNECT BY PRIOR employee_id = manager_id
ORDER by EMPLOYEE_ID;


--------CONNECT_BY_ISCYCLE:

The CONNECT_BY_ISCYCLE pseudocolumn returns 1 if the current row has a child which is also its ancestor. Otherwise it returns 0.
The NOCYCLE parameter instructs Oracle Database to return rows from a query even if a CONNECT BY loop exists in the data.
SYS_CONNECT_BY_PATH : Returns a delimited breadcrumb from root to the current row.

SELECT e.*,LEVEL FROM hr.employees e
start with e.employee_id = 100
connect by prior e.EMPLOYEE_ID = e.MANAGER_ID
ORDER BY LEVEL;---without loop in hierarchy

In the hr.employees table, the employee Steven King is the head of the company and has no manager. Among his employees is John Russell, who is the manager of department 80. If you update the employees table to set Russell as Kings manager, you

create a loop in the data:

UPDATE employees SET manager_id = 145
WHERE employee_id = 100;

SELECT e.LAST_NAME,LEVEL,CONNECT_BY_ISCYCLE CYCLE,SYS_CONNECT_BY_PATH(E.last_name, '/') FROM hr.employees e
start with e.employee_id = 100
connect by NOCYCLE prior e.EMPLOYEE_ID = e.MANAGER_ID
ORDER BY LEVEL;--with loop in hierarchy

--------CONNECT_BY_ROOT : Returns the root node(s) associated with the current row.

The following example returns the last name of each employee in department 110, each manager at the highest level above that
employee in the hierarchy, the number of levels between manager and employee, and the path between the two:

SELECT last_name "Employee", LAST_NAME Manager,
--CONNECT_BY_ROOT last_name "Manager",
LEVEL-1 "Pathlen", SYS_CONNECT_BY_PATH(last_name, '/') "Path"
FROM employees
WHERE EMPLOYEE_ID = 206
CONNECT BY PRIOR employee_id = manager_id
ORDER BY "Pathlen";

SELECT last_name "Employee", CONNECT_BY_ROOT last_name "Manager",
LEVEL-1 "Pathlen", SYS_CONNECT_BY_PATH(last_name, '/') "Path"
FROM employees
WHERE EMPLOYEE_ID = 206
CONNECT BY PRIOR employee_id = manager_id
ORDER BY "Employee", "Manager", "Pathlen", "Path";

--------CONNECT_BY_ISLEAF : Indicates if the current row is a leaf node.
ORDER SIBLINGS BY : Applies an order to siblings, without altering the basic hierarchical structure of the data returned by the query.

Flashing back
Faster PL/SQL
Oracle HTML DB
Oracle Automatic Storage Management (ASM)
DBMS_ADVANCED_REWRITE
SQL profiles
Easier online redefinitions
Case-insensitive searching
Fewer invalidations
Online segment shrinking
---------------
REGEXP:
. means "any character".
* means "any number of this".
.* therefore means an arbitrary string of arbitrary length.
^ indicates the beginning of the string.
$ indicates the end of the string.
/
select * from dba_tab_privs where table_name='V_CLEC_QUALIFIED_SUBS';
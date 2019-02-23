set serveroutput on;
declare

TYPE nested_type IS TABLE OF VARCHAR2(20);
TYPE varray_type IS VARRAY(5) OF INTEGER;
TYPE asso_array_num_type IS TABLE OF NUMBER INDEX BY PLS_INTEGER;
TYPE asso_array_str_type IS TABLE OF VARCHAR2(32) INDEX BY PLS_INTEGER;
TYPE asso_array_str_type2 IS TABLE OF VARCHAR2(32) INDEX BY VARCHAR2(64);

v1 nested_type;
v2 varray_type;
v3 asso_array_num_type;
v4 asso_array_str_type;
v5 asso_array_str_type2;

begin
v1 := nested_type('apple','orange','mango','banana'); --initialize the constructor using the colleciton type
v2 := varray_type(1,2,3,4,5); --upto 5 integer values --initialize the constructor using the colleciton type
v3(5) := 500;    --just start assigning values
v3(6) := 400;    --subscripts can be any integer values
v4(7) := 'arun'; --just start assigning values
v4(10):= 'bindhi'; --subscripts can be any integer values
v5('arjun') := 'arun'; --just start assigning values
v5('bindhu') := 'juniper'; --subscripts can be any integer values
--referencing nested table values
DBMS_OUTPUT.PUT_LINE('nested table values');
FOR REC IN v1.FIRST..v1.LAST LOOP
    DBMS_OUTPUT.PUT_LINE(v1(REC));
END LOOP;
--referencing varray table values
DBMS_OUTPUT.PUT_LINE('varray table values');
FOR REC IN v2.FIRST..v2.LAST LOOP
    DBMS_OUTPUT.PUT_LINE(v2(REC));
END LOOP;
--referencing asso array str type table values
DBMS_OUTPUT.PUT_LINE('asso array str type table values');
DBMS_OUTPUT.PUT_LINE(v4(7));
DBMS_OUTPUT.PUT_LINE(v4(10));
end;
/

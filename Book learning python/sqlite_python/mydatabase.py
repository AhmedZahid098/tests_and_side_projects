import sqlite3
from database import Employee

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""create table employees(
            first text,
            last text,
            pay integer
 )""")


def insert_emp(emp):
    with conn:
        c.execute("insert into employees values (:first, :last, :pay) ", {
            'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emp_by_name(lastname):
    c.execute("select * from employees where last=:last", {'last': lastname, })
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""update employees set pay=:pay where first=:first AND last=:last""", {
                  'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    c.execute("""delete from employees where first = :first and last = :last""", {
              'first': emp.first, 'last': emp.last})


emp_1 = Employee('ahmed', 'zahid', 500)
emp_2 = Employee('ali', 'zahid', 600)
insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emp_by_name('zahid')
print(emps)

payed = update_pay(emp_2, 100000)
print(payed)
emps = get_emp_by_name('zahid')
print(emps)
remove_emp(emp_2)

conn.close()

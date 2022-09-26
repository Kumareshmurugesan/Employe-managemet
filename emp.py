from tabulate import tabulate
import mysql.connector
con = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = 'task'
)

def insert_emp (ename,job,salary,branch_id):
    res = con.cursor()
    sql = "insert into emp (ename,job,salary,branch_id) values (%s,%s,%s,%s)"
    user = (ename,job,salary,branch_id)
    res.execute(sql,user)
    con.commit()
    print("Data insert Success")

def get_all_emp ():
    res = con.cursor()
    sql = "Select * from emp"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result,headers=["EMPLOYEE_ID","EMPLOYEE_Name","JOB","SALARY","BRANCH_ID"]))

def delete_emp(emp_id):
    res = con.cursor()
    sql = "delete from emp where emp_id=%s"
    user = (emp_id,)
    res.execute(sql,user)
    con.commit()
    print("data deleted successfully")


def get_emp_details(branch_id):
    res = con.cursor()
    #sql = "select * from order_details where order_id = %s"
    sql = "select emp.emp_id,emp.ename,emp.job,emp.salary,branch.br_name " \
          "from emp inner join branch on emp.branch_id=branch.branch_id where emp.branch_id=%s;"

    user = (branch_id,)
    res.execute(sql,user)
    result = res.fetchall()
    print(tabulate(result, headers=["emp_id", "emp_name", "salary","branch_name"]))
    print(result)
    #con.commit()





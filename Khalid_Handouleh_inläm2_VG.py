# 1-  This is how I connected mysql to pthon and a selec example
import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd

connection = mysql.connector.connect(
     user='root', 
      password='aloore@22',
      database= 'employees')

cursor = connection.cursor()

#select_stmt = "SELECT * FROM dept_manager "
#cursor.execute(select_stmt, {'emp_no':1})
#rows = cursor.fetchmany(5)
#print(rows)

# 2-  This is another example of selecting from database
#connection = mysql.connector.connect(
 #    user='root', 
  #    password='aloore@22',
   #   database= 'employees')

#cursor = connection.cursor()
#select_stmt = "SELECT * FROM dept_manager "
#cursor.execute(select_stmt, {'emp_no':1})
#rows = cursor.fetchmany(5)
#print(rows)

# 3- This is to select how many women employees with the same first_name. show first_name and how many women shares this name 

#select_stmt = "SELECT first_name, COUNT(first_name) AS female_with_samelast FROM employees WHERE gender = 'F' GROUP BY first_name "
#cursor.execute(select_stmt, {'last_name': 'Markovitch'})
#rows = cursor.fetchmany(6)
#print(rows)

# Here is different data frames and their plots. 
# 4 - Data frame of employees with the same salary  and it's plot
#df_emp_same_salary = pd.read_sql('SELECT salary, COUNT(emp_no) AS emps_with_same_salary FROM salaries  GROUP BY salary', con = connection)
#print(df_emp_same_salary)

# PLOT. show salary in X axis and employees with the same salary in Y axis
#df_emp_same_salary.plot(x = 'salary', y = 'emps_with_same_salary')
#plt.show()

# 5 - Data frame of the title and the number of this specific title in titles table. 
df_num_titles = pd.read_sql('SELECT title, COUNT(title) AS num_title FROM titles GROUP BY title', con = connection) 
print(df_num_titles)

# PLOT
df_num_titles.plot(kind = 'bar', x= 'title', y= 'num_title')
plt.show()

# 6 - DATAFRAME how many managers has each department.
#df_debt_managers_number = pd.read_sql('SELECT dept_no, COUNT(emp_no) AS number_of_managers FROM dept_manager GROUP BY dept_no', con = connection)
#print(df_debt_managers_number)

#PLOT
#df_debt_managers_number.plot(kind = 'bar', x ='dept_no', y = 'number_of_managers')
#plt.show()

# 7 -  Data frame of employees and how many departments he/she works
#df_num_departments = pd.read_sql('SELECT emp_no, COUNT(DISTINCT dept_no) AS number_of_departments FROM dept_emp GROUP BY emp_no   ', con = connection) 
#print(df_num_departments)

#df_num_departments.plot(kind = 'scatter', x = 'emp_no', y = 'number_of_departments')
#plt.show()

# 8 DATA FRAME show employee and his/her average salary where salary > 150000
#df_emp_avg_salary = pd.read_sql('SELECT emp_no, AVG(salary) AS avg_salary FROM salaries WHERE salary > 150000 GROUP BY emp_no', con = connection)
#print(df_emp_avg_salary)

# PLOT
#df_emp_avg_salary.plot(kind = 'scatter', x = 'emp_no', y = 'avg_salary')
#plt.show()

# 9 - DATA FRAME for employees with the same first_name where employee has number of same first name less than 200 employees
#df_employees_samefirst = pd.read_sql('SELECT DISTINCT(first_name) AS name, COUNT(first_name) AS employees_with_same_firstname FROM employees  GROUP BY first_name HAVING employees_with_same_firstname < 200', con = connection)
#print(df_employees_samefirst)

# PLOT
#df_employees_samefirst.plot(kind = 'bar', x = 'name', y = 'employees_with_same_firstname')
#plt.show()

# 10 DATAFRAME of EMPLOYEES WITH THE SAME TITLE. for example there are 24 employers who has the title Manager
#df_employees_same_title = pd.read_sql('SELECT title , COUNT(emp_no) AS num_employers FROM titles GROUP BY title', con = connection)
#print(df_employees_same_title)

#PLOT
#df_employees_same_title.plot(kind = 'bar', x = 'title', y = 'num_employers')
#plt.show()

# 11 - DATAFRAME  number of employers in a single department
#df_employees_in_department = pd.read_sql('SELECT dept_no, COUNT(emp_no) AS num_employers FROM dept_emp GROUP BY dept_no', con = connection)
#print(df_employees_in_department)

#PLOT
#df_employees_in_department.plot(kind = 'bar', x = 'dept_no', y = 'num_employers')
#plt.show()

# 12 - DATAFRAME OF  HIRE_DATE AND NUMBER OF EMPLOYEES HIRED IN THIS DATE  WHEN THIS NUMBER IS ABOVE 126 EMPLOYERS
#df_num_emp_hired = pd.read_sql('SELECT hire_date, COUNT(hire_date) AS num_emp_hired FROM employees   GROUP BY hire_date HAVING num_emp_hired > 126 ', con = connection)
#print(df_num_emp_hired)

#df_num_emp_hired.plot(kind = 'scatter', x = 'hire_date', y = 'num_emp_hired')
#plt.show()












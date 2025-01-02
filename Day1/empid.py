import pandas as pd


data = {
    'EMPLOYEE_ID': [102, 101, 101, 201, 114, 122, 200, 176, 176, 200],
    'START_DATE': ['2001-01-13', '1997-09-21', '2001-10-28', '2004-02-17', '2006-03-24', '2007-01-01', '1995-09-17', '2006-03-24', '2007-01-01', '2002-07-01'],
    'END_DATE': ['2006-07-24', '2001-10-27', '2005-03-15', '2007-12-19', '2007-12-31', '2007-12-31', '2001-06-17', '2006-12-31', '2007-12-31', '2006-12-31'],
    'JOB_ID': ['IT_PROG', 'AC_ACCOUNT', 'AC_MGR', 'MK_REP', 'ST_CLERK', 'ST_CLERK', 'AD_ASST', 'SA_REP', 'SA_MAN', 'AC_ACCOUNT'],
    'DEPARTMENT_ID': [60, 110, 110, 20, 50, 50, 90, 80, 80, 90]
}


department_names = {
    60: 'IT', 
    110: 'Accounting', 
    20: 'Marketing', 
    50: 'Shipping', 
    90: 'Administration', 
    80: 'Sales'
}


df = pd.DataFrame(data)

employee_job_counts = df.groupby('EMPLOYEE_ID').size()
employees_two_or_more_jobs = employee_job_counts[employee_job_counts >= 2].index


filtered_df = df[df['EMPLOYEE_ID'].isin(employees_two_or_more_jobs)]

distinct_departments = filtered_df[['EMPLOYEE_ID', 'DEPARTMENT_ID']].drop_duplicates()


distinct_departments['DEPARTMENT_NAME'] = distinct_departments['DEPARTMENT_ID'].map(department_names)

print("Departments for employees with two or more jobs:")
print(distinct_departments[['EMPLOYEE_ID', 'DEPARTMENT_NAME']])

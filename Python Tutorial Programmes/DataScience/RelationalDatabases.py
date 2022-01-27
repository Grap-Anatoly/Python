# We can connect to relational databases for analysing data using the pandas library as well as
# another additional library for implementing database connectivity.
# This package is named as sqlalchemy which provides full SQL language functionality to be used in python.

from sqlalchemy import create_engine
import pandas as pd

data = pd.read_csv('input.csv')

# Create the db engine
engine = create_engine('sqlite:///:memory:')

# Store the dataframe as a table
data.to_sql('data_table', engine)

# Query 1 on the relational table
res1 = pd.read_sql_query('SELECT * FROM data_table', engine)
print('Result 1')
print(res1)
print('')

# Query 2 on the relational table
res2 = pd.read_sql_query('SELECT dept,sum(salary) FROM data_table group by dept', engine)
print('Result 2')
print(res2)

# We can also insert data into relational tables using sql.execute function available in pandas.
# In the below code we previous csv file as input data set,
# store it in a relational table and then insert another record using sql.execute.

from pandas.io import sql

# Insert another row
sql.execute('INSERT INTO data_table VALUES(?,?,?,?,?,?)', engine, params=[('id',9,'Ruby',711.20,'2015-03-27','IT')])

# Read from the relational table
res = pd.read_sql_query('SELECT ID,Dept,Name,Salary,start_date FROM data_table', engine)
print(res)

# We can also delete data into relational tables using sql.execute function available in pandas.
# The below code deletes a row based on the input condition given.

sql.execute('Delete from data_table where name = (?) ', engine,  params=[('Gary')])

res = pd.read_sql_query('SELECT ID,Dept,Name,Salary,start_date FROM data_table', engine)
print(res)
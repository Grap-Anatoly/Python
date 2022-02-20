# The SQL Expression Language constructs its expressions against table columns.
# SQLAlchemy Column object represents a column in a database table which is in turn represented by a Tableobject.
# Metadata contains definitions of tables and associated objects such as index, view, triggers, etc.
#
# Hence an object of MetaData class from SQLAlchemy Metadata is a collection of
# Table objects and their associated schema constructs.
# It holds a collection of Table objects as well as an optional binding to an Engine or Connection.

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
)

# The create_all() function uses the engine object to create all the defined table objects
# and stores the information in metadata.

meta.create_all(engine)

# Expressions --------------------

ins = students.insert()

# The result of above method is an insert object that can be verified by using str() function.
# The below code inserts details like student id, name, lastname.

# 'INSERT INTO students (id, name, lastname) VALUES (:id, :name, :lastname)'

# It is possible to insert value in a specific field by values() method to insert object. The code for the same is given below −

ins = students.insert().values(name = 'Karan')
str(ins)

# 'INSERT INTO users (name) VALUES (:name)'
# The SQL echoed on Python console doesn’t show

# Executing exressions --------------------

# In order to execute the resulting SQL expressions, we have to obtain a connection object
# representing an actively checked out DBAPI connection resource and then
# feed the expression object as shown in the code below.

conn = engine.connect()

# The following insert() object can be used for execute() method −

ins = students.insert().values(name = 'Ravi', lastname = 'Kapoor')
result = conn.execute(ins)

# Selecting rows --------------------

s = students.select()

# The select object translates to SELECT query by str(s) function as shown below −

# 'SELECT students.id, students.name, students.lastname FROM students'
# We can use this select object as a parameter to execute() method of connection object as shown in the code below −

result = conn.execute(s)

# The resultant variable is an equivalent of cursor in DBAPI. We can now fetch records using fetchone() method.

row = result.fetchone()
# All selected rows in the table can be printed by a for loop as given below

for row in result:
   print (row)

# The WHERE clause of SELECT query can be applied by using Select.where().
# For example, if we want to display rows with id >2

s = students.select().where(students.c.id>2)

result = conn.execute(s)

for row in result:
   print (row)

# Textual -------------------------

# SQLAlchemy lets you just use strings, for those cases when the SQL is already known and there isn’t a strong need
# for the statement to support dynamic features.
# The text() construct is used to compose a textual statement that is passed to the database mostly unchanged.
#
# It constructs a new TextClause, representing a textual SQL string directly as shown in the below code −
#
from sqlalchemy import text

t = text("SELECT * FROM students")

result = conn.execute(t)

# Aliases ------------------------

# The alias in SQL corresponds to a “renamed” version of a table or SELECT statement,
# which occurs anytime you say “SELECT * FROM table1 AS a”.
# The AS creates a new name for the table. Aliases allow any table or subquery to be referenced by a unique name.

from sqlalchemy.sql import alias, select

st = students.alias("a")
s = select([st]).where(st.c.id > 2)

conn.execute(s).fetchall()

# Update ------------------------

# The update() method on target table object constructs equivalent UPDATE SQL expression.
# table.update().where(conditions).values(SET expressions)

stmt=students.update().where(students.c.lastname=='Khanna').values(lastname='Kapoor')

conn.execute(stmt)

# Delete ------------------------

# The delete operation can be achieved by running delete() method on target table object as given in the following statement −

# stmt = students.delete()
# In case of students table, the above line of code constructs a SQL expression as following −

# 'DELETE FROM students'

stmt = students.delete().where(students.c.lastname == 'Khanna')

conn.execute(stmt)

# Parameter updates ------------

# In some cases, the order of parameters rendered in the SET clause are significant. In MySQL, providing updates to column values is based on that of other column values.
#
# Following statement’s result −
#
# UPDATE table1 SET x = y + 10, y = 20
# will have a different result than −
#
# UPDATE table1 SET y = 20, x = y + 10
# SET clause in MySQL is evaluated on a per-value basis and not on per-row basis.
# For this purpose, the preserve_parameter_order is used.
# Python list of 2-tuples is given as argument to the Update.values() method −
#
# stmt = table1.update(preserve_parameter_order = True).\
#    values([(table1.c.y, 20), (table1.c.x, table1.c.y + 10)])

# AND -----------------------

from sqlalchemy import and_

print(
   and_(
      students.c.name == 'Ravi',
      students.c.id <3
   )
)

# Select

stmt = select([students]).where(and_(students.c.name == 'Ravi', students.c.id <3))
conn.execute(stmt)

# OR -----------------------

from sqlalchemy import or_

stmt = select([students]).where(or_(students.c.name == 'Ravi', students.c.id <3))
conn.execute(stmt)

# asc -----------------------

from sqlalchemy import asc

stmt = select([students]).order_by(asc(students.c.name))
conn.execute(stmt)

# between-------------------

from sqlalchemy import between

stmt = select([students]).where(between(students.c.id,2,4))
print (stmt)

# UNION-------------------

# from sqlalchemy import union
#
# u = union(addresses.select().where(addresses.c.email_add.like('%@gmail.com addresses.select().where(addresses.c.email_add.like('%@yahoo.com'))))
#
# result = conn.execute(u)
# result.fetchall()

# union_all()-------------------

# UNION ALL operation cannot remove the duplicates and cannot sort the data in the resultset.
# For example, in above query, UNION is replaced by UNION ALL to see the effect.
#
# u = union_all(addresses.select().where(addresses.c.email_add.like('%@gmail.com')), addresses.select().where(addresses.c.email_add.like('%@yahoo.com')))
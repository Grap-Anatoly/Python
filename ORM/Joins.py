# The join() method returns a join object from one table object to another.

# join(right, onclause = None, isouter = False, full = False)
# The functions of the parameters mentioned in the above code are as follows −

# right − the right side of the join; this is any Table object
# onclause − a SQL expression representing the ON clause of the join.
# If left at None, it attempts to join the two tables based on a foreign key relationship
# isouter − if True, renders a LEFT OUTER JOIN, instead of JOIN
# full − if True, renders a FULL OUTER JOIN, instead of LEFT OUTER JOIN

# For example, following use of join() method will automatically result in join based on the foreign key.
#
# print(students.join(addresses))
# This is equivalent to following SQL expression −

# students JOIN addresses ON students.id = addresses.st_id

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
engine = create_engine('sqlite:///college.db', echo = True)

meta = MetaData()
conn = engine.connect()
students = Table(
   'students', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
)

addresses = Table(
   'addresses', meta,
   Column('id', Integer, primary_key = True),
   Column('st_id', Integer,ForeignKey('students.id')),
   Column('postal_add', String),
   Column('email_add', String)
)

from sqlalchemy import join
from sqlalchemy.sql import select

j = students.join(addresses, students.c.id == addresses.c.st_id)
stmt = select([students]).select_from(j)

result = conn.execute(stmt)
result.fetchall()
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, select
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()
conn = engine.connect()

studentsNew = Table(
   'studentsNew', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
)

addresses = Table(
   'addresses', meta,
   Column('id', Integer, primary_key = True),
   Column('st_id', Integer, ForeignKey('studentsNew.id')),
   Column('postal_add', String),
   Column('email_add', String))

meta.create_all(engine)

conn.execute(studentsNew.insert(), [
   {'name':'Ravi', 'lastname':'Kapoor'},
   {'name':'Rajiv', 'lastname' : 'Khanna'},
   {'name':'Komal','lastname' : 'Bhandari'},
   {'name':'Abdul','lastname' : 'Sattar'},
   {'name':'Priya','lastname' : 'Rajhans'},
])

conn.execute(addresses.insert(), [
   {'st_id':1, 'postal_add':'Shivajinagar Pune', 'email_add':'ravi@gmail.com'},
   {'st_id':1, 'postal_add':'ChurchGate Mumbai', 'email_add':'kapoor@gmail.com'},
   {'st_id':3, 'postal_add':'Jubilee Hills Hyderabad', 'email_add':'komal@gmail.com'},
   {'st_id':5, 'postal_add':'MG Road Bangaluru', 'email_add':'as@yahoo.com'},
   {'st_id':2, 'postal_add':'Cannought Place new Delhi', 'email_add':'admin@khanna.com'},
])

s = select([studentsNew, addresses]).where(studentsNew.c.id == addresses.c.st_id)
result = conn.execute(s)

for row in result:
   print (row)

#  The following lines of codes explain the concept of multiple table updates clearly.

stmt = studentsNew.update().\
values({
   studentsNew.c.name:'xyz',
   addresses.c.email_add:'abc@xyz.com'
}).\
where(studentsNew.c.id == addresses.c.id)
# The update object is equivalent to the following UPDATE query −

# UPDATE students
# SET email_add = :addresses_email_add, name = :name
# FROM addresses
# WHERE students.id = addresses.id

# As far as MySQL dialect is concerned, multiple tables can be embedded into a single UPDATE statement separated by a comma as given below −

stmt = studentsNew.update().\
   values(name = 'xyz').\
   where(studentsNew.c.id == addresses.c.id)
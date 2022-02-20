from sqlalchemy import create_engine

engine = create_engine('sqlite:///college.db', echo = True)

# MySql

engineSql = create_engine("mysql://user:pwd@localhost/college",echo = True)




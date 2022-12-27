0x0F. Python - Object-relational mapping
Python
OOP
SQL
MySQL
ORM
SQLAlchemy
 By: Guillaume

Before you start…
Please make sure your MySQL server is in 8.0 -> How to install MySQL 8.0 in Ubuntu 20.04

Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
With an ORM:

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

Resources
Read or watch:

Object-relational mappers
mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)
MySQLdb tutorial
SQLAlchemy tutorial
SQLAlchemy
mysqlclient/MySQLdb
Introduction to SQLAlchemy
Flask SQLAlchemy
10 common stumbling blocks for SQLAlchemy newbies
Python SQLAlchemy Cheatsheet
SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)
SQLAlchemy Tutorial
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
How to connect to a MySQL database from a Python script
How to SELECT rows in a MySQL table from a Python script
How to INSERT rows in a MySQL table from a Python script
What ORM means
How to map a Python Class to a MySQL table

More Info
Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04

$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
Install SQLAlchemy module version 1.4.x
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
Also, you can have this warning message:

/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
You can ignore it.

TASKS:

0. Get all states .
 Write a script that lists all states from the database hbtn_0e_0_usa

1. Filter states
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

    
2. Filter states by user input
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

    
3. SQL Injection...
Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?

Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

    
4. Cities by states
Write a script that lists all cities from the database hbtn_0e_4_usa

    
5. All cities by state
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

    
6. First state model
Write a python file that contains the class definition of a State and an instance Base = declarative_base():

    
7. All states via SQLAlchemy
Write a script that lists all State objects from the database hbtn_0e_6_usa

    
8. First state
Write a script that prints the first State object from the database hbtn_0e_6_usa

    
9. Contains `a`
Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa

    
10. Get a state
Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa

    
11. Add a new state
Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa

    
12. Update a state
Write a script that changes the name of a State object from the database hbtn_0e_6_usa

    
13. Delete states
Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa

    
14. Cities in state
Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.

City class:
inherits from Base (imported from model_state)
links to the MySQL table cities
class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key


    
15. City relationship
Improve the files model_city.py and model_state.py, and save them as relationship_city.py and relationship_state.py:

Write a script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)

    
16. List relationship
Write a script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa



    
17. From city
Write a script that lists all City objects from the database hbtn_0e_101_usa

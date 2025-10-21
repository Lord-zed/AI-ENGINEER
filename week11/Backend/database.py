# from sqlalchemy import create_engine,text
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv
# import os

# # dbhost = localhost
# # dbpassword

# # dbuser=root
# # dbname=backend_db


# load_dotenv()

# #db_url =dialect+driver://dbuser;dbpassword;dbhost;dbpart;dbname

# #db_url=f'mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}:{os.getenv("dbhost")}:{os.getenv("dbport")}:{os.getenv("dbname")}'
# db_url = f'mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}'

# engine=create_engine(db_url)

# session=sessionmaker(bind=engine)
# db=session()

# # writting sql queries 
# query = text('select * from user')
# users = db.execute(query).fetchall()
# print(users)

from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pymysql.constants import CLIENT
import os

load_dotenv()
#db_url =dialect+driver://dbuser;dbpassword;dbhost;dbport;dbname
# proper url:
# db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


db_url = f'mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}'
engine = create_engine(db_url)
session =sessionmaker(bind=engine)
db = session()
# Writing sql queries
# query =  text("select * from user")
# users = db.execute(query).fetchall()
# print(users)




# create_users_table = text("""
# CREATE TABLE IF NOT EXISTS users (
#     id  INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     email VARCHAR(100) NOT NULL
# );
# """)
# create_courses_table = text("""
# CREATE TABLE IF NOT EXISTS courses (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     title VARCHAR(100) NOT NULL,
#     level VARCHAR(100) NOT NULL
# );
# """)
# create_enrollment_table = text("""
# CREATE TABLE IF NOT EXISTS enrollment (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     userId INT,
#     courseId INT,
#     FOREIGN KEY (userId) REFERENCES users(id),
#     FOREIGN KEY (courseId) REFERENCES courses(id)
# );
# """)
# # Execute each one
# db.execute(create_users_table)
# db.execute(create_courses_table)
# db.execute(create_enrollment_table)
# print('Tables has been created successfully')


# using a different method
engine = create_engine(
    db_url,
    connect_args={"client_flag": CLIENT.MULTI_STATEMENTS}
)

create_tables_query = text("""
CREATE TABLE IF NOT EXISTS users (
    id  INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
                           );
CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    level VARCHAR(100) NOT NULL
     );
CREATE TABLE IF NOT EXISTS enrollment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT,
    courseId INT,
    FOREIGN KEY (userId) REFERENCES users(id),
    FOREIGN KEY (courseId) REFERENCES courses(id)
          );
# """)

print("Tables have been created successfully.")
db.execute(create_tables_query)

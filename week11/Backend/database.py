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
import os
load_dotenv()
# db_url = dialect+driver://dbuser;dbpassword;dbhost;dbport;dbname
# proper url:
# db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}
db_url = f'mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}'
engine = create_engine(db_url)
session =sessionmaker(bind=engine)
db = session()
# Writing sql queries
query =  text("select * from user")
users = db.execute(query).fetchall()
print(users)
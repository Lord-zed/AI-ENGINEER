from database import db
from fastapi import FastAPI, HTTPExeption
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
import bcrypt
from dotenv import load_dotenv
import uvicorn

# load_dotenv()
# app=FastAPI(title='Simple APP', version='1.0.0')

# class simple(BaseModel):
#        name: str = Field(..., example = "Sam Larry")
#        email: str = Field(..., example = "sam@gmail.com")
#        password: str = Field(..., example = "sam123")
    
# @app.post("/signup")
# def signup(input:simple):
#     try:

#         duplicate_query=text("""SELECT * FROM users 
#                               WHERE email =:email  """)
        

#         existing =db.execute(duplicate_query,{"email":input.email})
#         if existing:
#              raise HTTPExeption(status_code=400, detail= 'Email already exist')
        

#         query= text(""" INSERT INTO users (name,email,password)
#                            VALUES (:name,:email, :password)
#         """)
#         salt=bcrypt.gensalt()
#         hashedpassword =bcrypt.hashpw(input.password.encode('utf-8'), salt)
#         print(hashedpassword)

#         db.execute(query, {'name':input.name, 'email': input.email, 'pasword': hashedpassword})
#         db.commit()

#         return {'message': "user created successfully",
#                 "data":{'name':input.name, "email":input.email}}
    
#     except Exception as e:
#          raise HTTPExeption(status_code=500, detail=e)
    

# if __name__=="__main__":
#      uvicorn.run(app,host=os.getenv("host"), port=int(os.getenv("port")))
    

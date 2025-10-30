from databasen import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
import bcrypt
from dotenv import load_dotenv
import uvicorn
import jwt
from middleware import create_token

load_dotenv()
app=FastAPI(title='Simple APP', version='1.0.0')

token_time = int(os.getenv('token_time'))

class simple(BaseModel):
       name: str = Field(..., example = "Sam Larry")
       email: str = Field(..., example = "sam@gmail.com")
       password: str = Field(..., example = "sam123")
       userType: str = Field(...,example= 'student')
    
@app.post("/signup")
def signup(input:simple):
    try:

        duplicate_query=text("""SELECT * FROM users 
                              WHERE email =:email  """)
        

        existing =db.execute(duplicate_query,{"email":input.email})
        if existing:
               #raise HTTPExeption(status_code=400, detail= 'Email already exist')
        

         query= text(""" INSERT INTO users (name,email,password)
                           VALUES (:name,:email, :password, :userType)
        """)
        salt=bcrypt.gensalt()
        hashedpassword =bcrypt.hashpw(input.password.encode('utf-8'), salt)
        print(hashedpassword)

        db.execute(query, {'name':input.name, 'email': input.email, 'pasword': hashedpassword})
        db.commit()

        return {'message': "user created successfully",
                "data":{'name':input.name, "email":input.email}}
    
    except Exception as e:
         raise HTTPException(status_code=500, detail=e)
    

# Building a login endpoint
class LoginRequest(BaseModel):
    email: str = Field(..., example="jdoe@gmail.com")
    password: str = Field(..., example="sam11")
@app.post("/login")
def login(input: LoginRequest):
    try:
        
        query = text("""    SELECT * FROM users WHERE email = :email      """)
        result = db.execute(query, {"email": input.email}).fetchone()
        if not result:
            raise HTTPException(status_code=400, detail = "invalid email or password")
        
        verified_password = bcrypt.checkpw(input.password.encode('utf-8'),result.password.encode('utf-8'))
        if not verified_password:
            raise HTTPException(status_code=404, detail= 'Invalid email or password')
        
        encoded_token = create_token(details={
            'email':result.email,
            'userType':result.userType

        }, expiry=token_time)

        return {
            'message':'Login successful'
        }
    


    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    




    
if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))

    

# if __name__=="__main__":
#      uvicorn.run(app,host=os.getenv("host"), port=int(os.getenv("port")))
    

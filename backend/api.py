from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel
from typing import Optional
from fastapi import Form, Depends
from checkImage import CascadeClassifier

app=FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins='*'

)

@app.get('/')
def home():
    return json.dumps({"type":"identification"})

@app.get('/home')
def some():

    return "Type is passport"


@app.post('/images/something')
def process(image):
    c=CascadeClassifier(image)
    output=c.process()
    return output 







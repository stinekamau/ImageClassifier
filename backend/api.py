from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

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
    return json.dumps({'type':'passport'})


@app.get('/images/something')
def process(image):
    return {'type':'hello'}



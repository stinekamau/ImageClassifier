from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app=FastAPI()

origins=['http://localhost','http://localhost:8080','http://localhost:*','http.localhost:2715']

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex='http://.*'

)

@app.get('/')
def home():
    return json.dumps({'type':'identification'})

@app.get('/home')
def some():
    return json.dumps({'type':'passport'})


@app.get('/images/something')
def process(image):
    return {'type':'hello'}



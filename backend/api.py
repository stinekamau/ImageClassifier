from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def home():
    print('Hello')
    return {'type':None}

@app.get('/something')
def some():
    return {'detail':'Niice'}

@app.get('/images/classifier/{image}')
def process(image):
    return {'type':'hello'}



from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def home():
    print('Hello')
    return 'identification'

@app.get('/home')
def some():
    return {'detail':'Niice'}

@app.get('/images/something')
def process(image):
    return {'type':'hello'}



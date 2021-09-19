from fastapi import FastAPI

app=FastAPI()

@app.route('/')
async def home():
    return {'type':None}

@app.route('/images/classifier/{image}')
async def process(image):
    return {'type':'hello'}



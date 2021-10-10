from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from fastapi import Form, Depends
from checkImage import CascadeClassifier
from fastapi import UploadFile,File
from uvicorn import run
from pathlib import Path,PureWindowsPath

app=FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins='*'

)

@app.get('/')
def home():
    return json.dumps({"type":"identification"})

@app.post('/home/process')
async def image_type(file:UploadFile=File(...)):
    
    pt_name=Path.cwd() / 'resources' / file.filename
    with open(pt_name,'wb+') as f:
        f.write(file.file.read())
        f.close()
    c=CascadeClassifier(str(pt_name))
    output=c.process()
    print(f'Output is {output} ')
    return output['type_']
   

run(app)







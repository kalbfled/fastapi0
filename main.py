from fastapi import FastAPI
from typing import Union


app = FastAPI()


@app.get('/status')
def get_status():
    return {'message': 'System is healthy'}

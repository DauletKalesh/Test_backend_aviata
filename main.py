from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import ORJSONResponse

import time
import json
app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


with open('response_a.json') as a:
    data_a = json.loads(a.read())
with open('response_b.json') as b:
    data_b = json.loads(b.read())
# provider-a
@app.post('/search/', response_class=ORJSONResponse)
async def provider_a():
    time.sleep(30)
    return data_a

# provider-a
@app.post('/search/', response_class=ORJSONResponse)
async def provider_b():
    time.sleep(60)
    return data_b

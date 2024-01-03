from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel
import json
from typing import Any
from typing import Union
from typing import Dict
from typing import List
from typing import Optional
import os
import asyncio

app = FastAPI()

class RequestData(BaseModel):
    inputs: Union[Any, Dict]
    parameters: Optional[Dict]
            
async def get(inputs):
    print(inputs)
    prediction = [{'label': 'pos', 'score': 0.8038843274116516}]
    return prediction

async def post(request_data: RequestData):
    inputs = request_data.json()
    inputs = json.loads(inputs)
    prediction = [{'label': 'pos', 'score': 0.8038843274116516}]
    return prediction

app.add_api_route(path="/fastapi/api", endpoint=get, methods=["GET"])
app.add_api_route(path="/fastapi/api", endpoint=post, methods=["POST"])
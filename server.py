from typing import Union
from password_evaluation import evaluate
from fastapi import FastAPI

app = FastAPI()


@app.get("/")   
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get('/password/{upass}')
def res_pass(upass:str):
    res_msg = evaluate(upass)
    return {'msg':res_msg}

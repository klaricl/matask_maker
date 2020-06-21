from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

templates = Jinja2Templates(directory="templates")

@app.get("/templates")
def webpage():
    return templates.TemplateResponse("main.html")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
    

@app.get("/add/{a}/{b}")
def adding_numbers(a: int, b: int):
    return {"a": a, "b": b, "a + b": a + b}
    
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "price": item.price}
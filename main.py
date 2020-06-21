from fastapi import FastAPI, Request, Depends

from fastapi.templating import Jinja2Templates

import models
from models import Item
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")
app = FastAPI()

class ItemRequest(BaseModel):
    name: str
    price: float
    is_offer: bool = None

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/home")
def home(request: Request, db: Session = Depends(get_db)):
    items = db.query(Item).all()
    
    
    
    return templates.TemplateResponse("main.html", {
        "request": request,
        "items": items
    })

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
def update_item(item_id: int, item_request: ItemRequest, db: Session = Depends(get_db)):
    item = Item()
    item.name = item_request.name
    
    db.add(item)
    db.commit()
    
    return {"item_name": item_request.name, "item_id": item_request, "price": item_request.price}
    
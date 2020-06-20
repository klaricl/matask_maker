from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
    

@app.get("/add/{a}/{b}")
def adding_numbers(a: int, b: int):
    return {"a": a, "b": b, "a + b": a + b}
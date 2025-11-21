from fastapi import FastAPI

app = FastAPI()

# In-memory database
items = {}

@app.get("/items")
def read_items():
    return items

@app.post("/items")
def create_item(item_id: int, name: str):
    items[item_id] = {"name": name}
    return {"message": "Item created successfully."}

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):
    if item_id in items:
        items[item_id]["name"] = name
        return {"message": "Item updated successfully."}
    return {"error": "Item not found."}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted successfully."}
    return {"error": "Item not found."}
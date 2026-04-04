from fastapi import FastAPI

app = FastAPI()

# Query Parameters
# /users?name=mohit
# /products?price=100
# Searching on Instagram of particular person

@app.get("/users")
def get_users(name: str = None):
    return {"Name":name}


# For default params
@app.get("/products")
def get_users(limit: int = 10):
    return {"limit":limit}


# Multiple Query Params
@app.get("/items")
def get_users(name: str = None, price: int=0):
    return {
        "name": name,
        "price": price
    }

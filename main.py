from fastapi import FastAPI
# Fast API Backend Python Framework
app = FastAPI()

# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to FastApi"}

#About Route
@app.get("/about")
def about():
    return {"message": "This is About Page"}

#Users Route
@app.get("/users")
def users():
    return {
        "users": ["Alex", "Tovino", "Basil"]
    }

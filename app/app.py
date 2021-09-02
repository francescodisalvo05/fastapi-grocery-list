from fastapi import FastAPI, HTTPException

app = FastAPI()

# tags is the category
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"Ping" : "Pong"}

# get --> read
@app.get('/todo', tags=['TODOS'])
async def get_todo() -> dict:
    return ({"data":todos})

# post --> create
@app.post('/create', tags=['TODOS'])
async def add_todo(todo : dict) -> dict:
    todos.append(todo)
    return {"data" : "Added correctly!"}

# put --> update
@app.put('/update', tags=['TODOS'])
async def update_todo(id:int, body:dict) -> dict:

    for todo in todos:
        if int(todo['id']) == id:
            todo['activity'] = body['activity']
            return {"data" : f"{id} has been updated correctly!"}

    return {"data" : "Not found!"}

@app.delete('/delete/{id}', tags=['TODOS'])
async def delete_todo(id:int) -> dict:

    for todo in todos:
        if int(todo['id']) == id:
            todos.remove(todo)
            return {'data' : "Deleted!"}

    return {'data':"Not found!"}


todos = [
    {"id" : 1, "activity" : "read"},
    {"id" : 2, "activity" : "eat"}
]
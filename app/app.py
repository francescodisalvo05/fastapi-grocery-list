from fastapi import FastAPI, HTTPException

app = FastAPI()

# get --> read
@app.get('/todo', tags=['TODOS'], status_code=200)
async def get_todo() -> dict:
    return ({"data":todos})

# post --> create
@app.post('/create', tags=['TODOS'], status_code=201)
async def add_todo(todo : dict) -> dict:

    for temp_todo in todos:
        if temp_todo['id'] == todo['id']:
            raise HTTPException(status_code=400, detail="Item already present!")

    todos.append(todo)
    return {"data" : "Added correctly!"}

# put --> update
@app.put('/update', tags=['TODOS'], status_code=200)
async def update_todo(id:int, body:dict) -> dict:

    for todo in todos:
        if int(todo['id']) == id:
            todo['activity'] = body['activity']
            return {"data" : "Updated correctly!"}

    raise HTTPException(status_code=404, detail="Item not found!")

# delete 
@app.delete('/delete/{id}', tags=['TODOS'], status_code=200)
async def delete_todo(id:int) -> dict:

    for todo in todos:
        if int(todo['id']) == id:
            todos.remove(todo)
            return {'data' : "Deleted!"}

    raise HTTPException(status_code=404, detail="Item not found!")


todos = [
    {"id" : 1, "activity" : "read"},
    {"id" : 2, "activity" : "eat"}
]
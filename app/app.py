from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get('/', status_code=200)
async def greetings() -> dict:
    """Greetings"""
    return {"Welcome":"Thank you for using our service!"}



@app.get('/list', status_code=200)
async def get_list() -> dict:
    """Gets the whole grocery list
    
    Returns:
        Dictionary containing the list of items under the key "data"
    """
    return {"data":grocery_list}


@app.post('/create', status_code=201)
async def add_item(item : dict) -> dict:
    """Creates a new item to buy

    Args:
        item (dict): {"item" : str, "qty" : int}
    
    Returns:
        notification, code 201

    Raises:
        HTTPException 400, if the element is already present on the list
    """

    for temp_item in grocery_list:
        if temp_item['item'] == item['item']:
            raise HTTPException(status_code=400, detail= f"{item['item']} already present!")

    grocery_list.append(item)
    return {"data" : f"{item['item']} added correctly!"}



@app.put('/update', status_code=200)
async def update_item(item_name:str, item_quantity:int) -> dict:
    """Updates the quantity to buy for a given item

    Args:
        item_name (str) : name of the item to update
        item_quantity (int) : quantity to update

    Returns:
        notification, code 200

    Raises:
         HTTPException 404, if the item is not present on the list
    """

    for temp_item in grocery_list:
        if temp_item['item'] == item_name:
            temp_item['qty'] = item_quantity
            return {"data" : f"{item_name} correctly updated!"}

    raise HTTPException(status_code=404, detail=f"{item_name} not found!")

# delete 
@app.delete('/delete/{item_name}',status_code=200)
async def delete_item(item_name:str) -> dict:
    """Deletes item with a given iten_name

    Args:
        item_name (str) : name of the item that must be removed
    
    Returns:
        notification, code 200

    Raises:
        HTTPException 404, if the item is not present on the list
    """
    for temp_item in grocery_list:
        if temp_item['item'] == item_name:
            grocery_list.remove(temp_item)
            return {"data" : f"{item_name} correctly deleted!"}

    raise HTTPException(status_code=404, detail=f"{item_name} not found!")

grocery_list = [
    {"item" : "bread", "qty" : 1},
    {"item" : "milk", "qty" : 2}
]
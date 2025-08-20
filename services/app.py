from fastapi import FastAPI, Body
from controller import Controller

app = FastAPI()

@app.get('/all-soldiers')
async def get_all_soldiers():
    return Controller.get_soldiers()

@app.post('/add-soldier')
async def add_soldier(soldier: dict = Body(...)):
    return Controller.add_soldier(soldier)

@app.put('/update-soldier/{id}')
async def update_soldier(id: int, data: dict = Body(...)):
    return Controller.update_soldier(id, data)

@app.delete('/delete-soldier/{id}')
async def delete_soldier(id: int):
    return Controller.delete_soldier(id)



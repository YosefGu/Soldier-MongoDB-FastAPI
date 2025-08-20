from fastapi import FastAPI, Body
import uvicorn
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


if __name__ == "__main__":
    try:
        uvicorn.run(app, port=8000)
    except Exception as e:
        print("Error running server")
        print(e)
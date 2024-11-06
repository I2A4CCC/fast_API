from typing import Union
from fastapi import FastAPI
from modules import TODO

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

todos = []
# get all todos
@app.get("/todos")
def get_todos():
    return {"todos": todos}

# get  single todo
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": 'No todos found'}
# create a todo
@app.post("/todos")
def creat_todos(todo: TODO):
    todos.append(todo)
    return {"message": 'todo has been added'}
# update todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo_obj: TODO):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"message": 'No todos found to update'}

# delete todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo has been DELETED"}
    return {"message": 'No todos found'}
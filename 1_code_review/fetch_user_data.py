import httpx
from pydantic import BaseModel


class Todo(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool

async def fetch_todo(todo_id):
    response = httpx.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")
    todo_data = response.json()
    return Todo(**todo_data)

async def fetch_multiple_todos(todo_ids):
    todo_list = []
    for todo_id in todo_ids:
        todo = await fetch_todo(todo_id)
        todo_list.append(todo)
    return todo_list

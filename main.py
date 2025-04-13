from typing import List, Optional

from fastapi import FastAPI, HTTPException, status, Query, Path
from fastapi.responses import JSONResponse
import uvicorn

from data_actions import get_db, save_db, get_db_users, save_db_users
from models import BookModel, BookModelResponse, UserModel, UserModelResponse


app = FastAPI()


@app.get("/books", response_model=List[BookModelResponse], status_code=status.HTTP_202_ACCEPTED)
async def get_books():
    return get_db()


@app.get("/books/{id}", response_model=BookModelResponse, status_code=status.HTTP_202_ACCEPTED)
async def get_book(id: int):
    book = next((book for book in get_db() if book.get("id") == id), None)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Книга з id {id} не знайдена. ☹️")
    return book


@app.post("/books/", status_code=status.HTTP_201_CREATED)
async def add_book(book_model: BookModel):
    db = get_db()
    db.append(book_model.model_dump())
    save_db(db)
    return JSONResponse("Нова книга успішно додана! 😎")


@app.delete("/books/{id}", status_code=status.HTTP_200_OK)
async def delete_book(id: int):
    db = get_db()
    book = next((book for book in db if book.get("id") == id), None)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Книга з id {id} не знайдена. ☹️")
    db.remove(book)
    save_db(db)
    return JSONResponse("Книга успішно видалена! 😎")


@app.post("/users/", status_code=status.HTTP_201_CREATED)
def add_user(user_model: UserModel):
    db = get_db_users()
    db.append(user_model.model_dump())
    save_db_users(db)
    return JSONResponse("Новий користувач успішно доданий! 😎")


@app.get("/users", response_model=List[UserModelResponse], status_code=status.HTTP_202_ACCEPTED)
async def get_users():
    return get_db_users()


@app.get("/users/{user_id}", response_model=UserModelResponse, status_code=status.HTTP_202_ACCEPTED)
async def get_user(user_id: int):
    user = next((user for user in get_db_users() if user.get("user_id") == user_id), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Користувач з id {user_id} не знайдений. ☹️")
    return user


@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int):
    db = get_db_users()
    user = next((user for user in db if user.get("user_id") == user_id), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Користувач з id {user_id} не знайдений. ☹️")
    db.remove(user)
    save_db_users(db)
    return JSONResponse("Користувач успішно видалений! 😎")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)
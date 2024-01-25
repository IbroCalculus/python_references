from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

inventory = {
    1: {
        "name": "Milk",
        "price": "3.99",
        "brand": "regular",
    },
    2: {
        "name": "Sugar",
        "price": "4.23",
        "brand": "condensed",
    }
}

BOOKS = {
    'book_1': {'title': 'Title one', 'author': 'Author one'},
    'book_2': {'title': 'Title two', 'author': 'Author two'},
    'book_3': {'title': 'Title three', 'author': 'Author three'},
    'book_4': {'title': 'Title four', 'author': 'Author four'},
    'book_5': {'title': 'Title five', 'author': 'Author fivee'}
}


# http://127.0.0.1:8000/        ============== GET ====================
@app.get('/')
async def read_all_books():
    return BOOKS


# http://127.0.0.1:8000/book_3      ================== GET (Path parameter) =====================
@app.get('/{book_name}')
async def read_book(book_name: str):
    return BOOKS.get(book_name)


# http://127.0.0.1:8000/get-with-query/?skip_book=book_2      ================== GET (Query parameter) =====================
@app.get('/get-with-query/')
async def read_some_books(skip_book: str = "book_4"):  # book_4 is default value and skip_book is required
    new_books = BOOKS.copy()
    del new_books[skip_book]
    return new_books


# http://127.0.0.1:8000/get-with-query2/ OR http://127.0.0.1:8000/get-with-query2/?skip_book=book_1     ===== GET (Query parameter) =======
@app.get('/get-with-query2/')
async def read_some_books(skip_book: Optional[str] = None):  # The value of skip_book is optional
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


# ==================== POST ================================
# This can be done in 2 ways, either using request body, or by using parameters (path or query)

# 1. -------------------------- Using path parameter -------------------
# http://127.0.0.1:8000/create-new-book/BookOfTech/IbrahimCalculus
@app.post('/create-new-book/{book_title}/{book_author}')
async def create_new_book(book_title, book_author):
    new_book_title = f"book_{len(BOOKS) + 1}"
    BOOKS[new_book_title] = {'title': book_title, 'author': book_author}
    return BOOKS


# 2. ---- Using query parameter -------
# http://127.0.0.1:8000/create-new-book2/?book_title=Legend&book_author=MKasim
@app.post('/create-new-book2/')
async def create_new_books2(book_title, book_author: Optional[str] = "JohnDoe"):
    new_book_title = f"book_{len(BOOKS) + 1}"
    BOOKS[new_book_title] = {'title': book_title, 'author': book_author}
    return BOOKS


# 3. ---- Using request body -------
class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    inventory[item_id] = {"name": item.name, "price": item.price, "brand": item.brand}
    # inventory[item_id] = item
    return inventory[item_id]


# ========================================= UPDATE ==================================

# 1. ---------------------- UPDATE (Path parameter) ----------------------
# http://127.0.0.1:8000/update-book/book_2/TheFrail/CalculusMBS
@app.put('/update-book/{book_id}/{book_title}/{book_author}')
async def update_book(book_id: str, book_title: str, book_author: str):
    BOOKS[book_id] = {'title': book_title, 'author': book_author}
    return BOOKS


# 2. ---------------------- UPDATE (Path & Query parameter) ----------------------
# http://127.0.0.1:8000/update-book2/book_1?book_title=bookTitleOne&book_author=authorOne
@app.put('/update-book2/{book_id}')
async def update_book2(book_id: str, book_title: str, book_author: str):
    BOOKS[book_id] = {'title': book_title, 'author': book_author}
    return BOOKS


# ========================================= DELETE ==================================
# http://127.0.0.1:8000/delete_book/book_3     (Path parameter)
@app.delete('/delete_book/{book_id}')
async def delete_book(book_id):
    del BOOKS[book_id]
    return BOOKS


# http://127.0.0.1:8000/delete_book2?book_id=book_3     (Query parameter)
@app.delete('/delete_book2')
async def delete_book(book_id):
    del BOOKS[book_id]
    return BOOKS

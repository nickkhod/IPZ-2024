from fastapi import FastAPI, Query
from typing import List
from menu_data import menu  # Імпортуємо наше меню

app = FastAPI()

# Отримання всього меню
@app.get("/menu")
def get_menu():
    return menu

# Фільтрація меню по категорії та максимальній ціні
@app.get("/filter")
def filter_menu(
    category: str = Query(None, alias="category"),  # Фільтр по категорії
    max_price: int = Query(None, alias="max_price")  # Фільтр по максимальній ціні
):
    filtered_menu = menu

    # Фільтрація по категорії, якщо вона задана
    if category:
        filtered_menu = [item for item in filtered_menu if item["category"].lower() == category.lower()]

    # Фільтрація по максимальній ціні, якщо вона задана
    if max_price:
        filtered_menu = [item for item in filtered_menu if item["price"] <= max_price]

    return filtered_menu
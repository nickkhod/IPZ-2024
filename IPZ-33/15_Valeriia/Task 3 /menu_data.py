import json

# Шлях до файлу з меню
MENU_FILE = "menu.json"

def load_menu():
    try:
        with open(MENU_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

menu = load_menu()

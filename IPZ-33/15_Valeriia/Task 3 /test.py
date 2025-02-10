import requests

# Основний URL API
BASE_URL = "http://127.0.0.1:8000"

def get_menu():
    url = f"{BASE_URL}/menu"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Помилка: {response.status_code}"

def get_by_category(category):
    url = f"{BASE_URL}/filter"
    params = {"category": category}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Помилка: {response.status_code}"

def get_by_price(max_price):
    url = f"{BASE_URL}/filter"
    params = {"max_price": max_price}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Помилка: {response.status_code}"

def get_item_by_id(item_id):
    url = f"{BASE_URL}/menu/{item_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Помилка: {response.status_code}"

def main():
    while True:
        print("\n--- Меню ---")
        print("1. Отримати все меню")
        print("2. Отримати страви за категорією")
        print("3. Фільтрувати страви за ціною")
        print("4. Вихід")
        
        choice = input("Виберіть опцію (1-4): ")

        if choice == "1":
            menu = get_menu()
            print("Меню:")
            print(menu)
        elif choice == "2":
            category = input("Введіть категорію: ")
            menu_by_category = get_by_category(category)
            print(f"Меню для категорії '{category}':")
            print(menu_by_category)
        elif choice == "3":
            max_price = input("Введіть максимальну ціну: ")
            menu_by_price = get_by_price(max_price)
            print(f"Меню з ціною до {max_price}:")
            print(menu_by_price)
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Невірний вибір! Спробуйте ще раз.")

if __name__ == "__main__":
    main()

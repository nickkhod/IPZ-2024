services = []

def add_service():
    name = input("Введіть назву послуги: ")
    description = input("Введіть опис послуги: ")
    price = float(input("Введіть вартість послуги: "))
    service = {
        "name": name,
        "description": description,
        "price": price
    }
    services.append(service)
    print("Послугу додано!\n")

def show_services():
    if not services:
        print("Послуги не додано.\n")
        return
    print("Список послуг:")
    for index, service in enumerate(services, 1):
        print(f"{index}. Назва: {service['name']}, Опис: {service['description']}, Вартість: {service['price']} грн")
    print()

def update_service():
    show_services()
    if not services:
        return
    service_index = int(input("Введіть номер послуги для оновлення: ")) - 1
    if 0 <= service_index < len(services):
        print("Оновлюємо послугу:")
        name = input("Введіть нову назву послуги: ")
        description = input("Введіть новий опис послуги: ")
        price = float(input("Введіть нову вартість послуги: "))
        services[service_index] = {
            "name": name,
            "description": description,
            "price": price
        }
        print("Послугу оновлено!\n")
    else:
        print("Невірний номер послуги.\n")

def delete_service():
    show_services()
    if not services:
        return
    service_index = int(input("Введіть номер послуги для видалення: ")) - 1
    if 0 <= service_index < len(services):
        removed_service = services.pop(service_index)
        print(f"Послугу '{removed_service['name']}' видалено!\n")
    else:
        print("Невірний номер послуги.\n")


def main():
    while True:
        print("Меню:")
        print("1. Додати послугу")
        print("2. Показати послуги")
        print("3. Оновити послугу")
        print("4. Видалити послугу")
        print("5. Вийти")
        choice = input("Виберіть опцію (1-5): ")

        if choice == "1":
            add_service()
        elif choice == "2":
            show_services()
        elif choice == "3":
            update_service()
        elif choice == "4":
            delete_service()
        elif choice == "5":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.\n")
if __name__ == "__main__":
    main()

def binarytext(text):
    return ''.join(format(ord(char), '08b') for char in text)

def encode(message, text):
    binary_message = binarytext(message)  # Перетворюємо повідомлення в двійкове
    encoded_text = []  # Тут буде зберігатися зашифрований текст
    binary_index = 0  # Індекс для бітів повідомлення

    words = text.split()  # Розбиваємо текст на слова

    for i in range(len(words) - 1):
        encoded_text.append(words[i])
        
        # Якщо є ще біти для шифрування
        if binary_index < len(binary_message):
            bit = binary_message[binary_index]
            if bit == '0':
                encoded_text.append('')  # Один пробіл
            else:
                encoded_text.append('  ')  # Два пробіли
            binary_index += 1

    encoded_text.append(words[-1])  # Додаємо останнє слово
    return ' '.join(encoded_text)

# Тестовий приклад
message = input()
text = "Here we will hide our message."
encoded = encode(message, text)
print("Зашифрований текст:")
print(encoded)
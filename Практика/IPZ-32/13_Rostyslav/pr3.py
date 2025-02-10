import requests
import telebot
import deepl
import time

token = input("Token:")
DeeplKey = input("Deepl Key:")

bot = telebot.TeleBot(token)

print("Bot Active!")

@bot.message_handler(commands=['start'])
def HaHaha(message):
    while True:    
        r = requests.get('https://v2.jokeapi.dev/joke/Any')
        data = r.json()
        if data['type'] == 'single':
            joke = data['joke']
        elif data['type'] == 'twopart':
            joke = f"{data['setup']} \n {data['delivery']}"
        
        translator = deepl.Translator(DeeplKey)
        jokeT = translator.translate_text(joke, target_lang="UK")
        bot.send_message(message.chat.id, jokeT)

        time.sleep(120)



bot.polling(non_stop=True)
# Telegram Joke Bot with DeepL Translation

This Python script creates a Telegram bot that sends jokes in Ukrainian every two minutes. It utilizes the JokeAPI to fetch jokes and DeepL for translation.

## Requirements

- Python 3.x
- `requests` library: `pip install requests`
- `pyTelegramBotAPI` library: `pip install pyTelegramBotAPI`
- `deepl` library: `pip install deepl`

## Setup

1.  **Obtain API Keys:**
    - Get a Telegram Bot token from BotFather on Telegram.
    - Get a DeepL API key from the DeepL website.

2.  **Install Dependencies:**
    ```bash
    pip install requests pyTelegramBotAPI deepl
    ```

3.  **Run the Script:**
    - Save the code as a Python file (e.g., `joke_bot.py`).
    - Execute the script: `python joke_bot.py`
    - The script will prompt you to enter your Telegram Bot token and DeepL API key.

## How it Works

The script does the following:

1.  **Initialization:**
    - Imports necessary libraries.
    - Prompts the user for the Telegram Bot token and DeepL API key.
    - Creates a Telegram bot instance using the provided token.
    - Prints "Bot Active!" to indicate successful initialization.

2.  **`/start` Command Handler:**
    - Defines a function `HaHaha` that is triggered when a user sends the `/start` command to the bot.
    - Enters an infinite loop (`while True`) to continuously fetch and send jokes.

3.  **Joke Fetching:**
    - Uses the `requests` library to fetch a joke from the JokeAPI (`https://v2.jokeapi.dev/joke/Any`).
    - Parses the JSON response to extract the joke text, handling both single and two-part jokes.

4.  **Translation:**
    - Creates a DeepL translator instance using the provided API key.
    - Translates the fetched joke to Ukrainian using `translator.translate_text(joke, target_lang="UK")`.

5.  **Sending the Joke:**
    - Sends the translated joke to the user who initiated the `/start` command using `bot.send_message()`.

6.  **Delay:**
    - Pauses the loop for 120 seconds (2 minutes) using `time.sleep(120)` before fetching the next joke.

7.  **Polling:**
    - Starts the Telegram bot polling to listen for incoming messages and commands using `bot.polling(non_stop=True)`.  The `non_stop=True` argument ensures the bot continues to run even if errors occur.

## Usage

1.  Start a chat with your bot on Telegram.
2.  Send the `/start` command.
3.  The bot will start sending you jokes in Ukrainian every 2 minutes.

## Notes

- The script uses an infinite loop, so it will continue running until it is manually stopped (e.g., by pressing Ctrl+C in the terminal).
- Error handling could be improved to handle potential issues with the API requests or translation process.
- Consider adding more features, like user preferences for joke categories or translation languages.
- Be mindful of the usage limits of the DeepL API.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.

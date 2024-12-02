#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <chrono>
#include <ctime>

using namespace std;

void logEvent(const string& event) {
    ofstream logFile("hangman_log.txt", ios_base::app);
    if (logFile.is_open()) {
        auto now = chrono::system_clock::now();
        time_t now_time = chrono::system_clock::to_time_t(now);
        char timeStr[26];
        ctime_s(timeStr, sizeof(timeStr), &now_time);
        timeStr[strlen(timeStr) - 1] = '\0';
        logFile << "[" << timeStr << "] " << event << endl;
    }
}

void displayHangman(int incorrectGuesses) {
    vector<string> hangmanStages = {
        "  +---+\n      |\n      |\n      |\n     ===",
        "  +---+\n  O   |\n      |\n      |\n     ===",
        "  +---+\n  O   |\n  |   |\n      |\n     ===",
        "  +---+\n  O   |\n /|   |\n      |\n     ===",
        "  +---+\n  O   |\n /|\\  |\n      |\n     ===",
        "  +---+\n  O   |\n /|\\  |\n /    |\n     ===",
        "  +---+\n  O   |\n /|\\  |\n / \\  |\n     ==="
    };

    cout << hangmanStages[incorrectGuesses] << endl;
}

void displayWord(const string& word, const vector<bool>& guessed) {
    for (int i = 0; i < word.size(); i++) {
        if (guessed[i]) {
            cout << word[i] << ' ';
        }
        else {
            cout << "_ ";
        }
    }
    cout << endl;
}

bool isWordGuessed(const vector<bool>& guessed) {
    for (bool letterGuessed : guessed) {
        if (!letterGuessed) {
            return false;
        }
    }
    return true;
}

void updateWinsFile(int wins) {
    ofstream winsFile("hangman_wins.txt");
    if (winsFile.is_open()) {
        winsFile << "Победа: " << wins << endl;
    }
}

int readWinsFile() {
    ifstream winsFile("hangman_wins.txt");
    int wins = 0;
    if (winsFile.is_open()) {
        string label;
        winsFile >> label >> wins;
    }
    return wins;
}

void playHangman(const string& word) {
    int incorrectGuesses = 0;
    vector<bool> guessed(word.size(), false);
    vector<char> incorrectLetters;

    while (incorrectGuesses < 6) {
        system("cls");
        displayHangman(incorrectGuesses);
        displayWord(word, guessed);

        cout << "Incorrect guesses: ";
        for (char letter : incorrectLetters) {
            cout << letter << ' ';
        }
        cout << endl;

        cout << "Enter your guess: ";
        char guess;
        cin >> guess;

        logEvent("Player guessed: " + string(1, guess));

        if (find(incorrectLetters.begin(), incorrectLetters.end(), guess) != incorrectLetters.end()) {
            cout << "You already guessed that letter. Try again." << endl;
            logEvent("Repeated guess: " + string(1, guess));
            continue;
        }

        bool correctGuess = false;
        for (int i = 0; i < word.size(); i++) {
            if (word[i] == guess) {
                guessed[i] = true;
                correctGuess = true;
            }
        }

        if (!correctGuess) {
            incorrectLetters.push_back(guess);
            incorrectGuesses++;
        }

        if (isWordGuessed(guessed)) {
            system("cls");
            displayHangman(incorrectGuesses);
            displayWord(word, guessed);
            cout << "Congratulations! You guessed the word: " << word << endl;
            logEvent("Victory! Player won the game.");
            int wins = readWinsFile();
            wins++;
            updateWinsFile(wins);
            return;
        }
    }

    system("cls");
    displayHangman(6);
    cout << "Game over! The word was: " << word << endl;
    logEvent("Player lost the game. The word was: " + word);
}

int main() {
    cout << "Welcome to Hangman!" << endl;

    int wins = readWinsFile();
    cout << "Total wins: " << wins << endl;

    cout << "Player 1, enter the word to guess: ";
    string word;
    cin >> word;
    system("cls");

    logEvent("New game started. Word to guess: " + word);
    playHangman(word);

    return 0;
}

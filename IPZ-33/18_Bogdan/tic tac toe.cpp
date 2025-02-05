#include <iostream>

using namespace std;

const int BOARD_SIZE = 3;
char board[BOARD_SIZE][BOARD_SIZE] = {{'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'}};
char currentMarker;
int currentPlayer;

void drawBoard() {
    system("cls");
    cout << "Tic Tac Toe Game" << endl;
    for (int i = 0; i < BOARD_SIZE; ++i) {
        for (int j = 0; j < BOARD_SIZE; ++j) {
            cout << board[i][j];
            if (j < BOARD_SIZE - 1) cout << " | ";
        }
        cout << endl;
        if (i < BOARD_SIZE - 1) cout << "--|---|--" << endl;
    }
}

bool placeMarker(int slot) {
    int row = (slot - 1) / BOARD_SIZE;
    int col = (slot - 1) % BOARD_SIZE;

    if (board[row][col] != 'X' && board[row][col] != '0') {
        board[row][col] = currentMarker;
        return true;
    }
    return false;
}

int winner() {
    // Check rows and columns
    for (int i = 0; i < BOARD_SIZE; ++i) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2]) return currentPlayer;
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i]) return currentPlayer;
    }

    // Check diagonals
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2]) return currentPlayer;
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0]) return currentPlayer;

    return 0;
}

void swapPlayerAndMarker() {
    if (currentMarker == 'X') currentMarker = 'O';
    else currentMarker = 'X';

    if (currentPlayer == 1) currentPlayer = 2;
    else currentPlayer = 1;
}

void game() {
    cout << "Player 1, choose your marker (X or O): ";
    char marker_p1;
    cin >> marker_p1;

    currentPlayer = 1;
    currentMarker = marker_p1;

    drawBoard();
    
    int playerWon;
    for (int i = 0; i < BOARD_SIZE * BOARD_SIZE; ++i) {
        cout << "It's player " << currentPlayer << "'s turn. Enter your slot: ";
        int slot;
        cin >> slot;

        if (slot < 1 || slot > 9) {
            cout << "Invalid slot! Please enter a number between 1 and 9." << endl;
            i--;
            continue;
        }

        if (!placeMarker(slot)) {
            cout << "Slot occupied! Try another slot!" << endl;
            i--;
            continue;
        }

        drawBoard();
        playerWon = winner();

        if (playerWon == 1) {
            cout << "Player 1 won! Congratulations!" << endl;
            break;
        }
        if (playerWon == 2) {
            cout << "Player 2 won! Congratulations!" << endl;
            break;
        }

        swapPlayerAndMarker();
    }

    if (playerWon == 0) {
        cout << "It's a draw!" << endl;
    }
}

int main() {
    game();
    return 0;
}
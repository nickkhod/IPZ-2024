#ifndef SAVE_LOAD_H
#define SAVE_LOAD_H

#include <fstream>

using namespace std;

void SaveGame(int x, int y, int fruitX, int fruitY, int score, int nTail, int dir, int tailX[], int tailY[]) {
    ofstream file("snake_save.txt");
    if (file.is_open()) {
        file << x << " " << y << " " << fruitX << " " << fruitY << " " << score << " " << nTail << " " << dir << endl;
        for (int i = 0; i < nTail; ++i) {
            file << tailX[i] << " " << tailY[i] << " ";
        }
        file.close();
    }
}

void LoadGame(int &x, int &y, int &fruitX, int &fruitY, int &score, int &nTail, int &dir, int tailX[], int tailY[]) {
    ifstream file("snake_save.txt");
    if (file.is_open()) {
        file >> x >> y >> fruitX >> fruitY >> score >> nTail >> dir;
        for (int i = 0; i < nTail; ++i) {
            file >> tailX[i] >> tailY[i];
        }
        file.close();
    }
}

#endif
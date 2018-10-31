/*
 * znaki.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>

using namespace std;

void licz_znaki(char tb[], int roz) {
    //~for(int i=0; i < roz; i++) {
        //~cout << tb[i];
    //~}
    int i = 0;
    int biale, inter, reszta;
    biale = inter = reszta = 0;
    while (tb[i] != '\0') {
        if (tb[i] == ' ' || tb[i] == '\t') biale++;  //or = ||
        else id (tb[i] == ',' || '.') inter++'
        else reszta++;
        i++;
    }
    cout << "Białych: " << biale <<
}

int main(int argc, char **argv)
{
    const int rozmiar = 20;
    char znaki[rozmiar];
    cin.getline(znaki, rozmiar);
    licz_znaki(znaki, cin.gcount());
	return 0;
}


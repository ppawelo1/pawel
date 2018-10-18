/*
 * liczby23.cpp
 * 
 * Copyright 2018  <>
 * 
 */

#include <iostream>

using namespace std;

int liczby2() {
    int ile = 0;
    for (int i = 1; i < 10; i++) {
         for (int j = 1; j < 10; j++) {
             if (i != j){
                 cout << i << j << " ";
                 ile++;
             }
        }
    }
    return ile;
}

int liczby3() {
    int ile = 0;
    for (int i = 1; i < 10; i++) {
        for (int j = 1; j < 10; j++) {
            for (int k = 1; k < 10; k++) {
                if (i != j && i != k && j != k){
                   cout << i << j << k << " ";
                   ile++;
                }
             }
        }
    }
    return ile;
}

int main(int argc, char **argv)
{
    //int ile = liczby2();
    //cout << "\n\nLiczb 2-cyfrowych:" << ile << endl;
    int ile = liczby3();
	cout << "\n\nLiczb 3-cyfrowych:" << ile << endl;
	return 0;
}



#!/usr/bin/env python
# -*- coding: utf-8 -*-


def liczby2():
    """
    Funkcja drukuje wszystkie liczby 2 cyfrowe 
    w ktorych cyfry nie powtarzaja sie. Funkcja zwraca ich liczbę.
    Wykluczone liczby 11 
    """
    licznik=0
    for i in range(1,10):
        for j in range(10):
            if i!=j:
                print(i*10+j, end=" ")
                licznik+=1
                
    print()
    return licznik
            
    
def liczby3():
    licznik=0
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                if i!=j and j!=k and i!=k:
                    print(i*100+j*10+k,end=" ")
                    licznik+=1
    print()
return licznik

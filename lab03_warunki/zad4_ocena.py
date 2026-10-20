# Lab 03 – Zadanie 4 (★): Ocena z przedmiotu
#
# Program wczytuje liczbę punktów (0–100) i wypisuje ocenę według progów
# z sylabusa naszego przedmiotu:
#     > 91        -> 5
#     > 83 – 91   -> 4.5
#     > 75 – 83   -> 4
#     > 67 – 75   -> 3.5
#     > 60 – 67   -> 3
#     <= 60       -> 2
#
# Przykład:  Ocena: 4.5
# Uwaga: w zachęcie input() nie wypisuj liczb (np. „0-100”) – testy szukają liczb w wyjściu.

# TODO: Twój kod poniżej
punkty = float(input("Podaj liczbę punktów: "))
if punkty > 91:
    print("Ocena: 5")
elif punkty > 83:
    print("Ocena: 4.5")
elif punkty > 75:
    print("Ocena: 4")
elif punkty > 67:
    print("Ocena: 3.5")
elif punkty > 60:
    print("Ocena: 3")
else:
    print("Ocena: 2")
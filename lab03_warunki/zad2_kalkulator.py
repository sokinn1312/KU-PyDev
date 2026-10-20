# Lab 03 – Zadanie 2 (★): Kalkulator z wyborem działania
#
# Program wczytuje kolejno: liczbę, operator (+, -, *, /) i drugą liczbę,
# a potem wypisuje wynik, np.:  8.0 * 2.0 = 16.0
#
# Obsłuż przypadki szczególne instrukcją if:
#   - dzielenie przez zero  -> "Nie można dzielić przez zero"
#   - inny operator         -> "Nieznany operator"

# TODO: Twój kod poniżej

liczba1 = float(input("Podaj pierwszą liczbę: "))
operator = input("Podaj operator (+, -, *, /): ")
liczba2 = float(input("Podaj drugą liczbę: "))
if operator == "+":
    wynik = liczba1 + liczba2
    print(f"{liczba1} + {liczba2} = {wynik}")
elif operator == "-":
    wynik = liczba1 - liczba2
    print(f"{liczba1} - {liczba2} = {wynik}")
elif operator == "*":
    wynik = liczba1 * liczba2
    print(f"{liczba1} * {liczba2} = {wynik}")
elif operator == "/":
    if liczba2 == 0:
        print("Nie można dzielić przez zero")
    else:
        wynik = liczba1 / liczba2
        print(f"{liczba1} / {liczba2} = {wynik}")
else:
    print("Nieznany operator")
# Lab 01 – Zadanie 2 (★): Wizytówka
#
# Program pyta użytkownika kolejno o:
#   1. imię,
#   2. nazwisko,
#   3. rok urodzenia (liczba całkowita),
# a potem wypisuje jedno zdanie, np.:
#     Nazywam się Anna Kowalska i w 2026 roku kończę 20 lat.
#
# Wskazówki:
#   - input() zawsze zwraca tekst (str) – rok zamień na liczbę: int(...)
#   - użyj f-stringa: f"Nazywam się {first_name} ..."

CURRENT_YEAR = 2026

# TODO: Twój kod poniżej

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
rok_urodzenia = int(input("Podaj rok urodzenia: "))
wiek = CURRENT_YEAR - rok_urodzenia
print(f"Nazywam się {imie} {nazwisko} i w {CURRENT_YEAR} roku kończę {wiek} lat.")
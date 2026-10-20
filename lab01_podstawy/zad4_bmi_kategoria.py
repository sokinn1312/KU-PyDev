# Lab 01 – Zadanie 4 (☆, dodatkowe): Kategoria BMI
#
# Rozbuduj kalkulator BMI: po obliczeniu wypisz także kategorię (wg WHO):
#     BMI < 18.5          -> niedowaga
#     18.5 <= BMI < 25    -> waga prawidłowa
#     25 <= BMI < 30      -> nadwaga
#     BMI >= 30           -> otyłość
#
# To zadanie wymaga instrukcji if / elif / else, którą dokładnie poznasz
# w labie 03. Spróbuj już teraz – składnię znajdziesz na slajdach.

# TODO: Twój kod poniżej

wzrost = float(input("Podaj wzrost w metrach (np. 1.75): "))
masa = float(input("Podaj masę w kilogramach: "))
bmi = masa / (wzrost ** 2)
print(f"Twoje BMI wynosi {bmi:.2f}")

if bmi < 18.5:
    print("Kategoria: niedowaga")
elif 18.5 <= bmi < 25:
    print("Kategoria: waga prawidłowa")
elif 25 <= bmi < 30:
    print("Kategoria: nadwaga")
else:
    print("Kategoria: otyłość")     
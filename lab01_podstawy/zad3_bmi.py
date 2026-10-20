# Lab 01 – Zadanie 3 (★): Kalkulator BMI
#
# BMI (Body Mass Index) = masa [kg] / (wzrost [m]) ** 2
#
# Program pyta o masę w kilogramach i wzrost w metrach (z KROPKĄ, np. 1.75),
# a potem wypisuje BMI zaokrąglone do 2 miejsc po przecinku, np.:
#     Twoje BMI wynosi 22.86
#
# Wskazówki:
#   - float(input(...)) zamienia tekst na liczbę zmiennoprzecinkową
#   - ** to potęgowanie, a f"{x:.2f}" formatuje liczbę do 2 miejsc

# TODO: Twój kod poniżej

masa = float(input("Podaj masę w kilogramach: "))
wzrost = float(input("Podaj wzrost w metrach (np. 1.75): "))
bmi = masa / (wzrost ** 2)
print(f"Twoje BMI wynosi {bmi:.2f}")    
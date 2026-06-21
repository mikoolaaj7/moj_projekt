liczba_a = input("Podaj pierwszą liczbę: ")
liczba_b = input("Podaj drugą liczbę: ")
dzialanie = input("Wybierz działanie (+, -, *, /): ")
liczba_a = int(liczba_a)
liczba_b = int(liczba_b)
wynik_dodawania = liczba_a + liczba_b
wynik_odejmowania = liczba_a - liczba_b
wynik_mnozenia = liczba_a * liczba_b
wynik_dzielenia = liczba_a / liczba_b
if dzialanie == "+":
    print("Wynik dodawania:", wynik_dodawania)
elif dzialanie == "-":
    print("Wynik odejmowania:", wynik_odejmowania)
elif dzialanie == "*":
    print("Wynik mnożenia:", wynik_mnozenia)
elif dzialanie == "/":
    print("Wynik dzielenia:", wynik_dzielenia)
else:
    print("Nieprawidłowe działanie")
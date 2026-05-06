\# Szyfr Cezara



\## Krótki opis działania szyfru



Szyfr Cezara to prosty szyfr podstawieniowy. Polega na przesunięciu każdej litery tekstu o określoną liczbę pozycji w alfabecie.



Przykład dla przesunięcia 3:



A → D  

B → E  

C → F  



Tekst `ABC` po zaszyfrowaniu daje wynik `DEF`.



\# Dostępne funkcje/metody w kodzie



\## `caesar\_cipher(text, shift)`



Funkcja szyfruje podany tekst za pomocą szyfru Cezara.



\### `caesar\_decrypt(text, shift)`



Funkcja odszyfrowuje tekst zaszyfrowany szyfrem Cezara.



\### `break\_caesar(cipher\_text)`



Funkcja próbuje złamać szyfr Cezara, sprawdzając wszystkie 26 możliwych przesunięć.



\# Argumenty funkcji



\## `caesar\_cipher(text, shift)`



\- `text` – tekst do zaszyfrowania

\- `shift` – liczba określająca przesunięcie liter w alfabecie



\### `caesar\_decrypt(text, shift)`



\- `text` – tekst do odszyfrowania

\- `shift` – liczba określająca przesunięcie



\### `break\_caesar(cipher\_text)`



\- `cipher\_text` – zaszyfrowany tekst, który ma zostać złamany



\# Co funkcja zwraca



\- `caesar\_cipher()` zwraca zaszyfrowany tekst

\- `caesar\_decrypt()` zwraca odszyfrowany tekst

\- `break\_caesar()` wypisuje możliwe odszyfrowania dla wszystkich przesunięć





\# Przykłady użycia



```python

result = caesar\_cipher("ABC", 3)

print(result)

```



Wynik:



```text

DEF

```



Przykład łamania szyfru:



```python

break\_caesar("KHOOR")

```



Jedno z możliwych rozwiązań:



```text

HELLO

```



\# Uwagi



Program obsługuje wielkie litery alfabetu A-Z. Inne znaki pozostają bez zmian.


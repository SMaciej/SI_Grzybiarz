# SI_Grzybiarz
Prosty projekt na zajęcia ze sztucznej inteligencji. Składa się z następujących modułów:

## generator.py
Generator ma za zadanie generować czytelną mapę dla naszego grzybiarza za pomocą następujących zasad:
- Na początku rozmieszcza na mapie poszczególne gatunki drzew, zgodnie z ich prawdopodobieństwami i podanym odstępem pomiędzy nimi.
- Następnie zapełnia mapę obiektami gruntu, w podanym odstępie od drzew i prawdopodobieństwem.
- Na koniec na mapie pojawiają się grzyby - również w podanym odstępie od drzew i prawdopodobieństwem. Prawdopodobieństwo wystąpienia danego grzyba zwiększa się, jeżeli generator wykryje w pobliżu "ulubione" drzewo danego gatunku grzyba.

## objects.py
Moduł zawierający definicje klas obiektów występujących na mapie.

## config.py
Plik konfiguracyjny, stanowiący bazę danych obiektów występujących na mapie.

## Ekran.py
Wyświetlanie grafiki (na razie tylko mapa wygenerowana przez generator).
Potrzebna jest biblioteka [pygame].
Wymagana jest wersja python 3.5

## Co mamy:
- Generator proceduralny mapy
- Wyświetlanie mapy
- Dodanie cech dodatkowych dla każdego grzyba
- Poruszanie się po danej ścieżce
- Zbieranie grzybów (wszystkich jak leci - trzeba zmienić to przez użycie SI)
- Kontrola myszy - wyświetlenie informacji o polu
- Pętla z tworzeniem nowej mapy
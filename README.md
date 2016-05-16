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

# Komunikacja Człowiek-Komputer (KCK) - Politechnika Poznańska

Repozytorium zawiera moje rozwiązania zadań z przedmiotu **Komunikacja Człowiek-Komputer** (5 semestr) na **Politechnice Poznańskiej**.

## Lab 1: Analiza Wyników Eksperymentów

Projekt z pierwszego laboratorium zajmuje się przetwarzaniem, analizą oraz wizualizacją danych z eksperymentów związanych z algorytmami ewolucyjnymi i koewolucyjnymi (m.in. 1-Coev, 1-Coev-RS, 1-Evol-RS, 2-Coev, 2-Coev-RS). Skrypty wczytują dane z plików CSV, dokonują odpowiednich obliczeń statystycznych, a następnie generują czytelne wykresy prezentujące wyniki.
## Wykorzystane technologie i biblioteki

Do realizacji projektu użyto języka **Python** wraz z następującymi bibliotekami:
- **Pandas** – do wczytywania plików CSV (`pd.read_csv`) oraz sprawnego operowania na danych tabelarycznych (DataFrame, wyciąganie kolumn, iteracja po wierszach).
- **NumPy** – do tworzenia macierzy i wektorów (np. `np.zeros`), które przechowują zagregowane wyniki potrzebne do wygenerowania wykresów.
- **Matplotlib** (`matplotlib.pyplot`) – kluczowa biblioteka wykorzystana do tworzenia wizualizacji (wykresy liniowe, pudełkowe, zarządzanie osiami, zapis do PDF).

## Struktura projektu i zaimplementowane rozwiązania

W ramach projektu przygotowano dwa główne skrypty ilustrujące postęp prac i różne stopnie zaawansowania wizualizacji.

### `task1.py` - Podstawowa wizualizacja
Skrypt ten stanowi wstępną analizę wyników:
1. Wczytuje pięć zestawów danych eksperymentalnych z katalogu `dane/`.
2. Dla każdego eksperymentu oblicza średnią wartość wierszową (z pominięciem pierwszych dwóch kolumn identyfikacyjnych).
3. Wykorzystuje prosty wykres liniowy (`plt.plot`), aby zaprezentować **odsetek wygranych gier** w zależności od **liczby rozegranych gier**.

### `task2.py` - Zaawansowana wizualizacja i statystyka
Ten skrypt rozwija podejście z pierwszego pliku, dodając znacznie bardziej profesjonalną i czytelną formę prezentacji z wykorzystaniem tzw. subplotów (`plt.subplots(1, 2)`):

**Lewy wykres (Wykres liniowy z podwójną osią):**
- Przedstawia krzywe uczenia dla wszystkich 5 algorytmów na przestrzeni czasu.
- Zastosowano **różne znaczniki** (kółka, trójkąty, gwiazdki, kwadraty) dla łatwiejszego odróżnienia poszczególnych metod eksperymentalnych.
- Dodano **podwójną oś X** (ang. *twin axis*). Dolna oś odzwierciedla liczbę rozegranych gier (przeskalowaną $\times 1000$), a górna ("Pokolenie") pozwala jednocześnie zorientować się w numeracji iteracji algorytmu.
- Wprowadzono ograniczenia zakresów osi (`set_xlim`, `set_ylim`) oraz pomocniczą siatkę w tle.

**Prawy wykres (Wykres pudełkowy - Boxplot):**
- Analizuje wariancję oraz rozkład wyników w **ostatnim pokoleniu** każdego z algorytmów.
- Prezentuje dane w postaci wyciętych wykresów pudełkowych (ang. *notched boxplots*), obrazując średnie, mediany i kwartyle.
- Znacząco dostosowano estetykę poprzez właściwości `meanprops`, `whiskerprops` i `boxprops`, używając predefiniowanych kolorów, stylów linii oraz znaczników.
- Oś Y na prawym wykresie celowo przeniesiono na prawą stronę za pomocą `yaxis.tick_right()`, aby nie zlewała się z poprzednim wykresem.

Gotowa, podwójna wizualizacja jest ostatecznie eksportowana do pliku wektorowego **`KCK_plot.pdf`**, który zapewnia bezstratną jakość na potrzeby raportów lub publikacji.

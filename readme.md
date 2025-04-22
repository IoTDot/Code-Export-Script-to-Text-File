<a id="top"></a>
<p align="left">
  <a href="#en">🇬🇧 English</a> |
  <a href="#pl">🇵🇱 Polski</a>
</p>

<a id="en"></a>

# Code Export Script to Text File _🇬🇧_

This Python script is designed to automatically collect the contents of code files from a specified folder within your VS Code workspace and export them into a single text file. This is especially useful for quickly sharing code context, analysis, or archiving.

## Features

*   **Single File Export:** Combines the contents of multiple files into one `.txt` file.
*   **VS Code Workspace Context:** Operates based on the current working folder (assumed to be the main project folder opened in VS Code).
*   **Configurable Source Folder:** You can define which subfolder (or the entire workspace) is the source for export.
*   **Configurable Output Folder:** The output file is created in a dedicated subfolder (`export_code` by default) within the workspace.
*   **Ignore File Extensions:** Define a list of file extensions to ignore during export (e.g. `.tmp`, `.bak`, `.pyc`).
*   **Ignore Paths:** Define folders or files (relative to the workspace) to completely skip (e.g. `.git`, `venv`, `node_modules`, the export folder itself).
*   **Preserve Structure (in headers):** Each code segment in the output file is preceded by a header indicating its original relative path.
*   **Encoding Handling:** Tries to read files using UTF-8 encoding while ignoring errors to prevent crashes due to unusual characters.

## Requirements

*   **Python 3:** Ensure Python 3 is installed and accessible via your system path.
*   **VS Code Workspace:** Run the script from the VS Code terminal with the project folder open as a workspace.
*   **(Optional) Python Extension for VS Code:** For using the run button (▶️).

## Installation / Setup

1.  **Save the Script:** Save the Python code as a `.py` file (e.g., `export_script.py`) in the **root folder** of your VS Code workspace. This is crucial for correct relative path handling, especially when using the run button.
2.  **Configure:** Open the `export_script.py` file in the editor and adjust the variables in the `--- Configuration ---` section according to your needs.

## Configuration

All configuration options are located at the top of the `export_script.py` file in the section marked `--- Configuration ---`.

```python
# --- Configuration ---

# Source folder RELATIVE to the VS Code workspace folder.
# '.' means the whole workspace. You can change this to 'src' or 'scripts', for example.
FOLDER_ZRODLOWY_RELATYWNY = '.'

# Name of the folder where the output file will be created (relative to workspace)
FOLDER_EXPORTU_NAZWA = 'export_code'
# Name of the output file
PLIK_EXPORTU_NAZWA = 'export.txt'

# Add extensions (with dot!) you want to skip in the export.
# Extensions are checked case-insensitively (e.g. .TMP and .tmp are both ignored)
POMIJANE_ROZSZERZENIA = {".tmp", ".bak"}

# Additional folders/files to skip (paths RELATIVE to workspace)
# Important to skip the export folder itself to avoid self-inclusion
POMIJANE_SCIEZKI = {FOLDER_EXPORTU_NAZWA}

# --- End of Configuration ---
```

*   **`FOLDER_ZRODLOWY_RELATYWNY`**: Relative path to the folder from which files will be exported. Default `'.'` means the entire workspace. Change to `'src'` to export only from the `src` folder.
*   **`FOLDER_EXPORTU_NAZWA`**: Name of the subfolder created within the workspace to hold the output file. Default is `'export_code'`.
*   **`PLIK_EXPORTU_NAZWA`**: Name of the text file to which the exported code will be saved. Default is `'export.txt'`.
*   **`POMIJANE_ROZSZERZENIA`**: A set of file extensions to ignore. Make sure to include the dot (e.g. `".log"`). Case-insensitive.
*   **`POMIJANE_SCIEZKI`**: A set of relative paths (folders or files) to be completely skipped. Ensure the export folder is included here to prevent self-inclusion.

## Running the Script

There are two main ways to run the script within the VS Code environment:

### Method 1: Using the Integrated Terminal (recommended for full control)

1.  Open your project (workspace) in VS Code.
2.  Open the integrated terminal (`Terminal` menu -> `New Terminal` or `Ctrl+\``). **Ensure it's running in the main workspace folder.**
3.  Run the following command (replace `export_script.py` with your actual script name if different):

    ```bash
    python export_script.py
    ```
    or if using `python3`:
    ```bash
    python3 export_script.py
    ```
4.  The script will begin processing files and show progress/output in the terminal.

### Method 2: Using the "Run Python File" Button (requires Python extension)

1.  Ensure you have the official [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) installed in VS Code.
2.  Open the script file (e.g. `export_script.py`) in the VS Code editor. **Make sure it resides in the root of the workspace.**
3.  Click the ▶️ "Run Python File" button in the top-right corner of the editor.

    *   **Important:** This method runs the script in the context of the folder where the script file resides. So it **must** be located in the root workspace folder for relative paths (`FOLDER_ZRODLOWY_RELATYWNY`, `POMIJANE_SCIEZKI`) to resolve correctly.
    *   Output messages (from `print`) will appear in the "OUTPUT" or "TERMINAL" pane at the bottom, depending on your Python extension settings.

Regardless of the method, the script will read its configuration, process the files accordingly, and create the result file in the export folder.

## Output

Upon successful execution:

1.  A subfolder defined by `FOLDER_EXPORTU_NAZWA` (default `export_code`) will be created in the root of the workspace if it doesn't already exist.
2.  Inside this folder, a text file named as per `PLIK_EXPORTU_NAZWA` (default `export.txt`) will be generated.
3.  This file will contain the combined contents of all *non-skipped* files found in `FOLDER_ZRODLOWY_RELATYWNY`. Each code segment will be preceded by a comment with the original file path, for example:

    ```
    # --- CODE EXPORT START ---
    # Source: /path/to/your/workspace
    # Skipped extensions: .tmp, .bak
    # Skipped paths: export_code
    #

    ========================================
    === File: main.py
    ========================================

    # Content of main.py
    print("Hello, World!")


    ========================================
    === File: utils/helpers.py
    ========================================

    # Content of utils/helpers.py
    def helper_function():
        pass

    # --- CODE EXPORT END ---
    ```

## Important Notes

*   **Overwriting:** Each run of the script **overwrites** the existing `export.txt`. Rename or backup if you want to keep previous versions.
*   **File Encoding:** The script tries to read source files as UTF-8, ignoring errors. Unusual characters from other encodings may be skipped or replaced.
*   **Large Projects:** For very large projects with many files, the resulting `export.txt` can become quite large.
*   **Skipping Important Folders:** Make sure `POMIJANE_SCIEZKI` includes all folders you don't want to export (e.g., dependency folders, `.git`, virtual environments, etc.).

[🔝 Back to top / Powrót na górę](#top)

***
***

<a id="pl"></a>

# Skrypt Eksportu Kodu do Pliku Tekstowego _🇵🇱_

Ten skrypt Pythona służy do automatycznego zbierania zawartości plików kodu z określonego folderu w ramach Twojego workspace VS Code i eksportowania ich do jednego, zbiorczego pliku tekstowego. Jest to przydatne np. do szybkiego udostępniania kontekstu kodu, analizy lub archiwizacji.

## Funkcjonalność

*   **Eksport do jednego pliku:** Łączy zawartość wielu plików w jeden plik `.txt`.
*   **Kontekst Workspace VS Code:** Działa w oparciu o bieżący folder roboczy (zakładamy, że jest to główny folder projektu otwarty w VS Code).
*   **Konfigurowalne źródło:** Możesz określić, który podfolder (lub cały workspace) ma być źródłem eksportu.
*   **Konfigurowalny folder wynikowy:** Plik wynikowy jest tworzony w dedykowanym podfolderze (`export_code` domyślnie) w ramach workspace.
*   **Pomijanie rozszerzeń:** Możliwość zdefiniowania listy rozszerzeń plików, które mają być ignorowane podczas eksportu (np. `.tmp`, `.bak`, `.pyc`).
*   **Pomijanie ścieżek:** Możliwość zdefiniowania listy folderów lub plików (względnych do workspace), które mają być całkowicie pominięte (np. `.git`, `venv`, `node_modules`, sam folder eksportu).
*   **Zachowanie struktury (w nagłówkach):** W pliku wynikowym każdy fragment kodu z danego pliku jest poprzedzony nagłówkiem wskazującym jego oryginalną, względną ścieżkę.
*   **Obsługa kodowania:** Próbuje odczytać pliki jako UTF-8, ignorując błędy (co zapobiega awarii skryptu przy nietypowych znakach, ale może pominąć niektóre z nich).

## Wymagania

*   **Python 3:** Upewnij się, że masz zainstalowany Python 3 i jest on dostępny w ścieżce systemowej.
*   **Workspace VS Code:** Skrypt powinien być uruchamiany z terminala VS Code, gdy otwarty jest folder projektu (workspace).
*   **(Opcjonalnie) Rozszerzenie Python dla VS Code:** Do użycia metody uruchamiania przez przycisk ▶️.

## Instalacja / Setup

1.  **Zapisz skrypt:** Zapisz kod Pythona jako plik `.py` (np. `export_script.py`) w **głównym folderze** Twojego workspace VS Code. Jest to ważne dla poprawnego działania ścieżek względnych, zwłaszcza przy uruchamianiu przez przycisk.
2.  **Skonfiguruj:** Otwórz plik `export_script.py` w edytorze i dostosuj zmienne w sekcji `--- Konfiguracja ---` zgodnie ze swoimi potrzebami.

## Konfiguracja

Wszystkie opcje konfiguracyjne znajdują się na początku pliku `export_script.py` w sekcji oznaczonej `--- Konfiguracja ---`.

```python
# --- Konfiguracja ---

# Folder źródłowy WZGLĘDEM folderu workspace VS Code.
# '.' oznacza cały folder workspace. Możesz zmienić na np. 'src' lub 'scripts'.
FOLDER_ZRODLOWY_RELATYWNY = '.'

# Nazwa folderu, w którym zostanie utworzony plik wynikowy (względem workspace)
FOLDER_EXPORTU_NAZWA = 'export_code'
# Nazwa pliku wynikowego
PLIK_EXPORTU_NAZWA = 'export.txt'

# Dodaj rozszerzenia (z kropką!), które chcesz pominąć w eksporcie.
# Rozszerzenia są sprawdzane bez względu na wielkość liter (np. .TMP i .tmp będą pominięte)
POMIJANE_ROZSZERZENIA = {".tmp", ".bak"}
# Przykład dodania kolejnych:
# POMIJANE_ROZSZERZENIA = {".tmp", ".bak", ".log", ".obj", ".pyc", ".git", ".vscode"}

# Dodatkowe foldery/pliki do pominięcia (ścieżki WZGLĘDEM workspace)
# Ważne, aby pominąć sam folder eksportu, by nie dołączał się do siebie!
POMIJANE_SCIEZKI = {FOLDER_EXPORTU_NAZWA}
# Przykład:
# POMIJANE_SCIEZKI = {FOLDER_EXPORTU_NAZWA, '.git', '.vscode', 'venv', '__pycache__'}

# --- Koniec Konfiguracji ---
```

*   **`FOLDER_ZRODLOWY_RELATYWNY`**: Ścieżka do folderu, z którego mają być eksportowane pliki, *względna* do głównego folderu workspace. Domyślnie `'.'` oznacza cały workspace. Zmień na np. `'src'`, jeśli chcesz eksportować tylko zawartość folderu `src`.
*   **`FOLDER_EXPORTU_NAZWA`**: Nazwa podfolderu, który zostanie utworzony w workspace, aby pomieścić plik wynikowy. Domyślnie `'export_code'`.
*   **`PLIK_EXPORTU_NAZWA`**: Nazwa pliku tekstowego, do którego zostanie zapisany wyeksportowany kod. Domyślnie `'export.txt'`.
*   **`POMIJANE_ROZSZERZENIA`**: Zestaw (set) ciągów znaków reprezentujących rozszerzenia plików do pominięcia. Pamiętaj o kropce na początku (np. `".log"`). Wielkość liter jest ignorowana.
*   **`POMIJANE_SCIEZKI`**: Zestaw (set) ciągów znaków reprezentujących ścieżki do folderów lub plików, które mają być całkowicie zignorowane. Ścieżki podawaj *względnie* do głównego folderu workspace (np. `'.git'`, `'venv'`, `'node_modules'`). **Ważne:** Domyślnie zawiera `FOLDER_EXPORTU_NAZWA`, aby skrypt nie próbował dołączyć swojego wyniku do samego siebie.

## Uruchamianie skryptu

Istnieją dwa główne sposoby uruchomienia skryptu w środowisku VS Code:

**Metoda 1: Użycie zintegrowanego terminala (zalecane dla pełnej kontroli)**

1.  Otwórz swój projekt (workspace) w VS Code.
2.  Otwórz zintegrowany terminal w VS Code (menu `Terminal` -> `Nowy Terminal` lub skrót `Ctrl+` \`). **Upewnij się, że terminal jest uruchomiony w głównym folderze Twojego workspace.** Możesz to sprawdzić, patrząc na ścieżkę wyświetlaną w terminalu.
3.  Wpisz w terminalu następującą komendę (zastąp `export_script.py` rzeczywistą nazwą pliku, jeśli jest inna):

    ```bash
    python export_script.py
    ```
    lub jeśli używasz `python3`:
    ```bash
    python3 export_script.py
    ```
4.  Skrypt rozpocznie przetwarzanie plików, wyświetlając postęp i wyniki w terminalu.

**Metoda 2: Użycie przycisku "Run Python File" (wymaga rozszerzenia Python)**

1.  Upewnij się, że masz zainstalowane oficjalne rozszerzenie [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) dla VS Code.
2.  Otwórz plik skryptu (np. `export_script.py`) w edytorze VS Code. **Upewnij się, że plik skryptu znajduje się w głównym folderze workspace.**
3.  Znajdź przycisk ▶️ ("Run Python File") w prawym górnym rogu okna edytora.
4.  Kliknij ten przycisk.

    *   **Ważne:** Ta metoda uruchomi skrypt używając interpretera Pythona skonfigurowanego w VS Code. Skrypt będzie działał w kontekście *folderu, w którym znajduje się sam plik skryptu*. Dlatego **kluczowe jest, aby plik `export_script.py` znajdował się bezpośrednio w głównym folderze Twojego workspace**, aby ścieżki względne (`FOLDER_ZRODLOWY_RELATYWNY`, `POMIJANE_SCIEZKI`) były poprawnie interpretowane względem całego projektu.
    *   Wyniki działania skryptu (komunikaty `print`) zostaną wyświetlone w zakładce "OUTPUT" lub "TERMINAL" w dolnym panelu VS Code, w zależności od konfiguracji rozszerzenia Python.

Niezależnie od wybranej metody, skrypt odczyta swoją konfigurację, przetworzy pliki zgodnie z nią i utworzy plik wynikowy w folderze eksportu.

## Wynik (Output)

Po pomyślnym uruchomieniu skryptu:

1.  W głównym folderze workspace zostanie utworzony (jeśli nie istniał) podfolder o nazwie zdefiniowanej w `FOLDER_EXPORTU_NAZWA` (domyślnie `export_code`).
2.  Wewnątrz tego folderu znajdzie się plik tekstowy o nazwie zdefiniowanej w `PLIK_EXPORTU_NAZWA` (domyślnie `export.txt`).
3.  Plik ten będzie zawierał połączoną zawartość wszystkich *niepominiętych* plików znalezionych w `FOLDER_ZRODLOWY_RELATYWNY`. Każdy fragment kodu będzie poprzedzony komentarzem z oryginalną ścieżką pliku, np.:

    ```
    # --- POCZĄTEK EKSPORTU KODU ---
    # Źródło: /ścieżka/do/twojego/workspace
    # Pominięte rozszerzenia: .tmp, .bak
    # Pominięte ścieżki: export_code
    #

    ========================================
    === Plik: main.py
    ========================================

    # Zawartość pliku main.py
    print("Hello, World!")


    ========================================
    === Plik: utils/helpers.py
    ========================================

    # Zawartość pliku utils/helpers.py
    def helper_function():
        pass

    # --- KONIEC EKSPORTU KODU ---
    ```

## Ważne uwagi

*   **Nadpisywanie:** Każde uruchomienie skryptu **nadpisuje** istniejący plik `export.txt`. Jeśli chcesz zachować poprzednie wersje, zmień nazwę pliku wynikowego lub zrób kopię przed ponownym uruchomieniem.
*   **Kodowanie plików:** Skrypt próbuje odczytać pliki źródłowe przy użyciu kodowania UTF-8 i ignoruje błędy. Oznacza to, że nietypowe znaki w plikach o innym kodowaniu mogą zostać pominięte lub zastąpione.
*   **Duże projekty:** W przypadku bardzo dużych projektów z wieloma plikami, wynikowy plik `export.txt` może stać się bardzo duży.
*   **Pominięcie ważnych folderów:** Upewnij się, że lista `POMIJANE_SCIEZKI` zawiera wszystkie foldery, których nie chcesz eksportować (np. foldery z zależnościami, repozytoria git, pliki konfiguracyjne środowisk wirtualnych itp.).

[🔝 Back to top / Powrót na górę](#top)
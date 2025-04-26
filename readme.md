**<a id="top"></a>**  
<p align="left">  
  <a href="#en">🇬🇧 English</a> |  
  <a href="#pl">🇵🇱 Polski</a>  
</p>

<a id="en"></a>

# Code Export Script to Text File _🇬🇧_

This Python script automates collecting the contents of code files from a specified folder within your VS Code workspace and exports them into a single text file. It’s ideal for sharing code context, analysis, or archiving quickly.

## Features

- **Single File Export:** Merges multiple source files into one `.txt` file.  
- **Workspace Context:** Works relative to the current VS Code workspace root.  
- **Configurable Source Folder:** Choose a subfolder (e.g. `src`) or the entire workspace.  
- **Configurable Output Folder:** Output goes into a dedicated subfolder (default `export_code`).  
- **Ignore Extensions:** Skip files by extension (case-insensitive).  
- **Ignore Paths:** Skip entire folders/files (e.g. `.git`, `node_modules`, virtual environments, the export folder).  
- **Directory Tree Header:** Inserts a tree of the source directory at the top of the output.  
- **File Headers:** Each code block is preceded by its original relative path.  
- **Encoding Handling:** Reads with UTF‑8 and ignores errors to avoid crashes.

## Requirements

- **Python 3:** Installed and in your system PATH.  
- **VS Code Workspace:** Open the project root in VS Code.  
- **(Optional) Python Extension:** For running via the ▶️ button.

## Installation & Setup

1. **Save the Script**  
   Save the Python code as `export_script.py` in the **root** of your VS Code workspace.  
2. **Configure**  
   Open `export_script.py` and edit the `--- Configuration ---` section as needed.

## Configuration

All options live at the top of `export_script.py`:

```python
# --- Configuration ---

# Source folder RELATIVE to the workspace root.
# Default 'src'; use '.' for entire workspace.
FOLDER_ZRODLOWY_RELATYWNY = 'src'

# Output folder name (relative to workspace).
FOLDER_EXPORTU_NAZWA    = 'export_code'
# Output file name.
PLIK_EXPORTU_NAZWA      = 'export.txt'

# File extensions to skip (include leading dot, case-insensitive).
POMIJANE_ROZSZERZENIA = {'.tmp', '.bak'}

# Folders/files to skip (relative paths).
# Must include export folder to avoid self-inclusion.
POMIJANE_SCIEZKI = {
    FOLDER_EXPORTU_NAZWA,
    '.git',
    'node_modules',
    'venv',
    '__pycache__'
}

# Additional files to include at the end (relative to workspace).
DODATKOWE_PLIKI = [
    'platformio.ini',
]

# --- End of Configuration ---
```  

- **FOLDER_ZRODLOWY_RELATYWNY:** `'src'` by default. Use `'.'` to export the whole workspace.  
- **POMIJANE_SCIEZKI:** Common ignores: `.git`, `node_modules`, virtual envs, caches.

## Running the Script

### Method 1: Integrated Terminal (recommended)

1. Open the workspace in VS Code.  
2. Open Terminal (`Ctrl+\``). Ensure it’s at the workspace root.  
3. Run:
   ```bash
   python export_script.py
   # or python3 export_script.py
   ```
4. Watch progress in the terminal.

### Method 2: ▶️ Run Python File (requires Python extension)

1. Install the official [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).  
2. Open `export_script.py` in the editor (must be in workspace root).  
3. Click the ▶️ button in the editor toolbar.  
4. Output appears in the "OUTPUT"/"TERMINAL" pane.

> **Note:** This runs in the folder containing `export_script.py`, so it must live at the workspace root for relative paths to resolve correctly.

## Output Example

Upon successful run, `export_code/export.txt` will contain:

```
# --- DIRECTORY TREE (/home/user/project/src) ---
# src/
# ├── main.py
# └── utils/
#     └── helper.py
#
# --- CODE EXPORT START ---
# Source: /home/user/project/src
# Skipped extensions: .bak, .tmp
# Skipped paths: export_code, .git, node_modules, venv, __pycache__
#
========================================
=== File: main.py
========================================

# Content of main.py
print("Hello, World!")

========================================
=== File: utils/helper.py
========================================

# Content of helper.py
def helper(): pass

# --- CODE EXPORT END ---
```

## Troubleshooting & FAQ

**Q:** *Permission denied writing to export folder.*  
**A:** Check file system permissions or run with appropriate user rights.

**Q:** *`export.txt` too large?*  
**A:** Narrow `FOLDER_ZRODLOWY_RELATYWNY` or add more patterns to `POMIJANE_SCIEZKI`/`POMIJANE_ROZSZERZENIA`.

**Q:** *Unicode errors?*  
**A:** Script ignores decode errors; ensure files are UTF‑8 or adjust to another codec.

**Q:** *Missing files in export?*  
**A:** Verify your `POMIJANE_*` settings and that `src` folder exists.

[🔝 Back to top / Powrót na górę](#top)

***

<a id="pl"></a>

# Skrypt Eksportu Kodu do Pliku Tekstowego _🇵🇱_

Ten skrypt Pythona automatycznie zbiera zawartość plików kodu z określonego folderu w ramach workspace VS Code i eksportuje je do jednego pliku tekstowego. Świetnie nadaje się do szybkiego udostępniania kodu, analizy lub archiwizacji.

## Funkcjonalność

- **Eksport do jednego pliku:** Łączy wiele plików źródłowych w jeden plik `.txt`.  
- **Kontekst workspace:** Działa względem głównego katalogu projektu w VS Code.  
- **Konfigurowalne źródło:** Wybierz podfolder (np. `src`) lub cały workspace.  
- **Konfigurowalny folder wynikowy:** Wynik trafia do subfolderu (domyślnie `export_code`).  
- **Pomijanie rozszerzeń:** Ignoruje pliki według rozszerzenia (bez rozróżnienia wielkości liter).  
- **Pomijanie ścieżek:** Ignoruje foldery/pliki (np. `.git`, `node_modules`, `venv`, folder eksportu).  
- **Drzewo katalogów:** Dodaje drzewo katalogów źródłowych na początku pliku.  
- **Nagłówki plików:** Każdy fragment kodu ma nagłówek z jego oryginalną ścieżką.  
- **Obsługa kodowania:** Odczyt UTF‑8, ignoruje błędy kodowania.

## Wymagania

- **Python 3** zainstalowany i dostępny w PATH.  
- **Workspace VS Code** otwarty w VS Code.  
- **(Opcjonalnie) Rozszerzenie Python** dla przycisku ▶️.

## Instalacja i Konfiguracja

1. **Zapisz skrypt**  
   Umieść `export_script.py` w **głównym** folderze workspace.  
2. **Dostosuj konfigurację**  
   Edytuj sekcję `--- Configuration ---` w skrypcie.

## Konfiguracja

```python
# --- Konfiguracja ---

# Folder źródłowy względem workspace ('src' domyślnie, '.' = cały projekt)
FOLDER_ZRODLOWY_RELATYWNY = 'src'

# Folder wynikowy (względem workspace)
FOLDER_EXPORTU_NAZWA = 'export_code'
# Plik wynikowy
PLIK_EXPORTU_NAZWA   = 'export.txt'

# Rozszerzenia do pominięcia (z kropką)
POMIJANE_ROZSZERZENIA = {'.tmp', '.bak'}

# Ścieżki do pominięcia (foldery/pliki)
POMIJANE_SCIEZKI = {
    FOLDER_EXPORTU_NAZWA,
    '.git',
    'node_modules',
    'venv',
    '__pycache__'
}

# Dodatkowe pliki do dołączenia na końcu
DODATKOWE_PLIKI = [
    'platformio.ini',
]

# --- Koniec konfiguracji ---
```  

## Uruchamianie skryptu

### Metoda 1: Terminal (zalecane)

1. Otwórz projekt w VS Code.  
2. Otwórz terminal (`Ctrl+\``) w głównym folderze workspace.  
3. Uruchom:
   ```bash
   python export_script.py
   ```
4. Śledź postęp w terminalu.

### Metoda 2: ▶️ Run Python File (wymaga rozszerzenia)

1. Zainstaluj oficjalne rozszerzenie [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python).  
2. Otwórz `export_script.py` w VS Code (musi być w głównym folderze).  
3. Kliknij ▶️ w prawym górnym rogu.  
4. Wyniki zobaczysz w panelu "OUTPUT"/"TERMINAL".

> **Uwaga:** Skrypt uruchamia się w katalogu, gdzie leży plik, więc `export_script.py` musi być w root, by ścieżki działały poprawnie.

## Przykład wyniku

```
# --- DRZEWO KATALOGÓW (/home/user/project/src) ---
# src/
# ├── main.py
# └── utils/
#     └── helper.py
#
# --- POCZĄTEK EKSPORTU KODU ---
# Źródło: /home/user/project/src
# Pominięte rozszerzenia: .bak, .tmp
# Pominięte ścieżki: export_code, .git, node_modules, venv, __pycache__
#
========================================
=== Plik: main.py
========================================

# Zawartość main.py
print("Hello, World!")

========================================
=== Plik: utils/helper.py
========================================

# Zawartość helper.py
def helper(): pass

# --- KONIEC EKSPORTU KODU ---
```

## Rozwiązywanie problemów

**Uprawnienia:** Upewnij się, że masz prawo zapisu w folderze wynikowym.  
**Za duży plik?** Zawęź `FOLDER_ZRODLOWY_RELATYWNY` lub dodaj więcej wzorców do ignorowanych.  
**Błędy Unicode?** Skrypt ignoruje błędy kodowania; upewnij się, że pliki są UTF‑8 lub zmodyfikuj kodowanie.

[🔝 Back to top / Powrót na górę](#top)
import os
import sys
import io  # Potrzebne do obsługi kodowania plików

# --- Konfiguracja ---

# Folder źródłowy WZGLĘDEM folderu workspace VS Code.
FOLDER_ZRODLOWY_RELATYWNY = ''

# Nazwa folderu, w którym zostanie utworzony plik wynikowy (względnie do workspace)
FOLDER_EXPORTU_NAZWA = 'export_code'
# Nazwa pliku wynikowego
PLIK_EXPORTU_NAZWA = 'export.txt'

# Dodaj rozszerzenia (z kropką!), które chcesz pominąć w eksporcie.
POMIJANE_ROZSZERZENIA = {'.tmp', '.bak'}

# Dodatkowe foldery/pliki do pominięcia (ścieżki WZGLĘDEM workspace)
POMIJANE_SCIEZKI = {FOLDER_EXPORTU_NAZWA}

# Dodatkowe nazwy folderów do pominięcia (niezależnie od lokalizacji)
POMIJANE_NAZWY_FOLDEROW = {'__pycache__'}

# Lista dodatkowych plików do dołączenia do eksportu (ścieżki względne do workspace)
DODATKOWE_PLIKI = [
    'platformio.ini',
]

# --- Koniec Konfiguracji ---

def get_directory_tree(root_path, prefix=''):
    """
    Rekurencyjnie buduje listę linii tekstu reprezentujących drzewo katalogów
    """
    lines = []
    try:
        entries = sorted(os.listdir(root_path))
    except OSError:
        return lines
    for index, entry in enumerate(entries):
        path = os.path.join(root_path, entry)
        connector = '├── ' if index < len(entries) - 1 else '└── '
        lines.append(f"{prefix}{connector}{entry}")
        if os.path.isdir(path):
            extension = '│   ' if index < len(entries) - 1 else '    '
            lines.extend(get_directory_tree(path, prefix + extension))
    return lines


def eksportuj_kod_do_pliku(workspace_root, src_relative, export_dir_name,
                          export_filename, excluded_extensions, excluded_paths,
                          additional_files, pomijane_nazwy_folderow):
    """
    Przechodzi przez pliki w folderze źródłowym (względnym do workspace),
    łączy ich treść do jednego pliku tekstowego w folderze eksportu,
    pomijając podane rozszerzenia i ścieżki.
    Dodaje na początku drzewo katalogów źródłowych oraz pliki dodatkowe na końcu.
    """
    licznik_przetworzonych = 0
    licznik_pominietych_rozszerzenie = 0
    licznik_pominietych_sciezka = 0
    licznik_pominietych_folder = 0  # Nowy licznik dla pominiętych folderów
    licznik_bledow_odczytu = 0

    abs_src_path = os.path.abspath(os.path.join(workspace_root, src_relative))
    abs_export_dir_path = os.path.join(workspace_root, export_dir_name)
    abs_export_file_path = os.path.join(abs_export_dir_path, export_filename)

    excluded_extensions_lower = {ext.lower() for ext in excluded_extensions}
    excluded_abs_paths = {os.path.abspath(os.path.join(workspace_root, p)) for p in excluded_paths}

    # Sprawdzenie istnienia katalogu źródłowego
    if not os.path.isdir(abs_src_path):
        print(f"BŁĄD: Folder źródłowy '{abs_src_path}' nie istnieje lub nie jest folderem.")
        return

    os.makedirs(abs_export_dir_path, exist_ok=True)

    try:
        with io.open(abs_export_file_path, 'w', encoding='utf-8') as outfile:
            # --- DRZEWO KATALOGÓW ---
            outfile.write(f"# --- DRZEWO KATALOGÓW ({abs_src_path}) ---\n")
            tree_lines = get_directory_tree(abs_src_path)
            for line in tree_lines:
                outfile.write(f"# {line}\n")
            outfile.write("#\n")

            # --- POCZĄTEK EKSPORTU ---
            outfile.write(f"# --- POCZĄTEK EKSPORTU KODU ---\n")
            outfile.write(f"# Źródło: {abs_src_path}\n")
            outfile.write(f"# Pominięte rozszerzenia: {', '.join(excluded_extensions_lower)}\n")
            outfile.write(f"# Pominięte ścieżki: {', '.join(excluded_paths)}\n")
            outfile.write(f"# Pominięte foldery: {', '.join(pomijane_nazwy_folderow)}\n")
            outfile.write("#\n")

            # Przetwarzanie plików ze źródła
            for root, dirs, files in os.walk(abs_src_path, topdown=True):
                # Pomijanie katalogów po nazwie
                for folder in list(dirs):  # Iterujemy po kopii listy
                    if folder in pomijane_nazwy_folderow:
                        dirs.remove(folder)  # Usuwamy z oryginalnej listy
                        licznik_pominietych_folder += 1  # Zliczamy pominięty folder

                # Pomijanie katalogów po ścieżce
                dirs[:] = [d for d in dirs
                           if not any(
                               os.path.abspath(os.path.join(root, d)) == p or
                               os.path.abspath(os.path.join(root, d)).startswith(p + os.sep)
                               for p in excluded_abs_paths
                           )]

                for filename in files:
                    source_file_path = os.path.join(root, filename)
                    relative_file_path = os.path.relpath(source_file_path, workspace_root)

                    # Pomijanie plików wg ścieżek
                    if any(
                        source_file_path == p or source_file_path.startswith(p + os.sep)
                        for p in excluded_abs_paths
                    ):
                        licznik_pominietych_sciezka += 1
                        continue

                    # Pomijanie wg rozszerzeń
                    _, extension = os.path.splitext(filename)
                    if extension.lower() in excluded_extensions_lower:
                        licznik_pominietych_rozszerzenie += 1
                        continue

                    # Odczyt i zapis zawartości
                    try:
                        outfile.write(f"\n{'=' * 40}\n")
                        outfile.write(f"=== Plik: {relative_file_path}\n")
                        outfile.write(f"{'=' * 40}\n\n")
                        with io.open(source_file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                            outfile.write(infile.read())
                        outfile.write("\n")
                        licznik_przetworzonych += 1
                    except Exception as e:
                        outfile.write(f"\n--- BŁĄD ODCZYTU PLIKU: {relative_file_path} ({e}) ---\n")
                        licznik_bledow_odczytu += 1

            # --- DODATKOWE PLIKI ---
            outfile.write("\n# --- DODATKOWE PLIKI ---\n")
            for rel_path in additional_files:
                abs_path = os.path.abspath(os.path.join(workspace_root, rel_path))
                if not os.path.isfile(abs_path):
                    print(f"BŁĄD: Plik dodatkowy '{rel_path}' nie istnieje.")
                    continue
                try:
                    outfile.write(f"\n{'=' * 40}\n")
                    outfile.write(f"=== Plik dodatkowy: {rel_path}\n")
                    outfile.write(f"{'=' * 40}\n\n")
                    with io.open(abs_path, 'r', encoding='utf-8', errors='ignore') as infile:
                        outfile.write(infile.read())
                    outfile.write("\n")
                    licznik_przetworzonych += 1
                except Exception as e:
                    print(f"BŁĄD podczas odczytu pliku dodatkowego {rel_path}: {e}")
                    outfile.write(f"\n--- BŁĄD ODCZYTU PLIKU DODATKOWEGO: {rel_path} ({e}) ---\n")
                    licznik_bledow_odczytu += 1

            outfile.write(f"\n# --- KONIEC EKSPORTU KODU ---\n")

    except IOError as e:
        print(f"BŁĄD: Nie można zapisać do pliku wynikowego '{abs_export_file_path}': {e}")
        return

    # Podsumowanie w konsoli
    print("\n--- Podsumowanie ---")
    print(f"🔍 Przetworzono i dodano do pliku: {licznik_przetworzonych}")
    print(f"⏩ Pominięto plików (rozszerzenie): {licznik_pominietych_rozszerzenie}")
    print(f"⏩ Pominięto plików/folderów (ścieżka): {licznik_pominietych_sciezka}")
    print(f"📂 Pominięto folderów (nazwa): {licznik_pominietych_folder}")  # Nowa linia podsumowania
    print(f"❌ Wystąpiło błędów odczytu plików: {licznik_bledow_odczytu}")
    print(f"✅ Wynik zapisano w: {abs_export_file_path}")


if __name__ == '__main__':
    print("--- Rozpoczęcie eksportu kodu do pliku ---")
    workspace_sciezka = os.getcwd()
    print(f"Wykryty folder Workspace: {workspace_sciezka}")
    eksportuj_kod_do_pliku(
        workspace_root=workspace_sciezka,
        src_relative=FOLDER_ZRODLOWY_RELATYWNY,
        export_dir_name=FOLDER_EXPORTU_NAZWA,
        export_filename=PLIK_EXPORTU_NAZWA,
        excluded_extensions=POMIJANE_ROZSZERZENIA,
        excluded_paths=POMIJANE_SCIEZKI,
        additional_files=DODATKOWE_PLIKI,
        pomijane_nazwy_folderow=POMIJANE_NAZWY_FOLDEROW
    )
    print("\n--- Eksport zakończony ---")
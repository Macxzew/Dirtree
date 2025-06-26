from pathlib import Path

def save_tree_to_file(folder, save_path):
    # Affiche l'arborescence et écrit dans le fichier
    print("")
    print(f"Folder structure: {folder}")
    print("")
    with open(save_path, 'w', encoding='utf-8') as file:
        file.write(f"Folder structure: {folder}\n")
        file.write("\n\n")
        _write_tree(folder, output_file=file)
    print("")
    print(f"The folder tree has been saved to: {save_path}")

def _write_tree(folder, indentation='', is_last=False, output_file=None):
    # Fonction récursive interne pour parcourir les dossiers
    folder_path = Path(folder)
    marker = '└─' if is_last else '├─'
    line = f"{indentation}{marker} {folder_path.name}"
    if folder_path.is_dir():
        line += '/'
    print(line)
    if output_file:
        output_file.write(f"{line}\n")
    if folder_path.is_dir():
        files = list(folder_path.iterdir())
        num_files = len(files)
        for i, path in enumerate(files):
            new_is_last = (i == num_files - 1)
            prefix = '│   ' if not is_last else '    '
            _write_tree(path, indentation + prefix, new_is_last, output_file)

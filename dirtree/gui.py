from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtGui import QIcon
import sys
from pathlib import Path

def prompt_folder_and_save_path():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("src/icon.ico"))

    # Sélection dossier
    folder = QFileDialog.getExistingDirectory(
        None,
        "Dirtree - Select a folder to browse",
        "",
        QFileDialog.ShowDirsOnly
    )
    if not folder:
        return None, None

    file_name = Path(folder).name
    default_name = f"{file_name} - structure.txt"

    # Sélection fichier de sauvegarde
    save_path, _ = QFileDialog.getSaveFileName(
        None,
        "Dirtree - Where do you want to save the structure file?",
        default_name,
        "Text files (*.txt)"
    )
    if not save_path:
        return folder, None

    return folder, save_path

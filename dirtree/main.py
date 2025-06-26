from dirtree.gui import prompt_folder_and_save_path
from dirtree.explorer import save_tree_to_file
from dirtree.welcome import welcome

def main():
    # Point d'entrée du programme
    welcome()
    folder, save_path = prompt_folder_and_save_path()
    if folder and save_path:
        save_tree_to_file(folder, save_path)

if __name__ == "__main__":
    main()

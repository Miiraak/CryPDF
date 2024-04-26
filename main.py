import tkinter as tk
import pypdf
from tkinter import filedialog
import os
import pyperclip
from tkinter import Toplevel


def crack_pdf(file_path, wordlist_path):
    with open(wordlist_path, 'r', encoding="utf-8") as f:
        wordlist = f.readlines()

    pdf_reader = pypdf.PdfReader(open(file_path, 'rb'))

    for word in wordlist:
        word = word.strip()
        if pdf_reader.decrypt(word):
            print(f"Mot de passe trouvé : {word}")
            show_password_window(word)
            return True

    print("Mot de passe non trouvé.")
    return False


def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = os.path.basename(file_path)
        label.config(text=file_name)
        global selected_file_path
        selected_file_path = file_path


def validate_crack():
    if selected_file_path:
        crack_pdf(selected_file_path, wordlist_path)
    else:
        print("Veuillez sélectionner un fichier.")


def copy_to_clipboard(password):
    pyperclip.copy(password)


def show_password_window(password):
    password_window = Toplevel(root)
    password_window.title("Mot de passe trouvé")
    password_window.geometry("250x100")
    password_label = tk.Label(password_window, text="Mot de passe trouvé :")
    password_label.pack(pady=5)
    password_display = tk.Entry(password_window, width=20)
    password_display.insert(0, password)
    password_display.pack(pady=5)
    copy_button = tk.Button(password_window, text="Copier dans le presse-papiers", command=lambda: copy_to_clipboard(password))
    copy_button.pack(pady=5)


root = tk.Tk()
root.title("CryPDF")
root.geometry("210x100")

browseFile_button = tk.Button(root, text="Select", command=browse_file)
browseFile_button.pack(pady=10)
browseFile_button.place(x=15, y=60)

browse_button = tk.Button(root, text="Select", command=browse_file)
browse_button.pack(pady=10)
browse_button.place(x=15, y=60)

label = tk.Label(root, text="")
label.pack()
label.place(x=30, y=30)

labelTitre = tk.Label(root, text="File name :")
labelTitre.pack()
labelTitre.place(x=10, y=5)

wordlist_path = "C:/Users/Feynlok/Desktop/Developpement/Python/PDF_Cracker/french_passwords_top20000.txt"

validate_button = tk.Button(root, text="Attack", command=validate_crack)
validate_button.pack(pady=10)
validate_button.place(x=130, y=60)

root.mainloop()

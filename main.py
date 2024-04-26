import tkinter as tk
from tkinter import filedialog
import PyPDF2
import os
import pyperclip

fileNameLabel = ""

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = os.path.basename(file_path)
        label.config(text=file_name)
        global selected_file_path
        selected_file_path = file_path

    fileNameLabel = file_name



def crack_pdf(file_path, wordlist_path):
    with open(wordlist_path, 'r', encoding="utf-8") as f:
        wordlist = f.readlines()

    pdf_reader = PyPDF2.PdfReader(open(file_path, 'rb'))

    for word in wordlist:
        word = word.strip()
        if pdf_reader.decrypt(word):
            print(f"Password find : {word}")
            show_password_window(word)
            return True

    print("Password not find.")
    return False


def validate_crack():
    if selected_file_path:
        crack_pdf(selected_file_path, wordlist_path)
    else:
        print("Please, select a file.")


def show_password_window(password):
    password_window = tk.Toplevel(root)
    password_window.title("Done !")
    password_window.geometry("250x100")
    password_label = tk.Label(password_window, text=f"Password is :" + fileNameLabel)
    password_label.pack(pady=5)
    password_display = tk.Label(password_window, text=password, width=20, relief="sunken")
    password_display.pack(pady=5)
    copy_button = tk.Button(password_window, text="Copy", command=lambda: copy_to_clipboard(password))
    copy_button.pack(pady=5)


def copy_to_clipboard(password):
    pyperclip.copy(password)


# Créer la fenêtre principale
root = tk.Tk()
root.title("CryPDF")
root.geometry("220x100")

# Créer un bouton pour parcourir les fichiers
browse_button = tk.Button(root, text="Select", command=browse_file)
browse_button.pack(pady=10)
browse_button.place(x=15, y=60)

# Créer une étiquette pour afficher le nom du fichier sélectionné
label = tk.Label(root, text="")
label.pack()
label.place(x=30, y=30)

labelTitre = tk.Label(root, text="File name :")
labelTitre.pack()
labelTitre.place(x=10, y=5)

# Emplacement du fichier de la liste de mots de passe
wordlist_path = os.path.abspath("french_passwords_top20000.txt")

# Créer un bouton pour valider le crack manuellement
validate_button = tk.Button(root, text="Brut-Force", command=validate_crack)
validate_button.pack(pady=10)
validate_button.place(x=130, y=60)

# Lancer la boucle principale
root.mainloop()

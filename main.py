import tkinter as tk
from tkinter import Toplevel
from tkinter import filedialog
import pypdf
import os
import pyperclip


def crack_pdf(file_path, wordlist_path):
    with open(wordlist_path, 'r', encoding="utf-8") as f:
        wordlist = f.readlines()

    pdf_reader = pypdf.PdfReader(open(file_path, 'rb'))

    for word in wordlist:
        word = word.strip()
        try:
            if pdf_reader.decrypt(word):
                show_password_window(word)
                return True
        except NotImplementedError:
            continue

    print("Password not found.")
    return False


def browse_pdf_file():
    global selected_pdf_path
    selected_pdf_path = filedialog.askopenfilename(filetypes=[("PDF File", "*.pdf")])
    global pdfName

    if selected_pdf_path:
        file_nameP = os.path.basename(selected_pdf_path)
        labelChoiceFile.delete(0, tk.END)
        labelChoiceFile.insert(0, file_nameP)
        global selected_wordlist_path
        selected_wordlist_path = ""
        pdfName = file_nameP


def browse_dictionary_file():
    global selected_wordlist_path
    selected_wordlist_path = filedialog.askopenfilename(filetypes=[("Text file", "*.txt"), ("All file", "*.*")])
    if selected_wordlist_path:
        file_nameD = os.path.basename(selected_wordlist_path)
        labelChoiceDict.delete(0, tk.END)
        labelChoiceDict.insert(0, file_nameD)


def validate_crack():
    if selected_pdf_path:
        if selected_wordlist_path:
            crack_pdf(selected_pdf_path, selected_wordlist_path)
        else:
            print("Please select a dictionary file.")
    else:
        print("Please select a PDF file.")


def copy_to_clipboard(password):
    pyperclip.copy(password)


def show_password_window(password):
    password_window = Toplevel(root)
    password_window.title("Done !")
    password_window.geometry("250x100")
    password_window.resizable(height=False, width=False)
    password_label = tk.Label(password_window, text=f"Password Found for : {pdfName}")
    password_label.pack(pady=5)
    password_display = tk.Entry(password_window, width=20)
    password_display.insert(0, password)
    password_display.pack(pady=5)
    copy_button = tk.Button(password_window, text="Copy", command=lambda: copy_to_clipboard(password))
    copy_button.pack(pady=5)


root = tk.Tk()
root.title("CryPDF")
root.geometry("230x180")
root.resizable(height=False, width=False)

browseFile_button = tk.Button(root, text="PDF", command=browse_pdf_file)
browseFile_button.pack(pady=10)
browseFile_button.place(x=10, y=135)

browseDictionary_button = tk.Button(root, text="Dictionary", command=browse_dictionary_file)
browseDictionary_button.pack(pady=10)
browseDictionary_button.place(x=75, y=135)

attack_button = tk.Button(root, text=" Attack", command=validate_crack)
attack_button.pack(pady=10)
attack_button.place(x=170, y=135)

labelFile = tk.Label(root, text="PDF :")
labelFile.pack()
labelFile.place(x=10, y=10)
labelChoiceFile = tk.Entry(root, width=34)
labelChoiceFile.pack()
labelChoiceFile.place(x=10, y=35)

labelDictionary = tk.Label(root, text="Dictionary :")
labelDictionary.pack()
labelDictionary.place(x=10, y=70)
labelChoiceDict = tk.Entry(root, width=34)
labelChoiceDict.pack()
labelChoiceDict.place(x=10, y=95)

root.mainloop()

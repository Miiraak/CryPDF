# CryPDF: 
Dictionary Attack on Locked PDFs

---

**CryPDF** is a simple yet powerful tool designed to help unlock password-protected PDF files using a dictionary attack. With its user-friendly graphical interface, you can quickly test passwords from a predefined or custom dictionary.

![Screenshot of the interface](https://github.com/Miiraak/CryPDF/blob/master/Images/img.png)

## Features

- **Simple Graphical Interface**: Easily select your PDF files and dictionaries via an intuitive interface.
- **Dictionary Attack**: Test passwords from dictionary files to unlock your PDFs.
- **Multithreading Support**: Use multiple threads to speed up the dictionary attack.
- **Result Window**: Displays the found password in a separate window with a one-click copy option.

![Screenshot of the result window](https://github.com/Miiraak/CryPDF/blob/master/Images/imgDone.png)

## Installation

To use CryPDF, ensure Python is installed on your system.  
Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Miiraak/CryPDF.git
cd CryPDF
pip install -r requirements.txt
```
or

Download the executable from [Releases](https://github.com/Miiraak/CryPDF/releases)

## Usage
#### Run the Application:
Execute the main script to open the graphical interface. <br>
```bash
python crypdf.py
```
or
```
Run the executable.
```

#### Choose a PDF:
Click the PDF button to select the PDF file you want to unlock. (required)

#### Choose a Dictionary:
Click the Dictionary button to select the file containing the passwords to test. (optional)

#### Start the Attack:
Click the Attack button to start the dictionary attack. If the password is found, it will be displayed in a new window with the option to copy.

## Contribute:
Contributions are welcome! To propose improvements or report bugs, please open an issue or submit a pull request on the GitHub repository.

---

# Disclaimer
Although it's "harmless," forcing PDFs that don't belong to you is still illegal!
### _I cannot be held responsible for your actions, guys_

---

## License:
This software is provided under the [MIT](https://github.com/Miiraak/CryPDF/blob/master/LICENSE) license.

## :sparkling_heart: Thanks to:

Dictionaries:

- [Richelieu - Tarraschk](https://github.com/tarraschk/richelieu) - [(CC BY 4.0 license)](https://creativecommons.org/licenses/by/4.0/)
- [CrackStation's Password Cracking Dictionary](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm) - [(CC BY SA 3.0 license)](https://creativecommons.org/licenses/by-sa/3.0/deed.en)
- [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords) - [(MIT License)](https://github.com/danielmiessler/SecLists/blob/master/LICENSE)


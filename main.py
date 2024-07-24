import tkinter as tk
from tkinter import Toplevel
from tkinter import filedialog
import pypdf
import os
import pyperclip
import threading


def crack_pdf(file_path, wordlist_path):
    pdf_reader = pypdf.PdfReader(open(file_path, 'rb'))

    if not labelChoiceDict.get() == "":
        with open(wordlist_path, 'r', encoding="utf-8") as f:
            wordlist = f.readlines()
    else:
        wordlist = wordlist_path

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


def DictionaryThreading(dictionnary):
    ThreadNumber = len(dictionnary) / 1000
    round_up(ThreadNumber)
    
    if ThreadNumber > 20:
        ThreadNumber = 20
        
    for i in range(ThreadNumber - 1):
        t = threading.Thread(target=crack_pdf, args=(selected_pdf_path, dictionnary[i*1000:(i+1)*1000]))
        
        
        


def round_up(number): 
    return int(number) + (number % 1 > 0)
    

def browse_pdf_file():
    global selected_pdf_path
    selected_pdf_path = filedialog.askopenfilename(filetypes=[("PDF File", "*.pdf")])
    global pdfName

    if selected_pdf_path:
        file_nameP = os.path.basename(selected_pdf_path)
        labelChoiceFile.delete(0, tk.END)
        labelChoiceFile.insert(0, file_nameP)
        pdfName = file_nameP


def browse_dictionary_file():
    global selected_wordlist_path
    selected_wordlist_path = filedialog.askopenfilename(filetypes=[("Text file", "*.txt"), ("All file", "*.*")])

    if selected_wordlist_path:
        file_nameD = os.path.basename(selected_wordlist_path)
        labelChoiceDict.delete(0, tk.END)
        labelChoiceDict.insert(0, file_nameD)
    else:
        print("Verify Dictionary.")


def validate_crack():
    if labelChoiceFile.get() != "" and labelChoiceDict.get() != "":
        crack_pdf(selected_pdf_path, selected_wordlist_path)
    elif labelChoiceFile.get() != "" and labelChoiceDict.get() == "":
        crack_pdf(selected_pdf_path, integratedPasswords)
    else:
        print("Verify the PDF file.")


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
integratedPasswords = [
    "123456", "qwertyuiop", "password", "12345678", "12345", "qwerty", "trustno1", "123456789", "jordan", "12345",
    "1234", "computer", "111111", "michelle", "1234567", "111111", "dragon", "superman", "123123", "iloveyou", "baseball", "123123", "abc123", "pass",
    "football", "696969", "monkey", "shadow", "letmein", "password1", "696969", "123456789", "shadow", "master", "merlin", "666666",
    "qwertyuiop", "qwertyuiop", "123321", "123321", "mustang", "michael", "1234567890", "654321", "654321", "pussy", "pussy", "superman",
    "superman", "1qaz2wsx", "1qaz2wsx", "7777777", "7777777", "fuckyou", "fuckyou", "121212", "121212", "000000", "000000", "qazwsx", "qazwsx",
    "123qwe", "123qwe", "killer", "killer", "trustno1", "trustno1", "jordan", "jordan", "jennifer", "jennifer", "zxcvbnm", "zxcvbnm",
    "asdfgh", "asdfgh", "hunter", "hunter", "buster", "buster", "soccer", "soccer", "harley", "harley", "batman", "batman", "andrew", "andrew",
    "tigger", "tigger", "sunshine", "sunshine", "iloveyou", "iloveyou", "fuckme", "fuckme", "2000", "2000", "charlie", "charlie", "robert",
    "robert", "thomas", "thomas", "hockey", "hockey", "ranger", "ranger", "daniel", "daniel", "starwars", "starwars", "klaster", "klaster",
    "112233", "112233", "george", "george", "asshole", "asshole", "computer", "computer", "michelle", "michelle", "jessica", "jessica",
    "pepper", "pepper", "1111", "1111", "zxcvbn", "zxcvbn", "555555", "555555", "11111111", "11111111", "131313", "131313", "freedom",
    "freedom", "777777", "777777", "pass", "pass", "fuck", "fuck", "maggie", "maggie", "159753", "159753", "aaaaaa", "aaaaaa", "ginger",
    "ginger", "princess", "princess", "joshua", "joshua", "cheese", "cheese", "amanda", "amanda", "summer", "summer", "love", "love",
    "ashley", "ashley", "6969", "6969", "nicole", "nicole", "chelsea", "chelsea", "biteme", "biteme", "matthew", "matthew", "access",
    "access", "yankees", "yankees", "987654321", "987654321", "dallas", "dallas", "austin", "austin", "thunder", "thunder", "taylor",
    "taylor", "matrix", "matrix", "william", "william", "corvette", "corvette", "hello", "hello", "martin", "martin", "heather",
    "heather", "secret", "secret", "fucker", "fucker", "merlin", "merlin", "diamond", "diamond", "1234qwer", "1234qwer", "gfhjkm",
    "gfhjkm", "hammer", "hammer", "silver", "silver", "222222", "222222", "88888888", "88888888", "anthony", "anthony", "justin",
    "justin", "test", "test", "bailey", "bailey", "q1w2e3r4t5", "q1w2e3r4t5", "patrick", "patrick", "internet", "internet", "scooter",
    "scooter", "orange", "orange", "11111", "11111", "golfer", "golfer", "cookie", "cookie", "richard", "richard", "samantha", "samantha",
    "bigdog", "bigdog", "guitar", "guitar", "jackson", "jackson", "whatever", "whatever", "mickey", "mickey", "chicken", "chicken",
    "sparky", "sparky", "snoopy", "snoopy", "maverick", "maverick", "phoenix", "phoenix", "camaro", "camaro", "sexy", "sexy", "peanut",
    "peanut", "morgan", "morgan", "welcome", "welcome", "falcon", "falcon", "cowboy", "cowboy", "ferrari", "ferrari", "samsung",
    "samsung", "andrea", "andrea", "smokey", "smokey", "steelers", "steelers", "joseph", "joseph", "mercedes", "mercedes", "dakota",
    "dakota", "arsenal", "arsenal", "eagles", "eagles", "melissa", "melissa", "boomer", "boomer", "booboo", "booboo", "spider",
    "spider", "nascar", "nascar", "monster", "monster", "tigers", "tigers", "yellow", "yellow", "xxxxxx", "xxxxxx", "123123123",
    "123123123", "gateway", "gateway", "marina", "marina", "diablo", "diablo", "bulldog", "bulldog", "qwer1234", "qwer1234", "compaq",
    "compaq", "purple", "purple", "hardcore", "hardcore", "banana", "banana", "junior", "junior", "hannah", "hannah", "123654",
    "123654", "porsche", "porsche", "lakers", "lakers", "iceman", "iceman", "money", "money", "cowboys", "cowboys", "987654",
    "987654", "london", "london", "tennis", "tennis", "999999","999999", "ncc1701", "ncc1701", "coffee", "coffee", "scooby",
    "scooby", "0000", "0000", "miller", "miller", "boston", "boston", "q1w2e3r4", "q1w2e3r4", "fuckoff", "fuckoff", "brandon", "brandon",
    "yamaha", "yamaha", "chester", "chester", "mother", "mother", "forever", "forever", "johnny", "johnny", "edward", "edward",
    "333333", "333333", "oliver", "oliver", "redsox", "redsox", "player", "player", "nikita", "nikita", "knight", "knight",
    "fender", "fender", "barney", "barney", "midnight", "midnight", "please", "please", "brandy", "brandy", "chicago", "chicago",
    "badboy", "badboy", "iwantu", "iwantu", "slayer", "slayer", "rangers", "rangers", "charles", "charles", "angel", "angel",
    "flower", "flower", "bigdaddy", "bigdaddy", "rabbit", "rabbit", "wizard", "wizard", "bigdick", "bigdick", "jasper", "jasper",
    "enter", "enter", "rachel", "rachel", "chris", "chris", "steven", "steven", "winner", "winner", "adidas", "adidas", "victoria",
    "victoria", "natasha", "natasha", "1q2w3e4r", "1q2w3e4r", "jasmine", "jasmine", "winter", "winter", "prince", "prince", "panties",
    "panties", "marine", "marine", "ghbdtn", "ghbdtn", "fishing", "fishing", "cocacola", "cocacola", "casper", "casper", "james",
    "james", "232323", "232323", "raiders", "raiders", "888888", "888888", "marlboro", "marlboro", "gandalf", "gandalf", "asdfasdf",
    "asdfasdf", "crystal", "crystal", "87654321", "87654321", "12344321", "12344321", "sexsex", "sexsex", "golden", "golden",
    "blowme", "blowme", "bigtits", "bigtits", "8675309", "8675309", "panther", "panther", "lauren", "lauren", "angela", "angela",
    "bitch", "bitch", "spanky", "spanky", "thx1138", "thx1138", "angels", "angels", "madison", "madison", "winston", "winston",
    "shannon", "shannon", "mike", "mike", "toyota", "toyota", "blowjob", "blowjob", "jordan23", "jordan23", "canada", "canada",
    "sophie", "sophie", "Password", "Password", "apples", "apples", "dick", "dick", "tiger", "tiger", "razz", "razz", "123abc",
    "123abc", "pokemon", "pokemon", "qazxsw", "qazxsw", "55555", "55555", "qwaszx", "qwaszx", "muffin", "muffin", "johnson",
    "johnson", "murphy", "murphy", "cooper", "cooper", "jonathan", "jonathan", "liverpoo", "liverpoo", "david", "david", "danielle",
    "danielle", "159357", "159357", "jackie", "jackie", "1990", "1990", "123456a", "123456a", "789456", "789456", "turtle",
    "turtle", "horny", "horny", "abcd1234", "abcd1234", "scorpion", "scorpion", "qazwsxedc", "qazwsxedc", "101010", "101010",
    "butter", "butter", "carlos", "carlos", "password1", "password1", "dennis", "dennis", "slipknot", "slipknot", "qwerty123",
    "qwerty123", "booger", "booger", "asdf", "asdf", "1991", "1991", "black", "black", "startrek", "startrek", "12341234", "12341234",
    "cameron", "cameron", "newyork", "newyork", "rainbow", "rainbow", "nathan", "nathan", "john", "john", "1992", "1992", "rocket",
    "rocket", "viking", "viking", "redskins", "redskins", "butthead", "butthead", "asdfghjkl", "asdfghjkl", "1212", "1212", "sierra",
    "sierra", "peaches", "peaches", "gemini", "gemini", "doctor", "doctor", "wilson", "wilson", "sandra", "sandra", "helpme",
    "helpme", "qwertyui", "qwertyui", "victor", "victor", "florida", "florida", "dolphin", "dolphin", "pookie", "pookie", "captain",
    "captain", "tucker", "tucker", "blue", "blue", "liverpool", "liverpool", "theman", "theman", "bandit", "bandit", "dolphins",
    "dolphins", "maddog", "maddog", "packers", "packers", "jaguar", "jaguar", "lovers", "lovers", "nicholas", "nicholas", "united",
    "united", "tiffany", "tiffany", "maxwell", "maxwell", "zzzzzz", "zzzzzz", "nirvana", "nirvana", "jeremy", "jeremy", "suckit",
    "suckit", "stupid", "stupid", "porn", "porn", "monica", "monica", "elephant", "elephant", "giants", "giants", "jackass", "jackass",
    "hotdog", "hotdog", "rosebud", "rosebud", "success", "success", "debbie", "debbie", "mountain", "mountain", "444444", "444444",
    "xxxxxxxx", "xxxxxxxx", "warrior", "warrior", "1q2w3e4r5t", "1q2w3e4r5t", "q1w2e3", "q1w2e3", "123456q", "123456q", "albert",
    "albert", "metallic", "metallic", "lucky", "lucky", "azerty", "azerty", "7777", "7777", "shithead", "shithead", "alex", "alex",
    "bond007", "bond007", "alexis", "alexis", "1111111", "1111111", "samson", "samson", "5150", "5150", "willie", "willie", "scorpio",
    "scorpio", "bonnie", "bonnie", "gators", "gators", "benjamin", "benjamin", "voodoo", "voodoo", "driver", "driver", "dexter",
    "dexter", "2112", "2112", "jason", "jason", "calvin", "calvin", "freddy", "freddy", "212121", "212121", "creative", "creative",
    "12345a", "12345a", "sydney", "sydney", "rush2112", "rush2112", "1989", "1989", "asdfghjk", "asdfghjk", "red123", "red123",
    "bubba", "bubba", "4815162342", "4815162342", "passw0rd", "passw0rd", "trouble", "trouble", "gunner", "gunner", "happy",
    "happy", "fucking", "fucking", "gordon", "gordon", "legend", "legend", "jessie", "jessie", "stella", "stella", "qwert",
    "qwert", "eminem", "eminem", "arthur", "arthur", "apple", "apple", "nissan", "nissan", "bullshit", "bullshit", "bear", "bear",
    "america", "america", "1qazxsw2", "1qazxsw2", "nothing", "nothing", "parker", "parker", "4444", "4444", "rebecca", "123456", "123456789", "azerty", "1234561", "qwerty", "marseille",
    "000000", "1234567891", "doudou", "12345", "loulou", "123", "password", "azertyuiop", "12345678", "soleil", "chouchou", "1234", "1234567",
    "123123", "123451", "bonjour", "111111", "nicolas", "jetaime", "coucou", "motdepasse", "Status", "julien", "thomas", "camille",
    "010203", "chocolat", "iloveyou", "iloveyou1", "portugal", "1234567890", "alexandre", "654321", "maxime", "00000", "wxcvbn", "oceane", "pompier",
    "12345671", "marine", "0000", "maison", "isabelle", "celine", "sandrine", "pierre", "caroline", "elodie", "olivier", "mohamed", "romain", "badoo",
    "football", "princesse", "nathalie", "boubou", "vincent", "anthony", "aurelie", "caramel", "dragon", "sophie", "amour", "papillon", "antoine",
    "louloute", "0123456789", "sebastien", "audrey", "666666", "emilie", "naruto", "france", "987654321", "voiture", "789456", "amandine",
    "pauline", "laurent", "stephane", "melanie", "vanille", "benjamin", "chipie", "valentin", "159753", "morgane", "marion", "sabrina", "michel",
    "aaaaaa", "mar", "cheval", "samsung", "102030", "123654", "charlotte", "algerie", "jerome", "alexis", "121212", "junior", "scorpion",
    "toulouse", "secret", "lolita", "melissa", "clement", "123456781", "frederic", "nounours", "poisson", "vanessa", "quentin", "summer.fruit",
    "sandra", "jordan", "virginie", "guillaume", "salope", "patrick", "jessica", "azerty123", "Telechargement", "mamour", "aze", "justine",
    "philippe", "marie", "mathieu", "daniel", "jonathan", "maman", "laetitia", "florian", "jeremy", "tintin", "cedric", "qwertyuiop",
    "azerty1", "etoile", "zidane", "pascal", "NULL", "startfinding", "112233", "juliette", "nounou", "moimoi", "mathilde", "222222",
    "damien", "password1", "christophe", "stephanie", "nathan", "12345678901", "valerie", "fatima", "arthur", "choupette", "qwerty123",
    "amours", "dauphin", "orange", "6543211", "snoopy", "delphine", "monamour", "aqwzsx", "jennifer", "555555", "prince", "claire", "147852",
    "marina", "patricia", "zouzou", "florence", "789456123", "bhf", "bordeaux", "mercedes", "francois", "1q2w3e4r5t", "123321", "ronaldo",
    "internet", "dominique", "martine", "abc123", "pepette", "samuel", "franck", "adrien", "sylvie", "scarface", "YAgjecc826", "bou",
    "alexandra", "noisette", "1111111", "arnaud", "0123456", "police", "christian", "musique", "cecile", "amelie", "caline", "amoure",
    "987654", "superman", "michael", "nicole", "ludovic", "emmanuel", "tigrou", "minette", "7777777", "thierry", "147258", "helene",
    "catherine", "mathis", "00000000", "chaton", "carole", "benoit", "gabriel", "101010", "lovely1", "aurore", "AZERTY", "pupuce",
    "laurence", "moncoeur", "1qaz2wsx", "777777", "mickael", "fabrice", "estelle", "megane", "christine", "abcdef", "ordinateur", "lovely",
    "famille", "monaco", "hunter1", "louise", "alicia", "rencontre", "ferrari", "guigui", "victor", "princess", "bonheur", "pokemon",
    "matheo", "147258369", "123456a", "claude", "liberte", "18n28n24a5", "biloute", "coralie", "david", "gribouille", "william", "adeline",
    "nikita", "crevette", "calimero", "robert", "aurelien", "123654789", "999999", "banane", "didier", "azertyui", "fabien", "lorenzo",
    "bernard", "madinina", "canada", "zoosk", "basket", "severine", "christelle", "gregory", "espoir", "bonbon", "marseille13", "poussin",
    "matrix", "cricri", "victoire", "cocacola", "moimeme", "joseph", "cha", "veronique", "azertyu", "angelique", "696969", "171204jg", "poupette",
    "yamaha", "christ", "cerise", "karine", "bretagne", "martin", "roxane", "charles", "1q2w3e4r", "tunisie", "reglisse", "sylvain", "ulysse",
    "nenette", "forever", "corentin", "maurice", "chance", "9876543211", "chacha", "matthieu", "010101", "lol", "tonton", "baptiste", "sousou",
    "456789", "minouche", "!", "killer", "fanfan", "clemence", "malika", "princess1", "tuning", "nirvana", "jeanne", "vRbGQnS997", "xavier",
    "maxence", "master", "yasmine", "qwerty1", "matteo", "samira", "andrea", "brigitte", "131313", "raphael", "casablanca", "yannick",
    "richard", "grenouille", "secret1", "charly", "noemie", "333333", "italia", "titeuf", "123123123", "romane", "patate", "123soleil",
    "1111", "florent", "888888", "olivia", "nadine", "victoria", "morgan", "barcelone", "bandit", "bl8LYGB0", "moussa", "lovers1", "julie",
    "margot", "charlie", "bibiche", "chantal", "senegal", "capucine", "tennis", "monique", "azert", "souris", "corsica", "fuckyou",
    "welcome", "bisous", "zxcvbnm", "0000000000", "qazwsx", "reunion", "margaux", "francis", "bastien", "mimine", "sarah", "lolo", "shadow",
    "tortue", "naruto1", "chanel", "starwars", "beatrice", "steven", "ludivine", "angel", "moumoune", "gaelle", "dou", "tequila", "eminem",
    "handball", "peugeot", "lionel", "ophelie", "corinne", "titine", "espagne", "mon", "guitare", "friends", "159357", "0000001", "kawasaki",
    "michelle", "marcel", "lou", "tristan", "q1w2e3r4t5y6", "stella", "montana", "carine", "domino", "mickey", "mamadou", "sniper", "travail",
    "lolotte", "pirate", "youyou", "titi", "hiphop", "angel1", "147852369", "valentine", "boulette", "samantha", "doudoune", "jacques", "cambiami",
    "gilles", "batman", "poupoune", "lilou", "bambou", "kevin", "jesus", "dimitri", "didine", "456123", "tomtom", "TMM", "patrice", "cassandra",
    "toutou", "alexia", "mariam", "manon", "11111111", "01234567891", "floflo", "portable", "metallica", "lacoste", "lyonnais", "slipknot",
    "juventus", "rachel", "suzuki", "car", "canelle", "nadege", "qwe123", "loveyou", "sabine", "11111", "oliver", "praline", "fondoom",
    "napoleon", "mustang", "sofiane", "natacha", "janvier", "magali", "michael1", "moi", "killian", "aminata", "444444", "carpediem",
    "55555", "vacances", "esteban", "laura", "forever1", "paris", "fsd9shtyut", "angelina", "pioupiou", "tresor", "iloveu1", "amoureuse",
    "amoureux", "88888888", "741852963", "mam", "123qwe", "love", "123789", "mylene", "freedom", "L58jkdjP!m", "pistache", "lololo", "212121",
    "1234qwer", "6hBf28W791", "lucas", "010", "fripouille", "50cent", "poulette", "seigneur", "tulipe", "ramses", "emeline", "mahalkita1",
    "fabienne", "sweety", "picasso", "poiuytreza", "lapinou", "monange", "myriam", "lovers", "axelle", "toietmoi", "a123456", "yassine",
    "winnie", "000", "pepito", "cachou", "adidas", "mimi", "232323", "qsdfghjklm", "poiuyt", "1231231", "1111111111", "stargate", "playboy",
    "agathe", "jet", "toto", "qwer1234", "gerard", "spiderman", "mat", "blabla", "marlboro", "aqwzsxedc", "angelo", "joshua", "pompiers",
    "arsenal", "monster", "clochette", "connard", "passion", "012345", "rachid", "truand", "violette", "ytreza", "fleurs", "bertrand",
    "titoune", "biscotte", "champion", "blink182", "hardcore", "johnny", "marseille1", "hotmail", "emploi", "merlin", "drogba", "zebulon",
    "asdfgh", "marmotte", "charlene", "bounty", "man", "francoise", "dom", "tamere", "georges", "123456789a", "thibault", "xxxxxx",
    "namour", "martinique", "nougat", "soprano", "nicole1", "toulouse31", "bogoss", "barbie", "mariage", "angele", "canard", "realmadrid",
    "laguna", "italie", "phoenix", "fraise", "justin", "diablo", "momo", "aaaaa", "bouboule", "youssef", "mozart", "claudine", "marius",
    "mathias", "sasuke", "dorian", "paradis", "mireille", "merde", "kylian", "danielle", "bon", "ricard", "cookie", "6666661", "laurie",
    "albert", "alex", "nbvcxw", "kimbum1", "12301230", "gaetan", "tatiana", "tmm", "deborah", "cannabis", "montagne", "marjorie", "renault",
    "enfants", "vegeta", "manuel", "karima", "cannelle", "pompom", "kiki", "lulu", "clarisse", "sam", "pretty1", "ouioui", "252525", "9876543210",
    "sunshine", "angela", "myspace1", "monkey", "yuantuo2012", "melodie", "mapuce", "0987654321", "sangoku", "ducati", "142536", "linkedin",
    "marley", "juillet", "sakura", "carlos", "aaaa", "maelys", "novembre", "roucky", "melina", "badboy", "parissg", "salome", "abcd1234", "iloveu",
    "compaq", "denise", "marguerite", "mou", "pascale", "pamela", "etienne", "chatte", "london", "200", "3rJs1la7qE", "jesus1", "fra",
    "123abc", "nantes", "yacine", "cou", "cloclo", "gaston", "anthony1", "mahalko1", "cocotte", "simone", "chris", "loveme", "guadeloupe",
    "asdfghjkl", "pitchoune", "mamans", "couscous", "toutoune", "pikachu", "leslie", "qdujvyG5sxa", "pauleta", "choupinette", "maelle", "coco",
    "tahiti", "celibataire", "poupou", "madeleine", "151515", "charline", "soleil13", "philou", "marianne", "emmanuelle", "camion", "bobmarley",
    "cho", "ben", "741852", "diabolo", "barbara", "friendster1", "socrate", "0000000", "fairways", "nelson", "joshua1", "poulet", "octobre",
    "elephant", "198", "raymond", "christian1", "balance", "solene", "azer", "roland", "looping", "liverpool", "aze123", "4567891",
    "popeye", "rebecca", "syl", "porsche", "mylove", "bateau", "cheyenne", "solange", "maganda1", "junpyo1", "9876541", "prisca", "verseau",
    "bianca", "bamako", "alain", "7894561", "11111111111", "salut", "laurine", "freddy", "panget1", "nutella", "5236", "johanna", "honey1",
    "clementine", "chelsea", "rammstein", "marvin", "jasmine", "cherie", "butterfly", "tarzan", "subaru", "flower", "azerty12", "7894561231",
    "124578", "renard", "kirikou", "fatoumata", "ang", "papa", "michou", "bestfriend1", "angels", "Eh1K9oh335", "143441", "111", "nanou",
    "athena", "anissa", "anais", "cameroun", "pommes", "evelyne", "ballon", "monbebe", "carotte", "100", "madrid", "bigboss", "moustique",
    "motocross", "san", "mamama", "decembre", "septembre", "josephine", "popopo", "cancer", "ashley", "jul", "harley", "zezette", "geronimo",
    "loveyou1", "clara", "141414", "sayang1", "papounet", "joelle", "trustno1", "titou", "1122331", "titanic", "barcelona", "amitie",
    "bruno", "amo", "blanche", "246810", "sexe", "computer", "renaud", "fuckyou1", "gabrielle", "sweety1", "cynthia", "qsdfgh", "tigresse",
    "bebe", "fred", "antonio", "hunter", "lamine", "khadija", "garfield", "007007", "pierrot", "lumiere", "louloutte", "diamant", "cecilia",
    "bisounours", "xbox360", "pourquoi", "superman1", "geraldine", "ale", "papamaman", "sesame", "null", "avenir", "tanguy", "sal", "sultan",
    "1212121", "lovelove", "hornet", "friends1", "reussite", "miguel", "mourad", "mmmmmm", "benfica", "q1w2e3r4t5", "roxanne", "lilian",
    "info", "frimousse", "asterix", "12341234", "viviane", "onepiece", "lil", "suzanne", "hello", "bidule", "pretty", "flo", "magalie", "jojo",
    "afrique", "pou", "melody", "mathys", "alison", "mel", "securite", "jordan23", "silver", "demo", "vincent1", "lili", "paris75", "michele",
    "guizmo", "toyota", "jupiter", "cochon", "gwada971", "enfant", "8888881", "120", "muriel", "202020", "penelope", "diesel", "181818",
    "newyork", "josiane", "logitech", "magic", "elisabeth", "coline", "canabis", "abcdefg", "789", "09876543211", "joseph1", "gilbert",
    "000001", "madonna", "chloe", "rosalie", "pollux", "pap", "amanda", "jessie", "1q2w3e", "toulouse1", "99999", "solene", "ocean", "kenji",
    "boston", "bambi", "coincoin", "ken", "concorde", "minou", "perso", "magic", "abigail", "maeva", "saucisson", "teddy", "asdfgh1", "monchou",
    "azert1", "abcd", "frank", "alexandra1", "babouche", "lilou", "aymeric", "aimer", "dragonball", "imene", "penis", "justine1", "azerty0",
    "douleur", "charly1", "rever", "skyrock", "isabella", "conan", "didier1", "morgane1", "purple", "demain", "savannah", "hector",
    "catalina", "babylove", "britney", "tomate", "nikos", "bambina", "skynet", "mangue", "triton", "revolte", "sexyboy", "connasse", "rap",
    "cyril", "cyber", "dominic", "copine", "sandy", "boucle", "raphael1", "camille1", "butterfly1", "sergio", "2000", "romeo", "caroline1",
    "ma", "marine1", "mazda", "wilson", "sacha", "minipouce", "mystere", "lucie", "polux", "petite", "olivier1", "pokemon1", "emmanuelle1",
    "tatan", "123poil", "gothic", "familia", "fortune", "made", "pol", "auto", "morgane123", "banzai", "amour1", "brandon", "smiley",
    "freeman", "blaise", "serrure", "lololo1", "micro", "sylvain1", "martini", "maison1", "ninou", "treize", "bribri", "maud", "pulsar",
    "1990", "cleo", "pouvoir", "bernard1", "marocaine", "tonton1", "bambou1", "horizon", "victor1", "emma", "free", "tomate1", "calamar",
    "century", "boris", "sylvia", "rencontres", "rania", "pablo", "2005", "twilight", "clem", "chocolat1", "djibril", "marjolaine", "2004",
    "gogo", "jane", "love1", "loulou1", "lion", "goldorak", "poireau", "baby", "chou", "patrick1", "seb", "reno", "cougar", "pingpong",
    "aime", "azazaz", "frederic1", "pascal1", "yaya", "mikado", "serge", "brahima", "mic", "flower1", "celine1", "star", "priscilla", "lol1",
    "marcel1", "je", "darth", "paul", "hello1", "marchand", "bob", "super", "moumou", "dure", "gino", "nathalie1", "benoit1", "satan", "jenifer",
    "elise", "louis", "chanel1", "flower13", "hamza", "suisse", "emile", "lana", "aster", "iop", "dylan", "baron", "melodie1", "kikou",
    "peche", "shadow1", "raf", "lapin", "33333", "vivi", "bilal", "beurk", "jiji", "olivier123", "rose", "alexis1", "mido", "yahoo", "dimitri1",
    "laetitia1", "azerty11", "pep", "vampire", "douda", "genesis", "nono", "djib", "november", "mya", "2008", "noel", "amer", "papa123", "matthieu1",
    "jesus123", "mouloud", "odile", "gaby", "lolo1", "les", "mimi1", "anto", "mik", "lancome", "cool1", "romane1", "richard1", "leo", "romain1",
    "prince1", "ibrahim", "mariama", "samer", "marinette", "hugodu13", "planet", "europe", "giovanni", "star13", "cameleon", "jojo1", "emile1",
    "roger", "roger1", "genevieve", "raptor", "cassie", "off", "space", "1992", "swimming", "dragon1", "raouf", "didi", "shadow13", "kenny",
    "maeva1", "cyrielle", "lili1", "alexandra123", "alice", "baba", "amine", "01234", "carlo", "wael", "jean", "juin", "choup", "vince",
    "golden", "france1", "prince123", "musique1", "sarah1", "panda", "maxim", "casa", "logan", "desire", "sofia", "caramel13", "plume",
    "tati", "fuck123", "al", "milan", "alban", "bib", "dan", "singer", "azerty13", "choupinou", "med", "kiki13", "bourriquet", "douda1",
    "alain1", "sarah123", "amel", "samsam", "severine1", "etoile1", "anis", "bb", "cel", "richie", "lala", "animaux", "titi13", "zouzou13",
    "impossible", "capitaine", "hugo", "free13", "houssem", "jayjay", "angeline", "gabriel1", "compte", "kilian", "helene", "brian",
    "princess", "planete", "dora", "paradis1", "soufiane", "lavie", "1981", "myriam1", "ninie", "antoine1", "crevette", "schtroumpf",
    "harry", "bidou", "emilie123", "arcenciel", "natacha1", "zzzzzz", "majid", "yahia", "mamadou1", "azert123", "gold", "prince", "socrate1",
    "192837465", "kenzo", "happiness", "fille", "rose13", "amelie1", "driss", "guigui", "ali", "angelique1", "cyborg", "karine1", "nael",
    "kool", "lool", "candy", "emma1", "0123456", "albator", "supermoi", "zazou", "sahra", "baby13", "zinedine", "hacker", "personne",
    "laurie13", "bernie", "djamel", "morad", "tony", "megane", "dorine", "elsa", "camille123", "ange", "axel", "maeva123", "marine123", "gala",
    "du13", "exemple", "3125", "poupinette", "2002", "tommy", "charly123", "goal", "onizuka", "laurie123", "marianne1", "mat123", "qqqqqq",
    "bebe13", "golum", "poisson", "maya", "bab", "stars", "lol13", "sword", "morad13", "3110", "toto1", "nick", "yassir", "bettyboop", "lina",
    "pierre123", "montreal", "hihihi", "marley1", "the", "paris1", "mohammed1", "dodo13", "mamour", "ocean13", "wolf", "mathilde1",
    "azerty1234", "rossi", "solene1", "willy", "camelia", "mathieu123", "yoan", "mathis1", "perle", "sergent", "claude1", "mama", "bonjour13",
    "arcenciel13", "1980", "securite1", "roberto", "choupinette1", "patricia1", "leon", "perle1", "renaissance", "claude123", "kamel",
    "rockstar", "12345678a", "victoire", "isabelle1", "00000001", "tango", "allo", "caterina", "daniel123", "dominique1", "anthony123", "jonathan1",
    "kaiser", "banane", "elfe", "celine123", "souris", "florence1", "1995", "amigo", "anthony13", "aaaaaaa", "mathilde123", "manuel123",
    "oh", "1998", "youyou13", "paulo", "alpha", "brice", "gohan", "ombre", "kaka", "berthelot", "nicolas1", "aubin", "computer1", "1994",
    "alfred", "snoop", "emilie1", "tigrou", "oceane123", "biloute", "farid", "natacha123", "bbbbbb", "ros", "leila", "etoile", "camille13",
    "brayan", "gaston123", "namaste", "claudine1", "vava", "tonio", "wolf13", "mohamed1", "mortelle", "amelia", "patricia123", "doudou13", "lolol",
    "sebastien1", "hardcore1", "gaston13", "1999", "pupuce13", "aurelie1", "nadia1", "mathieu13", "nikita", "bernadette", "emo", "mamadou123",
    "1960", "loool", "olivia", "123a", "amina", "merci", "yoann", "charlene1", "yvette", "tim", "amine1", "minette", "456456", "vol", "jimmy1", "nenette",
    "camelia123", "1961", "1962", "lemon", "ronaldo", "camille1234", "camelia1", "daniel13", "moussa", "moi1", "valentin123", "ohm", "omar", "tiamo",
    "perle13", "fatou", "pimousse", "caillou", "sebastien123", "192837", "dragon13", "fantasy", "mercedes", "benjamin1", "berthelot1", "pirate13",
    "tabatha", "shadow123", "eloise", "martin1", "2023", "az", "pop", "timoth", "1963", "1928374651", "lulu13", "azerty", "bapteme", "eternite", "azerty0",
    "valerie1", "coucou1", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "eternite1", "123soleil", "timothee", "lucifer", "sylvia1",
    "juillet13", "cyril1", "jiji1", "jessica1", "rose123", "oooooo", "eh", "mehdi1", "free1", "1940", "1985", "1989", "000000000", "696969", "mom",
    "maurice", "nezuko", "abig12345"]

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

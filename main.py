import tkinter as tk
from tkinter import Toplevel
from tkinter import filedialog
import pypdf
import os
import pyperclip
import threading
import math


def crack_pdf(file_path, wordlist_var):
    pdf_reader = pypdf.PdfReader(open(file_path, 'rb'))

    if not labelChoiceDict.get() == "":
        with open(wordlist_var, 'r', encoding="utf-8") as f:
            wordlist = f.readlines()
    else:
        wordlist = wordlist_var

    for word in wordlist:
        word = word.strip()
        try:
            if pdf_reader.decrypt(word):
                show_password_window(word)
                return True
        except NotImplementedError:
            continue

    show_passwordNF_window()
    return False


def ThreadingCalculator(dictionnary):
    factor = 1000
    min_thread = 1
    max_thread = 8
    
    return max(max_thread, min(min_thread, math.ceil(len(dictionnary) / factor)))


def split_list(dictionnary, num_threads):
    avg_len = len(dictionnary) // num_threads
    return [dictionnary[i * avg_len:(i + 1) * avg_len] for i in range(num_threads - 1)] + [dictionnary[(num_threads - 1) * avg_len:]]


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
    password_label = tk.Label(password_window, text=f"Password found for : {pdfName}")
    password_label.pack(pady=5)
    password_display = tk.Entry(password_window, width=20)
    password_display.insert(0, password)
    password_display.pack(pady=5)
    copy_button = tk.Button(password_window, text="Copy", command=lambda: copy_to_clipboard(password))
    copy_button.pack(pady=5)
    

def show_passwordNF_window():
    passwordNF_window = Toplevel(root)
    passwordNF_window.title("Awww...")
    passwordNF_window.geometry("250x40")
    passwordNF_window.resizable(height=False, width=False)
    passwordNF_label = tk.Label(passwordNF_window, text=f"Password not found for : {pdfName}")
    passwordNF_label.pack(pady=5)


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


integratedPasswords = [
"123456", "qwertyuiop", "password", "12345678", "12345", "qwerty", 
"trustno1", "123456789", "jordan", "1234", "computer", "111111", 
"michelle", "1234567", "dragon", "superman", "123123", "iloveyou", 
"baseball", "abc123", "pass", "football", "696969", "monkey", 
"shadow", "letmein", "password1", "master", "merlin", "666666", 
"123321", "mustang", "michael", "1234567890", "654321", "pussy", 
"1qaz2wsx", "7777777", "fuckyou", "121212", "000000", "qazwsx", 
"123qwe", "killer", "jennifer", "zxcvbnm", "asdfgh", "hunter", 
"buster", "soccer", "harley", "batman", "andrew", "tigger", 
"sunshine", "fuckme", "2000", "charlie", "robert", "thomas", 
"hockey", "ranger", "daniel", "starwars", "klaster", "112233", 
"george", "asshole", "jessica", "pepper", "1111", "zxcvbn", 
"555555", "11111111", "131313", "freedom", "777777", "fuck", 
"maggie", "159753", "aaaaaa", "ginger", "princess", "joshua", 
"cheese", "amanda", "summer", "love", "ashley", "6969", 
"nicole", "chelsea", "biteme", "matthew", "access", "yankees", 
"987654321", "dallas", "austin", "thunder", "taylor", "matrix", 
"william", "corvette", "hello", "martin", "heather", "secret", 
"fucker", "diamond", "1234qwer", "gfhjkm", "hammer", "silver", 
"222222", "88888888", "anthony", "justin", "test", "bailey", 
"q1w2e3r4t5", "patrick", "internet", "scooter", "orange", "11111", 
"golfer", "cookie", "richard", "samantha", "bigdog", "guitar", 
"jackson", "whatever", "mickey", "chicken", "sparky", "snoopy", 
"maverick", "phoenix", "camaro", "sexy", "peanut", "morgan", 
"welcome", "falcon", "cowboy", "ferrari", "samsung", "andrea", 
"smokey", "steelers", "joseph", "mercedes", "dakota", "arsenal", 
"eagles", "melissa", "boomer", "booboo", "spider", "nascar", 
"monster", "tigers", "yellow", "xxxxxx", "123123123", "gateway", 
"marina", "diablo", "bulldog", "qwer1234", "compaq", "purple", 
"hardcore", "banana", "junior", "hannah", "123654", "porsche", 
"lakers", "iceman", "money", "cowboys", "987654", "london", 
"tennis", "999999","999999", "ncc1701", "coffee", "scooby", "0000", 
"miller", "boston", "q1w2e3r4", "fuckoff", "brandon", "yamaha", 
"chester", "mother", "forever", "johnny", "edward", "333333", 
"oliver", "redsox", "player", "nikita", "knight", "fender", 
"barney", "midnight", "please", "brandy", "chicago", "badboy", 
"iwantu", "slayer", "rangers", "charles", "angel", "flower", 
"bigdaddy", "rabbit", "wizard", "bigdick", "jasper", "enter", 
"rachel", "chris", "steven", "winner", "adidas", "victoria", 
"natasha", "1q2w3e4r", "jasmine", "winter", "prince", "panties", 
"marine", "ghbdtn", "fishing", "cocacola", "casper", "james", 
"232323", "raiders", "888888", "marlboro", "gandalf", "asdfasdf", 
"crystal", "87654321", "12344321", "sexsex", "golden", "blowme", 
"bigtits", "8675309", "panther", "lauren", "angela", "bitch", 
"spanky", "thx1138", "angels", "madison", "winston", "shannon", 
"mike", "toyota", "blowjob", "jordan23", "canada", "sophie", 
"Password", "apples", "dick", "tiger", "razz", "123abc", 
"pokemon", "qazxsw", "55555", "qwaszx", "muffin", "johnson", 
"murphy", "cooper", "jonathan", "liverpoo", "david", "danielle", 
"159357", "jackie", "1990", "123456a", "789456", "turtle", 
"horny", "abcd1234", "scorpion", "qazwsxedc", "101010", "butter", 
"carlos", "dennis", "slipknot", "qwerty123", "booger", "asdf", 
"1991", "black", "startrek", "12341234", "cameron", "newyork", 
"rainbow", "nathan", "john", "1992", "rocket", "viking", 
"redskins", "butthead", "asdfghjkl", "1212", "sierra", "peaches", 
"gemini", "doctor", "wilson", "sandra", "helpme", "qwertyui", 
"victor", "florida", "dolphin", "pookie", "captain", "tucker", 
"blue", "liverpool", "theman", "bandit", "dolphins", "maddog", 
"packers", "jaguar", "lovers", "nicholas", "united", "tiffany", 
"maxwell", "zzzzzz", "nirvana", "jeremy", "suckit", "stupid", 
"porn", "monica", "elephant", "giants", "jackass", "hotdog", 
"rosebud", "success", "debbie", "mountain", "444444", "xxxxxxxx", 
"warrior", "1q2w3e4r5t", "q1w2e3", "123456q", "albert", "metallic", 
"lucky", "azerty", "7777", "shithead", "alex", "bond007", 
"alexis", "1111111", "samson", "5150", "willie", "scorpio", 
"bonnie", "gators", "benjamin", "voodoo", "driver", "dexter", 
"2112", "jason", "calvin", "freddy", "212121", "creative", 
"12345a", "sydney", "rush2112", "1989", "asdfghjk", "red123", 
"bubba", "4815162342", "passw0rd", "trouble", "gunner", "happy", 
"fucking", "gordon", "legend", "jessie", "stella", "qwert", 
"eminem", "arthur", "apple", "nissan", "bullshit", "bear", 
"america", "1qazxsw2", "nothing", "parker", "4444", "rebecca", 
"1234561", "marseille", "1234567891", "doudou", "loulou", "123", 
"azertyuiop", "soleil", "chouchou", "123451", "bonjour", "nicolas", 
"jetaime", "coucou", "motdepasse", "Status", "julien", "camille", 
"010203", "chocolat", "iloveyou1", "portugal", "alexandre", "maxime", 
"00000", "wxcvbn", "oceane", "pompier", "12345671", "maison", 
"isabelle", "celine", "sandrine", "pierre", "caroline", "elodie", 
"olivier", "mohamed", "romain", "badoo", "princesse", "nathalie", 
"boubou", "vincent", "aurelie", "caramel", "amour", "papillon", 
"antoine", "louloute", "0123456789", "sebastien", "audrey", "emilie", 
"naruto", "france", "voiture", "amandine", "pauline", "laurent", 
"stephane", "melanie", "vanille", "chipie", "valentin", "morgane", 
"marion", "sabrina", "michel", "mar", "cheval", "102030", 
"charlotte", "algerie", "jerome", "toulouse", "lolita", "clement", 
"123456781", "frederic", "nounours", "poisson", "vanessa", "quentin", 
"summer.fruit", "virginie", "guillaume", "salope", "azerty123", "Telechargement", 
"mamour", "aze", "justine", "philippe", "marie", "mathieu", 
"maman", "laetitia", "florian", "tintin", "cedric", "azerty1", 
"etoile", "zidane", "pascal", "NULL", "startfinding", "juliette", 
"nounou", "moimoi", "mathilde", "damien", "christophe", "stephanie", 
"12345678901", "valerie", "fatima", "choupette", "amours", "dauphin", 
"6543211", "delphine", "monamour", "aqwzsx", "claire", "147852", 
"patricia", "zouzou", "florence", "789456123", "bhf", "bordeaux", 
"francois", "ronaldo", "dominique", "martine", "pepette", "samuel", 
"franck", "adrien", "sylvie", "scarface", "YAgjecc826", "bou", 
"alexandra", "noisette", "arnaud", "0123456", "police", "christian", 
"musique", "cecile", "amelie", "caline", "amoure", "ludovic", 
"emmanuel", "tigrou", "minette", "thierry", "147258", "helene", 
"catherine", "mathis", "00000000", "chaton", "carole", "benoit", 
"gabriel", "lovely1", "aurore", "AZERTY", "pupuce", "laurence", 
"moncoeur", "mickael", "fabrice", "estelle", "megane", "christine", 
"abcdef", "ordinateur", "lovely", "famille", "monaco", "hunter1", 
"louise", "alicia", "rencontre", "guigui", "bonheur", "matheo", 
"147258369", "claude", "liberte", "18n28n24a5", "biloute", "coralie", 
"gribouille", "adeline", "crevette", "calimero", "aurelien", "123654789", 
"999999", "banane", "didier", "azertyui", "fabien", "lorenzo", 
"bernard", "madinina", "zoosk", "basket", "severine", "christelle", 
"gregory", "espoir", "bonbon", "marseille13", "poussin", "cricri", 
"victoire", "moimeme", "cha", "veronique", "azertyu", "angelique", 
"171204jg", "poupette", "christ", "cerise", "karine", "bretagne", 
"roxane", "tunisie", "reglisse", "sylvain", "ulysse", "nenette", 
"corentin", "maurice", "chance", "9876543211", "chacha", "matthieu", 
"010101", "lol", "tonton", "baptiste", "sousou", "456789", 
"minouche", "!", "fanfan", "clemence", "malika", "princess1", 
"tuning", "jeanne", "vRbGQnS997", "xavier", "maxence", "yasmine", 
"qwerty1", "matteo", "samira", "brigitte", "raphael", "casablanca", 
"yannick", "grenouille", "secret1", "charly", "noemie", "italia", 
"titeuf", "romane", "patate", "123soleil", "florent", "olivia", 
"nadine", "barcelone", "bl8LYGB0", "moussa", "lovers1", "julie", 
"margot", "bibiche", "chantal", "senegal", "capucine", "monique", 
"azert", "souris", "corsica", "bisous", "0000000000", "reunion", 
"margaux", "francis", "bastien", "mimine", "sarah", "lolo", 
"tortue", "naruto1", "chanel", "beatrice", "ludivine", "moumoune", 
"gaelle", "dou", "tequila", "handball", "peugeot", "lionel", 
"ophelie", "corinne", "titine", "espagne", "mon", "guitare", 
"friends", "0000001", "kawasaki", "marcel", "lou", "tristan", 
"q1w2e3r4t5y6", "montana", "carine", "domino", "mamadou", "sniper", 
"travail", "lolotte", "pirate", "youyou", "titi", "hiphop", 
"angel1", "147852369", "valentine", "boulette", "doudoune", "jacques", 
"cambiami", "gilles", "poupoune", "lilou", "bambou", "kevin", 
"jesus", "dimitri", "didine", "456123", "tomtom", "TMM", 
"patrice", "cassandra", "toutou", "alexia", "mariam", "manon", 
"01234567891", "floflo", "portable", "metallica", "lacoste", "lyonnais", 
"juventus", "suzuki", "car", "canelle", "nadege", "qwe123", 
"loveyou", "sabine", "praline", "fondoom", "napoleon", "sofiane", 
"natacha", "janvier", "magali", "michael1", "moi", "killian", 
"aminata", "carpediem", "vacances", "esteban", "laura", "forever1", 
"paris", "fsd9shtyut", "angelina", "pioupiou", "tresor", "iloveu1", 
"amoureuse", "amoureux", "741852963", "mam", "123789", "mylene", 
"L58jkdjP!m", "pistache", "lololo", "6hBf28W791", "lucas", "010", 
"fripouille", "50cent", "poulette", "seigneur", "tulipe", "ramses", 
"emeline", "mahalkita1", "fabienne", "sweety", "picasso", "poiuytreza", 
"lapinou", "monange", "myriam", "axelle", "toietmoi", "a123456", 
"yassine", "winnie", "000", "pepito", "cachou", "mimi", 
"qsdfghjklm", "poiuyt", "1231231", "1111111111", "stargate", "playboy", 
"agathe", "jet", "toto", "gerard", "spiderman", "mat", 
"blabla", "aqwzsxedc", "angelo", "pompiers", "clochette", "connard", 
"passion", "012345", "rachid", "truand", "violette", "ytreza", 
"fleurs", "bertrand", "titoune", "biscotte", "champion", "blink182", 
"marseille1", "hotmail", "emploi", "drogba", "zebulon", "marmotte", 
"charlene", "bounty", "man", "francoise", "dom", "tamere", 
"georges", "123456789a", "thibault", "namour", "martinique", "nougat", 
"soprano", "nicole1", "toulouse31", "bogoss", "barbie", "mariage", 
"angele", "canard", "realmadrid", "laguna", "italie", "fraise", 
"momo", "aaaaa", "bouboule", "youssef", "mozart", "claudine", 
"marius", "mathias", "sasuke", "dorian", "paradis", "mireille", 
"merde", "kylian", "bon", "ricard", "6666661", "laurie", 
"nbvcxw", "kimbum1", "12301230", "gaetan", "tatiana", "tmm", 
"deborah", "cannabis", "montagne", "marjorie", "renault", "enfants", 
"vegeta", "manuel", "karima", "cannelle", "pompom", "kiki", 
"lulu", "clarisse", "sam", "pretty1", "ouioui", "252525", 
"9876543210", "myspace1", "yuantuo2012", "melodie", "mapuce", "0987654321", 
"sangoku", "ducati", "142536", "linkedin", "marley", "juillet", 
"sakura", "aaaa", "maelys", "novembre", "roucky", "melina", 
"parissg", "salome", "iloveu", "denise", "marguerite", "mou", 
"pascale", "pamela", "etienne", "chatte", "200", "3rJs1la7qE", 
"jesus1", "fra", "nantes", "yacine", "cou", "cloclo", 
"gaston", "anthony1", "mahalko1", "cocotte", "simone", "loveme", 
"guadeloupe", "pitchoune", "mamans", "couscous", "toutoune", "pikachu", 
"leslie", "qdujvyG5sxa", "pauleta", "choupinette", "maelle", "coco", 
"tahiti", "celibataire", "poupou", "madeleine", "151515", "charline", 
"soleil13", "philou", "marianne", "emmanuelle", "camion", "bobmarley", 
"cho", "ben", "741852", "diabolo", "barbara", "friendster1", 
"socrate", "0000000", "fairways", "nelson", "joshua1", "poulet", 
"octobre", "198", "raymond", "christian1", "balance", "solene", 
"azer", "roland", "looping", "aze123", "4567891", "popeye", 
"syl", "mylove", "bateau", "cheyenne", "solange", "maganda1", 
"junpyo1", "9876541", "prisca", "verseau", "bianca", "bamako", 
"alain", "7894561", "11111111111", "salut", "laurine", "panget1", 
"nutella", "5236", "johanna", "honey1", "clementine", "rammstein", 
"marvin", "cherie", "butterfly", "tarzan", "subaru", "azerty12", 
"7894561231", "124578", "renard", "kirikou", "fatoumata", "ang", 
"papa", "michou", "bestfriend1", "Eh1K9oh335", "143441", "111", 
"nanou", "athena", "anissa", "anais", "cameroun", "pommes", 
"evelyne", "ballon", "monbebe", "carotte", "100", "madrid", 
"bigboss", "moustique", "motocross", "san", "mamama", "decembre", 
"septembre", "josephine", "popopo", "cancer", "jul", "zezette", 
"geronimo", "loveyou1", "clara", "141414", "sayang1", "papounet", 
"joelle", "titou", "1122331", "titanic", "barcelona", "amitie", 
"bruno", "amo", "blanche", "246810", "sexe", "renaud", 
"fuckyou1", "gabrielle", "sweety1", "cynthia", "qsdfgh", "tigresse", 
"bebe", "fred", "antonio", "lamine", "khadija", "garfield", 
"007007", "pierrot", "lumiere", "louloutte", "diamant", "cecilia", 
"bisounours", "xbox360", "pourquoi", "superman1", "geraldine", "ale", 
"papamaman", "sesame", "null", "avenir", "tanguy", "sal", 
"sultan", "1212121", "lovelove", "hornet", "friends1", "reussite", 
"miguel", "mourad", "mmmmmm", "benfica", "roxanne", "lilian", 
"info", "frimousse", "asterix", "viviane", "onepiece", "lil", 
"suzanne", "bidule", "pretty", "flo", "magalie", "jojo", 
"afrique", "pou", "melody", "mathys", "alison", "mel", 
"securite", "demo", "vincent1", "lili", "paris75", "michele", 
"guizmo", "jupiter", "cochon", "gwada971", "enfant", "8888881", 
"120", "muriel", "202020", "penelope", "diesel", "181818", 
"josiane", "logitech", "magic", "elisabeth", "coline", "canabis", 
"abcdefg", "789", "09876543211", "joseph1", "gilbert", "000001", 
"madonna", "chloe", "rosalie", "pollux", "pap", "1q2w3e", 
"toulouse1", "99999", "ocean", "kenji", "bambi", "coincoin", 
"ken", "concorde", "minou", "perso", "abigail", "maeva", 
"saucisson", "teddy", "asdfgh1", "monchou", "azert1", "abcd", 
"frank", "alexandra1", "babouche", "aymeric", "aimer", "dragonball", 
"imene", "penis", "justine1", "azerty0", "douleur", "charly1", 
"rever", "skyrock", "isabella", "conan", "didier1", "morgane1", 
"demain", "savannah", "hector", "catalina", "babylove", "britney", 
"tomate", "nikos", "bambina", "skynet", "mangue", "triton", 
"revolte", "sexyboy", "connasse", "rap", "cyril", "cyber", 
"dominic", "copine", "sandy", "boucle", "raphael1", "camille1", 
"butterfly1", "sergio", "romeo", "caroline1", "ma", "marine1", 
"mazda", "sacha", "minipouce", "mystere", "lucie", "polux", 
"petite", "olivier1", "pokemon1", "emmanuelle1", "tatan", "123poil", 
"gothic", "familia", "fortune", "made", "pol", "auto", 
"morgane123", "banzai", "amour1", "smiley", "freeman", "blaise", 
"serrure", "lololo1", "micro", "sylvain1", "martini", "maison1", 
"ninou", "treize", "bribri", "maud", "pulsar", "cleo", 
"pouvoir", "bernard1", "marocaine", "tonton1", "bambou1", "horizon", 
"victor1", "emma", "free", "tomate1", "calamar", "century", 
"boris", "sylvia", "rencontres", "rania", "pablo", "2005", 
"twilight", "clem", "chocolat1", "djibril", "marjolaine", "2004", 
"gogo", "jane", "love1", "loulou1", "lion", "goldorak", 
"poireau", "baby", "chou", "patrick1", "seb", "reno", 
"cougar", "pingpong", "aime", "azazaz", "frederic1", "pascal1", 
"yaya", "mikado", "serge", "brahima", "mic", "flower1", 
"celine1", "star", "priscilla", "lol1", "marcel1", "je", 
"darth", "paul", "hello1", "marchand", "bob", "super", 
"moumou", "dure", "gino", "nathalie1", "benoit1", "satan", 
"jenifer", "elise", "louis", "chanel1", "flower13", "hamza", 
"suisse", "emile", "lana", "aster", "iop", "dylan", 
"baron", "melodie1", "kikou", "peche", "shadow1", "raf", 
"lapin", "33333", "vivi", "bilal", "beurk", "jiji", 
"olivier123", "rose", "alexis1", "mido", "yahoo", "dimitri1", 
"laetitia1", "azerty11", "pep", "vampire", "douda", "genesis", 
"nono", "djib", "november", "mya", "2008", "noel", 
"amer", "papa123", "matthieu1", "jesus123", "mouloud", "odile", 
"gaby", "lolo1", "les", "mimi1", "anto", "mik", 
"lancome", "cool1", "romane1", "richard1", "leo", "romain1", 
"prince1", "ibrahim", "mariama", "samer", "marinette", "hugodu13", 
"planet", "europe", "giovanni", "star13", "cameleon", "jojo1", 
"emile1", "roger", "roger1", "genevieve", "raptor", "cassie", 
"off", "space", "swimming", "dragon1", "raouf", "didi", 
"shadow13", "kenny", "maeva1", "cyrielle", "lili1", "alexandra123", 
"alice", "baba", "amine", "01234", "carlo", "wael", 
"jean", "juin", "choup", "vince", "france1", "prince123", 
"musique1", "sarah1", "panda", "maxim", "casa", "logan", 
"desire", "sofia", "caramel13", "plume", "tati", "fuck123", 
"al", "milan", "alban", "bib", "dan", "singer", 
"azerty13", "choupinou", "med", "kiki13", "bourriquet", "douda1", 
"alain1", "sarah123", "amel", "samsam", "severine1", "etoile1", 
"anis", "bb", "cel", "richie", "lala", "animaux", 
"titi13", "zouzou13", "impossible", "capitaine", "hugo", "free13", 
"houssem", "jayjay", "angeline", "gabriel1", "compte", "kilian", 
"brian", "planete", "dora", "paradis1", "soufiane", "lavie", 
"1981", "myriam1", "ninie", "antoine1", "schtroumpf", "harry", 
"bidou", "emilie123", "arcenciel", "natacha1", "majid", "yahia", 
"mamadou1", "azert123", "gold", "socrate1", "192837465", "kenzo", 
"happiness", "fille", "rose13", "amelie1", "driss", "ali", 
"angelique1", "cyborg", "karine1", "nael", "kool", "lool", 
"candy", "emma1", "albator", "supermoi", "zazou", "sahra", 
"baby13", "zinedine", "hacker", "personne", "laurie13", "bernie", 
"djamel", "morad", "tony", "dorine", "elsa", "camille123", 
"ange", "axel", "maeva123", "marine123", "gala", "du13", 
"exemple", "3125", "poupinette", "2002", "tommy", "charly123", 
"goal", "onizuka", "laurie123", "marianne1", "mat123", "qqqqqq", 
"bebe13", "golum", "maya", "bab", "stars", "lol13", 
"sword", "morad13", "3110", "toto1", "nick", "yassir", 
"bettyboop", "lina", "pierre123", "montreal", "hihihi", "marley1", 
"the", "paris1", "mohammed1", "dodo13", "ocean13", "wolf", 
"mathilde1", "azerty1234", "rossi", "solene1", "willy", "camelia", 
"mathieu123", "yoan", "mathis1", "perle", "sergent", "claude1", 
"mama", "bonjour13", "arcenciel13", "1980", "securite1", "roberto", 
"choupinette1", "patricia1", "leon", "perle1", "renaissance", "claude123", 
"kamel", "rockstar", "12345678a", "isabelle1", "00000001", "tango", 
"allo", "caterina", "daniel123", "dominique1", "anthony123", "jonathan1", 
"kaiser", "elfe", "celine123", "florence1", "1995", "amigo", 
"anthony13", "aaaaaaa", "mathilde123", "manuel123", "oh", "1998", 
"youyou13", "paulo", "alpha", "brice", "gohan", "ombre", 
"kaka", "berthelot", "nicolas1", "aubin", "computer1", "1994", 
"alfred", "snoop", "emilie1", "oceane123", "farid", "natacha123", 
"bbbbbb", "ros", "leila", "camille13", "brayan", "gaston123", 
"namaste", "claudine1", "vava", "tonio", "wolf13", "mohamed1", 
"mortelle", "amelia", "patricia123", "doudou13", "lolol", "sebastien1", 
"hardcore1", "gaston13", "1999", "pupuce13", "aurelie1", "nadia1", 
"mathieu13", "bernadette", "emo", "mamadou123", "1960", "loool", 
"123a", "amina", "merci", "yoann", "charlene1", "yvette", 
"tim", "amine1", "456456", "vol", "jimmy1", "camelia123", 
"1961", "1962", "lemon", "camille1234", "camelia1", "daniel13", 
"moi1", "valentin123", "ohm", "omar", "tiamo", "perle13", 
"fatou", "pimousse", "caillou", "sebastien123", "192837", "dragon13", 
"fantasy", "benjamin1", "berthelot1", "pirate13", "tabatha", "shadow123", 
"eloise", "martin1", "2023", "az", "pop", "timoth", 
"1963", "1928374651", "lulu13", "bapteme", "eternite", "valerie1", 
"coucou1", "1982", "1983", "1984", "1985", "1986", 
"1987", "1988", "eternite1", "timothee", "lucifer", "sylvia1", 
"juillet13", "cyril1", "jiji1", "jessica1", "rose123", "oooooo", 
"eh", "mehdi1", "free1", "1940", "000000000", "mom"]

root.mainloop()

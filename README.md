# CryPDF: 
Attaque par Dictionnaire sur PDF Verrouillés

---

**CryPDF** est un outil simple mais puissant conçu pour aider à déverrouiller les fichiers PDF protégés par mot de passe en utilisant une attaque par dictionnaire. Grâce à son interface graphique conviviale, vous pouvez rapidement tester des mots de passe à partir d'un dictionnaire prédéfini ou personnalisé.

![Capture d'écran de l'interface](https://github.com/Miiraak/CryPDF/blob/master/Images/img.png)

## Fonctionnalités

- **Interface Graphique Simple** : Choisissez facilement vos fichiers PDF et dictionnaires via une interface intuitive.
- **Attaque par Dictionnaire** : Testez des mots de passe à partir de fichiers dictionnaires pour déverrouiller vos PDFs.
- **Support Multithreading** : Utilisation de plusieurs threads pour accélérer l'attaque par dictionnaire.
- **Fenêtre de Résultat** : Affiche le mot de passe trouvé dans une fenêtre séparée avec une option de copie en un clic.

![Capture d'écran du résultat](https://github.com/Miiraak/CryPDF/blob/master/Images/imgDone.png)

## Installation

Pour utiliser CryPDF, assurez-vous d'avoir Python installé sur votre système. <br>
Clonez le dépôt et installez les dépendances nécessaires :

```bash
  git clone https://github.com/Miiraak/CryPDF.git
  cd CryPDF
  pip install -r requirements.txt
```
ou 

Téléchargez l'executable sous [Releases](https://github.com/Miiraak/CryPDF/releases)

## Utilisation
#### Lancer l'Application :
Exécutez le script principal pour ouvrir l'interface graphique. <br>
```bash
python crypdf.py
```
ou 
```
Lancez l'executable.
```

#### Choisir un PDF :
Cliquez sur le bouton PDF pour sélectionner le fichier PDF que vous souhaitez déverrouiller. (requis)

#### Choisir un Dictionnaire :
Cliquez sur le bouton Dictionary pour sélectionner le fichier contenant les mots de passe à tester. (optionnel)

#### Lancer l'Attaque :
Cliquez sur le bouton Attack pour commencer l'attaque par dictionnaire. Si le mot de passe est trouvé, il sera affiché dans une nouvelle fenêtre avec l'option de copie.

## Contribuer :
Les contributions sont les bienvenues ! Pour proposer des améliorations ou signaler des bugs, veuillez ouvrir une issue ou soumettre une pull request sur le dépôt GitHub.

---

# Avertissement 
Bien que ce soit "gentillet", cela reste illégal de forcer des PDF ne vous appartenant pas !
### _Je ne saurais être tenu responsable de vos exactions les gus_

---

## License :
Ce logiciel est fourni sous license [MIT](https://github.com/Miiraak/CryPDF/blob/master/LICENSE)

## :sparkling_heart: Merci à :

Dictionnaires :

- [Richelieu - Tarraschk](https://github.com/tarraschk/richelieu) - [(CC BY 4.0 license)](https://creativecommons.org/licenses/by/4.0/)
- [CrackStation's Password Cracking Dictionary](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm) - [(CC BY SA 3.0 license)](https://creativecommons.org/licenses/by-sa/3.0/deed.en)
- [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords) - [(MIT License)](https://github.com/danielmiessler/SecLists/blob/master/LICENSE)

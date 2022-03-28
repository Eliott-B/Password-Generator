"""
Created on Mon Mar 28 15:48:02 2022

@author: Eliott-B
"""
from random import choice

def Create_Password()->str:
    """Créer un mot de passe composé de 16 caractères dont au moins un caracère spécial,
    un chiffre, une lettre minuscule et une lettre majuscule."""
    password = ""
    for i in range(16):
        password += choice([chr(i) for i in range(33,126)])
    if Verify_Password(password) == True:
        return password
    elif Verify_Password(password) == False:
        return Create_Password

def Verify_Password(password:str)->bool:
    """Retourne True si le mot de passe est complet."""
    c_speciaux = False
    c_chiffre = False
    c_majuscule = False
    c_minuscule = False
    speciaux = [chr(i) for i in range(33,47)] + [chr(j) for j in range(58,64)] + [chr(k) for k in range(91,96)] + [chr(123)] + [chr(m) for m in range(125,126)]
    majuscule = [chr(i) for i in range(65,90)]
    minuscule = [chr(i) for i in range(97,122)]
    chiffre = [chr(i) for i in range(48,57)]
    for elt in password:
        for k in speciaux:
            if elt == k:
                c_speciaux = True
        for m in majuscule:
            if elt == m:
                c_majuscule = True
        for n in minuscule:
            if elt == n:
                c_minuscule = True
        for o in chiffre:
            if elt == o:
                c_chiffre = True
    if c_speciaux == True and c_majuscule == True and c_minuscule == True and c_chiffre == True:
        return True
    else:
        return False


password = open("password.txt","a")
nom = input("What's the web site ? ")
password.write(nom + " : " + Create_Password()+"\n")
password.close()
